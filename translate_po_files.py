#!/usr/bin/env python3

"""Automatically translate po files with deepl."""
import argparse
import html

import itertools
import logging
import re
import os
from pathlib import Path

import deepl
import polib
from polib import POEntry
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger(__name__)
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY")
assert DEEPL_API_KEY, "DEEPL_API_KEY env not set"
deepl_client = deepl.DeepLClient(os.environ["DEEPL_API_KEY"])

SINGULAR_FORMS_EXCEPTIONS = {
    # Arabic has a special form for 0, so the singular form is actually the on index 1.
    # https://www.gnu.org/savannah-checkouts/gnu/gettext/manual/html_node/Plural-forms.html
    "ar": 1,
}

ALL_LANGUAGES = {
    "ar": "ar",
    "es": "es",
    "fr": "fr",
    "ru": "ru",
    "zh_CN": "zh-hans",
}


class PoTranslator:
    comment = "Requires manual validation; translated with DeepL"
    type = "singular"

    def __init__(self, code, po_path, formality="prefer_more"):
        self.code = code
        self.po_path = po_path
        self.po = polib.pofile(self.po_path)
        self.done_count = 0
        self.untranslated_count = len(self.po.untranslated_entries()) + len(
            self.po.fuzzy_entries()
        )
        self.batch_size = 50
        self.formality = formality

    @property
    def singular_index(self):
        return SINGULAR_FORMS_EXCEPTIONS.get(self.code, 0)

    @staticmethod
    def remove_table_nodes(text):
        # The col/row spans don't need to be in the translated string for some reason.
        # So remove them here before sending to the translation API.
        pattern = r"{(rspan|cspan)}`\d+`"
        return re.sub(pattern, "", text)

    @staticmethod
    def wrap_placeholders(text):
        patterns = [
            r"{\w+}",  # {name}
            r"%\(\w+\)\w",  # %(name)s
        ]

        def replacer(match):
            return f"<x>{match.group(0)}</x>"

        for pattern in patterns:
            text = re.sub(pattern, replacer, text)
        return text

    @staticmethod
    def unwrap_placeholders(text):
        # Remove <x> tags around placeholders
        return re.sub(r"</?x>", "", text)

    def get_string(self, entry: POEntry):
        return entry.msgid

    def set_string(self, entry: POEntry, result: str):
        entry.msgstr = result
        if entry.msgid_plural:
            entry.msgstr_plural[self.singular_index] = result

    def translate(self):
        logger.info(
            "%s: Translating %s entries out of %s total... (%s)",
            self.code,
            self.untranslated_count,
            len(self.po),
            self.type,
        )
        for entry_batch in itertools.batched(
            itertools.chain(self.po.untranslated_entries(), self.po.fuzzy_entries()),
            self.batch_size,
        ):
            texts = []
            entries = []
            for entry in entry_batch:
                msg = self.get_string(entry)
                msg = self.remove_table_nodes(msg)
                msg = self.wrap_placeholders(msg)

                if msg:
                    texts.append(msg)
                    entries.append(entry)

            if not texts:
                continue

            results = deepl_client.translate_text(
                text=texts,
                target_lang=ALL_LANGUAGES[self.code],
                tag_handling="xml",
                ignore_tags="x",
                formality=self.formality,
            )

            for entry, result in zip(entries, results, strict=True):
                translated_text = self.unwrap_placeholders(result.text)
                # The DeepL library would have escaped the HTML entities for us, so
                # return it to its original form.
                translated_text = html.unescape(translated_text)

                self.set_string(entry, translated_text)
                entry.tcomment = self.comment
                # Reset entry if it was fuzzy before
                entry.fuzzy = False
                entry.previous_msgid = None
                entry.previous_msgctxt = None
                entry.previous_msgid_plural = None

            self.done_count += len(entry_batch)
            # Save after each batch to preserve progress in case of interruptions
            self.po.save(self.po_path)
            logger.info(
                "%s: %s/%s done", self.code, self.done_count, self.untranslated_count
            )


class PoTranslatorPlural(PoTranslator):
    type = "plural"

    def get_string(self, entry: POEntry):
        return entry.msgid_plural

    def set_string(self, entry: POEntry, result: str):
        # For languages that have more than one plural form such as Arabic,
        # these translations may be especially bad. But there's nothing
        # we can do about that.
        for index in entry.msgstr_plural:
            if index == self.singular_index:
                continue
            entry.msgstr_plural[index] = result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-l", "--lang", action="append")
    parser.add_argument("-p", "--po-file", default="*")
    args = parser.parse_args()

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    for code in args.lang or ALL_LANGUAGES:
        locale_path = Path("./locales") / code / "LC_MESSAGES"
        for po_path in locale_path.glob(f"{args.po_file}.po"):
            logger.info("Translating %s", po_path)
            # Instead of just putting the plural forms in the same batch, do it
            # in another new run. As the batch might go over the max amount and
            # DeepL will reject the API.
            PoTranslator(code, po_path).translate()
            PoTranslatorPlural(code, po_path).translate()


if __name__ == "__main__":
    main()
