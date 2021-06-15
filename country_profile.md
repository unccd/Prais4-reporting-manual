# Country profile

## Purpose

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

[^2]: https://esa.un.org/unpd/wup/DataQuery/
[^3]: https://data.worldbank.org/indicator/SP.POP.TOTL?locations=AF

Countries should ensure that data on demographics is consistent with data on poverty and drinking water

## Complementary information

Population datasets that have been further disaggregated (by labor force, age, male/female) are available
from the World Bank. This disaggregated data may assist in the interpretation of population dynamics and
potential population pressures. Any additional disaggregated data should also be uploaded to the PRAIS.

## Images

![Image name](https://d33wubrfki0l68.cloudfront.net/eab45e25bb79970178fab7a2d10cba0209372a59/94d9e/assets/images/philly-magic-garden.jpg "This is the tooltip")

![Internal image 2](/img/80-CMEMS-TAC-WIND.png "Tooltip 2")


## Tables

| Column 1 |   Column 2 |
| -------- | ---------- |
| Header     | Title       |
| Paragraph     | Text        |


## Basic formatting

Use double asterisks for **bold text**. It also works with __double underscores__.
Use single asterisks or underscores for *italic* _text_.
Use three asterisks for ***really important*** text.


## Blockquotes

Blockquotes can contain multiple paragraphs. Add a > even on the blank lines between the paragraphs.

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
> Blockquotes can contain formatting such as **bold text** or lists:
> - item 1
> - item 2
> 

## Numbered lists

Lines starting with numbers followed by periods are converted to numbered lists. You don't have to number each item manually, you can use number one for all items:

1. First item
2. Second item
3. Third item


## Boxes

```{note} This is a default note, without any arguments.
```

```{admonition} Orange title
:class: warning

This is a warning
```

```{admonition} Red title
:class: error
This is an error
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

### Tables (RST style)

```{eval-rst}
.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Popcorn", 1.99, "Straight from the oven"
```
