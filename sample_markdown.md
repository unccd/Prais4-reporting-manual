# Heading level 1

## Heading level 2

### Heading level 3

This information is required to facilitate analysis of the progress indicators for strategic objectives 1 and 2.


## About footnotes

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.


## Land area

Information relating to land area is required over several years to calculate the proportion of land covered by
each land cover class (SO1-1) and the proportion of land that is degraded over total land area (Sustainable
Development Goal indicator 15.3.1). This information is also useful to investigate possible climate impacts,
which could be potentially identified by the reduction in size of permanent water bodies, the disappearance of
permanent water bodies and the loss of coastline.

Total land area, water body area and total country area require respective estimates to be reported in km<sup>2</sup> for
the corresponding year. Land area data is pre-filled in the reporting template. The pre-filled data is editable
and thus can be adjusted if these estimates have changed. Any changes are to be justified in the ‘Comments’
column.

Countries should ensure that data on land area is consistent with data on land cover and on the proportion of
land that is degraded.

## Demographics

Demographics are required over several years to estimate the proportion of population below the international
poverty line (SO2-1) and proportion of population using safely managed drinking water services (SO2-2).
Information relating to population is also useful to ascertain how much pressure the increases in population
are having on land capital in both rural and urban areas.

Population estimates should be reported in thousand inhabitants. Population estimates can be accessed from
website of the United Nations, Department of Economic and Social Affairs, Population Division[^2] and/or from
the World Bank website.[^3]

[^2]: [https://esa.un.org/unpd/wup/DataQuery](https://esa.un.org/unpd/wup/DataQuery/)
[^3]: [World Bank data](https://data.worldbank.org/indicator/SP.POP.TOTL?locations=AF)

Countries should ensure that data on demographics is consistent with data on poverty and drinking water

## Complementary information

Population datasets that have been further disaggregated (by labor force, age, male/female) are available
from the World Bank. This disaggregated data may assist in the interpretation of population dynamics and
potential population pressures. Any additional disaggregated data should also be uploaded to the PRAIS.

## Images

![Alt-text for the first image](https://d33wubrfki0l68.cloudfront.net/eab45e25bb79970178fab7a2d10cba0209372a59/94d9e/assets/images/philly-magic-garden.jpg "This is the tooltip")

![Alt-text for the second image](/img/80-CMEMS-TAC-WIND.png "Tooltip 2")


## Basic formatting

Use double asterisks for **bold text**. It also works with __double underscores__.
Use single asterisks or underscores for *italic* _text_.
Use three asterisks for ***really important*** text.


## Quoted text

Blockquotes can contain multiple paragraphs. Add a > even on the blank lines between the paragraphs.

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
> Blockquotes can contain formatting such as **bold text** or lists:
> - item 1
> - item 2
> 

Example 2:

    Indenting text with 4 spaces or a tab shows the text as a code block.
    The text can span across multiple lines.



## Numbered lists

Lines starting with numbers followed by periods are converted to numbered lists. You don't have to number each item manually, you can use number one for all items:

1. First item
2. Second item
3. Third item


## Boxes

```{note} This is a default note, without any arguments.
```

```{admonition} Blue title
:class: note

This is a note, but in a different way
```

```{admonition} Orange title
:class: warning

This is a warning
```

```{admonition} Red title
:class: error
This is an error
```

```{admonition} Green title
:class: hint
This is a note
```

## Definition lists

To use definition lists and other formatting supported by ReStructuredText, use the `{eval-rst}` directive.

```{eval-rst}

Term 1
    Definition
Term 2
    Definition paragraph 1.
    Definition paragraph 2.
Term 3
    Definition paragraph A.

    Definition paragraph B.

```

## Tables (Markdown style)

| Column 1 |   Column 2 |
| -------- | ---------- |
| Header     | Title       |
| Paragraph     | Text        |


### Tables (RST style)

```{eval-rst}
.. list-table:: Table title
   :widths: 25 25 50
   :header-rows: 1
   :align: center

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
```

```{eval-rst}
.. list-table:: Transition Matrix
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   :align: center
   :class: transition-matrix

   * - IPCC Class
     - Forest Land
     - Grassland
     - Cropland
     - Wetlands
     - Settlements
     - Other Land
   * - Forest Land
     - Stable
     - Vegetation loss
     - Deforestation
     - Innundation
     - Deforestation
     - Vegetation loss
   * - Grassland
     - Aforestation
     - Stable
     - Agricultural expansion
     - Innundation
     - Urban expansion
     - Vegetation loss
   * - Cropland
     - Aforestation
     - Withdrawal of Agriculture
     - Stable
     - Innundation
     - Urban expansion
     - Vegetation loss
   * - Wetlands
     - Woody Encroachment
     - Wetland drainage
     - Wetland drainage
     - Stable
     - Wetland drainage
     - Wetland drainage
   * - Settlements
     - Aforestation
     - Vegetation establishment
     - Agricultural expansion
     - Wetland establishment
     - Stable
     - Withdrawal of Settlments
   * - Other Land
     - Aforestation
     - Vegetation establishment
     - Agricultural expansion
     - Wetland establishment
     - Urban expansion
     - Stable
```

```{eval-rst}
.. csv-table:: CSV Table - data can be stored in .CSV files
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Popcorn", 1.99, "Straight from the oven"


```


### Links

[This](https://duckduckgo.com) is a link to <https://www.markdownguide.org>.

HTML is also supported: <a href="http://example.com/" target="_blank">Hello, world!</a>.


### Sidebars (RST style)

The sidebar goes first, then the main text.

```{eval-rst}

.. sidebar:: Sidebar title

    This is the sidebar text

    .. image:: img/79-CMEMS-TAC-SST.png

    *Caption* This is the image caption
```

If a land degradation map or a ‘support class’ map, which show which indicator or combination of
indicators supports the classification of ‘degraded’ or ‘not degraded’ for a given pixel or land unit,
were produced, they should be uploaded to the PRAIS. Any indicator datasets used to assess the
proportion of land that is degraded, that have not already been included as part of the previous
reporting on indicators SO1: 1-3, should be uploaded to the PRAIS.

Voluntary targets can be set to achieve SO1 and therefore “to improve the condition of affected
ecosystems, combat desertification/land degradation, promote sustainable land management and
contribute to land degradation neutrality”. This includes the formulation by countries of LDN targets
in accordance with their specific national circumstances and development priorities.

The 2018 reporting will describe the countries’ level of ambition in achieving SO1.

------

End of sample text
