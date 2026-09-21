from __future__ import annotations

import unicodedata
from collections import defaultdict

from docutils import nodes
from docutils.parsers.rst import Directive
from pypinyin import lazy_pinyin
from sphinx.addnodes import glossary as glossary_node
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform


ALPHABETS = {
    "en": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "fr": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "es": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",

    # Russian alphabet, including Ё.
    "ru": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",

    # Arabic alphabet.
    "ar": "ابتثجحخدذرزسشصضطظعغفقكلمنهوي",

    # Chinese pinyin uses the Latin alphabet.
    "zh_CN": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}


class MultilingualGlossaryIndex(nodes.General, nodes.Element):
    pass


class MultilingualGlossaryIndexDirective(Directive):
    has_content = False

    def run(self):
        return [MultilingualGlossaryIndex()]


def normalize_text(text: str) -> str:
    """
    Unicode-normalize text and remove leading whitespace.
    """
    return unicodedata.normalize("NFC", text).strip()


def first_meaningful_character(text: str) -> str:
    """
    Find the first meaningful Unicode character.

    Formatting characters and punctuation are skipped.
    """
    text = normalize_text(text)

    for char in text:
        category = unicodedata.category(char)

        if category.startswith("C"):
            continue

        if category.startswith("P"):
            continue

        return char

    return ""


def language_code(app: Sphinx) -> str:
    return app.config.language or "en"


def chinese_initial(text: str) -> str:
    """
    Return the Pinyin initial of the first meaningful Chinese character.

    Examples:
        中国 -> Z
        北京 -> B
        生态系统 -> S
        水资源 -> S
    """
    text = normalize_text(text)

    if not text:
        return ""

    # Find first character that isn't punctuation/formatting.
    first = first_meaningful_character(text)

    if not first:
        return ""

    # pypinyin returns the pronunciation of the character.
    result = lazy_pinyin(
        first,
        errors="keep",
        strict=False,
    )

    if not result:
        return first.upper()

    pinyin = result[0]

    try:
        # First Latin character of the Pinyin syllable.
        return pinyin[0].upper()
    except IndexError:
        return first.upper()


def get_initial(text: str, app: Sphinx) -> str:
    """
    Determine the grouping letter for a glossary term.
    """
    lang = language_code(app)

    if lang == "zh_CN":
        return chinese_initial(text)

    return first_meaningful_character(text)


def sort_letters(letters, app: Sphinx):
    """
    Sort the navigation letters according to the current language.
    """
    lang = language_code(app)
    alphabet = ALPHABETS[lang]

    order = {
        char.casefold(): index
        for index, char in enumerate(alphabet)
    }

    def key(value):
        folded = value.casefold()

        if folded in order:
            return 0, order[folded]

        # Some terms have digits as first characters
        return 1, folded

    return sorted(letters, key=key)


def sort_terms(terms):
    """
    Sort glossary terms alphabetically within a group.
    """
    return sorted(
        terms,
        key=lambda item: normalize_text(item[0]).casefold(),
    )


def find_glossary_terms(document):
    """
    Find terms from the Sphinx glossary in the current doctree.

    Returns:
        [(display_text, target_id), ...]
    """
    result = []

    for glossary in document.findall(glossary_node):
        for term in glossary.findall(nodes.term):
            text = term.astext().strip()

            if not text:
                continue

            ids = term.get("ids", [])

            if not ids:
                continue

            result.append(
                (text, ids[0])
            )

    return result


class MultilingualGlossaryIndexTransform(SphinxPostTransform):
    # Run as a post-transform, after translation has been applied.
    default_priority = 500

    def run(self, **kwargs):
        document = self.document
        app = self.app

        index_nodes = document.findall(
            MultilingualGlossaryIndex
        )

        if not index_nodes:
            return

        terms = find_glossary_terms(document)

        if not terms:
            for index in index_nodes:
                index.replace_self(
                    nodes.paragraph(
                        text="No glossary terms found."
                    )
                )

            return

        groups = defaultdict(list)

        for text, target_id in terms:
            initial = get_initial(
                text,
                app,
            )
            if initial:
                groups[initial].append(
                    (text, target_id)
                )

        # Sort terms inside each group.
        for initial in groups:
            groups[initial] = sort_terms(
                groups[initial]
            )

        letters = sort_letters(
            groups.keys(),
            app,
        )

        container = nodes.container()
        nav = nodes.paragraph()

        for position, letter in enumerate(letters):
            if position > 0:
                nav += nodes.Text(" ")

            anchor_id = self.anchor_id(letter)
            reference = nodes.reference(
                "",
                letter,
                refid=anchor_id,
            )

            nav += reference

        container += nav

        for letter in letters:
            anchor_id = self.anchor_id(
                letter
            )

            section = nodes.section(
                ids=[anchor_id],
            )

            section += nodes.title(
                "",
                letter,
            )

            bullet_list = nodes.bullet_list()

            for text, target_id in groups[letter]:
                item = nodes.list_item()

                paragraph = nodes.paragraph()
                paragraph += nodes.reference(
                    "",
                    text,
                    refid=target_id,
                )

                item += paragraph
                bullet_list += item

            section += bullet_list
            container += section


        # Give navigation a stable ID, maybe it's useful later
        nav["ids"] = [
            self.navigation_id()
        ]

        # Replace directive with the actual DOM
        # Make a deepcopy for immutability
        for index in index_nodes:
            index.replace_self(
                container.deepcopy()
            )

    @staticmethod
    def navigation_id():
        return "glossary-index"

    @staticmethod
    def anchor_id(letter):
        """
        Generate a stable ID.

        A Unicode-safe ID isn't necessary here because we use the
        Unicode code point(s).
        """
        codepoints = "-".join(
            f"{ord(char):x}"
            for char in letter
        )

        return f"glossary-index-{codepoints}"


# Sphinx setup
def setup(app: Sphinx):
    app.add_node(
        MultilingualGlossaryIndex,
        html=(
            lambda node: None,
            lambda node: None,
        ),
    )
    app.add_directive(
        "multilingual-glossary-index",
        MultilingualGlossaryIndexDirective,
    )
    app.add_post_transform(
        MultilingualGlossaryIndexTransform
    )

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
