# 3. Strategic objective 3: To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems

## 3.1. SO 3-1 – Trends in the proportion of land under drought over the total land area

### 3.1.1. Introduction

Drought is defined as a period of dry weather long enough to cause a serious hydrological imbalance (World Meteorological Organization (WMO), 1992). The United Nations Convention to Combat Desertification (UNCCD) defines drought as the naturally occurring phenomenon that exists when precipitation has been significantly below normal recorded levels, causing serious hydrological imbalances that adversely affect land resource production systems[^1].

[^1]: "UNCCD. 1994. Article 1 of the Convention Text: <http://www2.unccd.int/sites/default/files/relevant-links/2017-01/UNCCD_Convention_ENG_0.pdf> "

Indicator SO 3-1 specifically describes the status of meteorological drought hazards that occurred during the baseline and reporting periods within a country.

There are several drought indices that might be used to estimate national drought hazard. The UNCCD methodology to estimate indicator SO 3-1 recommends using a globally accepted drought index, the Standardized Precipitation Index (SPI), to characterize the meteorological drought hazard. However, Parties may report using other indices if already in use at national level. For example, the Standardized Precipitation Evapotranspiration Index (SPEI) may represent an alternative index, readily comparable to the SPI, that provides more reliable signals of drought in arid areas. Parties using the SPEI can apply the same methods recommended in this manual and in the “Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3” to report indicator SO 3-1. For other indices currently in use, Parties may need to ensure statistical consistency with the SPI drought intensity classes described in table 19[^2].

[^2]: "The Global Drought Classification System (GDCS, formerly the Global Drought Indicator or GDI), currently under development by WMO through the Global Multi-Hazard Alert System (GMAS) framework, will provide methods on how a multitude of drought indices can be translated onto a harmonized legend of drought classes."

The overall objective is for Parties to assess drought hazard and identify areas exposed to extreme drought in order to prioritize mitigation efforts in conjunction with assessments of drought exposure (SO 3-2) and vulnerability (SO 3-3). National reporting is facilitated though the provision of default data.

### 3.1.2. Prerequisites for reporting

- An in-depth reading of chapter 1 of the [“Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3: To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems”](https://www.unccd.int/publications/good-practice-guidance-national-reporting-unccd-strategic-objective-3-mitigate-adapt) detailing the methodology used to estimate drought hazards and the changes over time.

- Data complying with the specifications listed in figure 1 and table 18.

- A pool of national experts officially nominated by the national authorities to verify the consistency of the results of the reporting process with the situation in the field, or to develop and implement a custom methodology to estimate indicator SO 3-1 where national data are preferred to the default data. Key institutions might include a country’s national meteorological and hydrological service (NMHS), ministry of environment, ministry of agriculture, remote sensing centre and national statistical office, as well as relevant universities and research centres.

### 3.1.3. Reporting process and step-by-step procedure

The step-by-step procedure for reporting is described in the following. If the default data is used, steps 2 to 5 are unnecessary.

#### Step 1: Select precipitation dataset

The UNCCD provides default data from the Global Precipitation Climatology Centre (GPCC) Monitoring Product, a gridded precipitation product derived from rain gauge data. Parties have the option to use an alternative default dataset in Trends.Earth: the Climate Hazards Group InfraRed Precipitation with Stations (CHIRPS), which produces high-resolution estimates based on satellite observations and gauged station data. While the higher spatial resolution of CHIRPS and slightly longer recording period are advantageous when deriving the SPI, it has a ‘quasi-global’ coverage that spans 50°S to 50°N. Therefore, Parties with country boundaries exceeding this range will not be able to use the CHRIPS dataset. In contrast, the GPCC precipitation data has global coverage.

Parties wishing to use in-country data provided by the NMHS or regional, rather than global, precipitation products can use the decision tree in figure 1 to assess whether the in-country (or regional) precipitation data is more appropriate to derive indicator SO 3-1 over the globally available datasets.

_Figure 1. Decision tree to help Parties chose the best precipitation data source to derive indicator SO 3-1_
````{ifconfig} language == 'en'
```{image} /img/SO3_Decision_tree.jpg
```
````
````{ifconfig} language == 'ru'
```{image} /img/Figure_1-RU.jpg
```
````
````{ifconfig} language == 'ar'
```{image} /img/Figure_1-AR.jpg
```
````
````{ifconfig} language == 'zh'
```{image} /img/Figure_1-ZH.png
```
````
````{ifconfig} language == 'es'
```{image} /img/Figure_1-ES.png
```
````
````{ifconfig} language == 'fr'
```{image} /img/Figure_1-FR.png
```
````


_GPCC: Global Precipitation Climatology Centre_{{br}}
_SPI: Standardized Precipitation Index_{{br}}
_CHIRPS: Climate Hazards Group InfraRed Precipitation with Stations_

This decision-making process should help Parties identify data that meets the specifications summarized in table 18.

{{pagebreak}}

```{tabularcolumns} |p{3.5cm}|p{5cm}|p{6cm}|
```

```{flat-table} *__Table 18__. Data specifications for SO 3-1 Indicator*
---
header-rows: 2
widths: 2 3 3
---
* - {rspan}`1` Item
  - {cspan}`1` Specifications
* - Default data
  - National data
* - __Input data__

    (Data needed to generate drought hazard estimates based on the Standardized Precipitation Index (SPI) calculations described in Step 2)
  - Global Precipitation Climatology Centre (GPCC) monthly precipitation products,1982–present.
  - Gridded products of monthly precipitation derived from national gauge networks. The dataset should ideally have a continuous record of at least 30 years, covering the period 1981–2010.
  
    For countries in the 50°S to 50°N range: Climate Hazards Group InfraRed Precipitation with Stations (CHIRPS) monthly precipitation products, 1981–present, can be accessed in Trends.Earth{sup}`*`.
* - __Output data__

    (Intermediate and final gridded products resulting from the analysis described in Steps 2 to 4)
  - Annual December SPI-12 grids classified into four SPI drought intensity classes for the baseline and reporting periods{sup}`*`.

    Total land area for each drought intensity class as well as proportion of total land area under drought.

    Gridded spatial summary in four-year epochs.
  - Annual December SPI-12 grids classified into four SPI drought intensity classes for the baseline and reporting periods{sup}`*`.

    Total land area for each drought intensity class as well as proportion of total land area under drought.

    Gridded spatial summary in four-year epochs.
* - __Classification__
  - Four SPI drought intensity classes as per table 19.
  - Four SPI drought intensity classes as per table 19.
* - __Spatial resolution__
  - GPCC: 1.0° x 1.0° (~111 km)
  - CHIRPS: 0.05° x 0.05° (~5.55 km) or otherwise assessed by national authorities based on available data
* - __Quality__
  - Specified in the datasets’ metadata.
  - Data should be continuous where possible; where data completeness is less than 85%, Parties may consider filling data gaps in accordance with guidance from the World Meteorological Organization.
* - __Metadata__
  - Metadata information is provided with default data.
  - Minimum metadata content as per the mandatory fields listed in Annex II.
```

{sup}`*` _As stated in Step 3, the December SPI-12 values represent the precipitation deficits (or excesses) over the Gregorian (January–December) calendar year._

#### Step 2:  Calculate the Standardized Precipitation Index

Monthly time series of the SPI are based on the selected gridded precipitation data and calculated using the SPI-12 method, which provides an annual summary of precipitation deficits for each month using a 12-month accumulation method. For example, the 12-month precipitation accumulation for April 2019 is the total monthly precipitation for May 2018 to April 2019.

In order to normalize the 12-month precipitation accumulation data distributions, the WMO climatological standard normal period of 1981–2010 is used as a reference period. The normalization method is based on a Gamma probability distribution function fitted to the 12-month precipitation accumulations in this reference period. Thus calculated, these probability distribution parameters are then applied to any time series of monthly 12-month precipitation accumulations to produce the normalized monthly SPI-12 time series for each grid cell for the entire recording period. However, a change in the standard climate normal period necessitates a recalculation of the SPI for the baseline and all historic reporting periods. As such, it is recommended that the reference period used to calculate the SPI be clearly stated in national reports of indicator SO 3-1 to the UNCCD.

Default SPI data is available in Trends.Earth for the purposes of SO3 monitoring. However, there are various open access tools that can be used to derive the SPI, a selection of which is listed in table 3 of the Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3.

#### Step 3: Identify the drought intensity class of each grid cell based on the calculated Standardized Precipitation Index value

```{note}
Related areas in the PRAIS 4 platform: table SO3-1.T1
```

To assess the SPI time series for the baseline and reporting periods, the December SPI-12 values for each year should be extracted. The December SPI-12 values represent the precipitation deficits (or excesses) over the Gregorian (January–December) calendar year.

For each of the December SPI-12 grids, the number of cells belonging to each of the SPI drought intensity classes listed in table 19 should be counted. Positive SPI values are discarded, since they indicate that there was no drought in the given period.

```{list-table} *__Table 19__. Standardized Precipitation Index (SPI) drought intensity classes*
---
header-rows: 1
---
* - SPI values
  - Drought intensity class
* - 0 to -0.99
  - Mild drought
* - -1.0 to -1.49
  - Moderate drought
* - -1.5 to -1.99
  - Severe drought
* - -2 and less
  - Extreme drought
```

The total area under each drought intensity class should be derived in a two-step process:

(i) Project the drought intensity class grid into a suitable equal area projection (e.g., Mollweide) to obtain the cells’ area in km{sup}`2`.

(ii) Combine all cells’ area in a given drought class to get the total area under each drought intensity class.

#### Step 4:  Calculate proportion of land under drought

```{note}
Related areas in the PRAIS 4 platform: table SO3-1.T2
```

The proportion of land in each drought intensity class is calculated for each reporting year as a percentage of the total land area.

For each of the SPI-12 grids in the baseline and reporting period, the number of cells falling under each of the SPI drought intensity classes is counted (cellCount). Then, for each reporting year, the percentage of the total land area in each drought intensity class is calculated. The formula is as follows:

$P_{ij} = \frac{cellCount_{ij}}{Total\ number\ of\ cells} \times 100$

Where:

- “P{sub}`ij`” is the proportion of land under the drought intensity class _i_ in the reporting year _j_
- “cellCount{sub}`ij`” is the number of pixels under the drought intensity class _i_ in the reporting year _j_
- “Total number of cells’” is all the grid cells within the country Party’s land area.

The total area falling under each of the drought intensity classes in each year is calculated by multiplying cellCount by the area of the cells (a constant value, since the drought intensity class grid was previously converted to an equal-area projection).

#### Step 5:  Create a gridded spatial summary for the baseline and reporting periods

In addition to the tabular reports described above, indicator SO 1-3 should also be summarized spatially to map the most extreme conditions that occurred in the baseline and reporting periods.

To summarize the reporting period spatially, the most extreme drought intensity class should be identified for each grid cell for each reporting year within the reporting period.

Data for the baseline period should be summarized spatially using the gridded SPI-12 data in four-year intervals (2000–2003, 2004–2007, 2008–2011 and 2012–2015), reflecting the reporting periods used for SO3 monitoring. In this case, the most extreme drought intensity class should be reported for each grid cell for each four-year period within the baseline.

#### Step 6: Verify the results

Parties should be aware of the limitations related to the use of SPI as a single drought indicator and critically review the default data vis-à-vis the national rain gauge data and other meteorological sources before submitting the reports to the UNCCD.

#### Step 7: Generate reports

Once verified by the Parties, the estimated drought hazard values for the reporting and baseline periods should be officially submitted to the UNCCD. Observed changes and their interpretation may be described in the “Qualitative Assessment” field of the PRAIS 4 platform.

Default maps or maps generated in Trends.Earth using national data representing drought hazard for the baseline/reporting period are made available in the PRAIS 4 platform. More specifically, the following maps will be available:

- Drought hazard in first epoch of baseline period (2000–2003)
- Drought hazard in second epoch of baseline period (2004–2007)
- Drought hazard in third epoch of baseline period (2008–2011)
- Drought hazard in fourth epoch of baseline period (2012–2015)
- Drought hazard in the reporting period (2016–2019)

These maps represent the most extreme conditions that occurred in each epoch, as explained in Step 5. Parties are also encouraged to submit narratives on the methodology, data sources and data accuracy in the event that the estimates are derived from national data using the “General Comment” field. It would also be beneficial to report on special cases and issues, describing situations where SPI values might be less reliable and providing the rationale to adopt a different methodology.

### 3.1.4. Dependencies

Drought hazard data relies on the total land area reported in table SO1-1.T1 to calculate the proportion of total land area under drought.
SO 3-1 outputs are also used as an input for calculating indicator SO 3-2.

### 3.1.5. Challenges

#### Data availability and quality

- Internationally available precipitation data might not be sufficiently accurate to estimate the intensity of drought hazard at national level. The use of national data is recommended because it is assumed to be more precise and reliable. However, national precipitation data might not be readily available in digital form and/or might be affected by gaps in the time series.

#### Limitations of the SPI-based estimates

- While the SPI is recommended as a well-established, flexible and robust drought index to quantify drought hazard on a global scale, it only quantifies the meteorological deficits, since it is solely based on precipitation, and other types of drought (e.g., hydrological, agricultural) may not be well captured. Moreover, in regions with very low and/or a high proportion of months with zero precipitation, the SPI values should be used and interpreted with caution; the application of the SPEI might be more appropriate in such regions. Being aware of this limitation, the national expert may highlight areas where estimates based on the SPI may not produce sufficiently accurate results and may base the estimates on alternative indexes.

- Because of the natural climate variability, any observed changes or trends in the proportion of land under drought over the short baseline and reporting time frames should be interpreted with caution. Anomalies and uncertainties in the estimates should be described in the “Qualitative Assessment” field.

- The adopted timescale, based on the 12-month cycle, might not always be suitable for characterizing drought impacts in some environments where other aggregation periods, e.g., 24 months, might be more appropriate.

### 3.1.6. Summary (main actions)

Key actions for reporting drought hazard intensity values are as follows:

1. **Select precipitation dataset**: Parties may decide to use the default data or alternative national sources, provided they comply with the data specifications listed in table 18. If Parties decide to use alternative data sources, they should follow Steps 2 to 5 below:

2. **Calculate the SPI**: the SPI should be derived for all months in the full available time series; however, Parties may choose alternative indexes better suited to their local environmental conditions.

3. **Identify the drought intensity class of each grid cell**: based on the SPI calculation, the number of cells belonging to each of the SPI drought intensity classes should be counted and converted to areas by projecting the drought intensity class grids into a suitable equal area projection, and calculating the total areas under each drought intensity class in km2. Data is then reported in table SO3-1.T1.

4. **Calculate proportion of land under drought**: the proportion of land in each drought intensity class and the overall proportion of land under drought over the total land area are calculated for each reporting year and reported in tables SO3-1.T1 and SO3-1.T2.

5. **Create a gridded spatial summary for the baseline and reporting periods**: data for the entire time series from 2000 to 2019 should be summarized spatially using the gridded SPI-12 data in four-year intervals (2000–2003, 2004–2007, 2008–2011, 2012–2015 and 2016–2019) to map the most extreme conditions in each period.

6. **Verify the results**: aware of the limitations related to the adoption of the SPI for estimating drought intensity, Parties may verify the suitability of such an index to describe drought occurrence and intensity in their countries before officially submitting estimates for UNCCD reporting.

7. **Generate reports**: once verified by the Parties, the data and supporting narrative for the reporting and baseline periods should be officially submitted to the UNCCD.

### 3.1.7. Further reading

- Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3. Chapter 1. Level 1 Indicator (<https://www.unccd.int/publications/good-practice-guidance-national-reporting-unccd-strategic-objective-3-mitigate-adapt>)

## 3.2. SO 3-2 – Trends in the proportion of the total population exposed to drought

### 3.2.1. Introduction

Indicator SO 3-2 defines the exposure of the population to drought hazard (identified by indicator SO 3-1) as the total count of people exposed as well as the percentage of the total population exposed. This indicator may be further disaggregated by sex if data is available.

The method of computation uses the spatial distribution of the population or sub-population group (i.e., by sex) to establish its exposure to drought, based on the location and extent of the drought intensity classes as determined by indicator SO 3-1. Using this information, the percentage of the total population located within each drought intensity class, as well as the percentage of the total population exposed to drought (i.e., to all drought intensity classes), is calculated and reported.
National reporting is facilitated though the provision of default data.

### 3.2.2. Prerequisites for reporting

- An in-depth reading of chapter 2 of the “[Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3](https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_Strategic-Objective-3_2021.pdf): To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems” detailing the methodology used to estimate drought exposure.

- Data complying with the specifications listed in figure 2 and table 20.

- A pool of national experts officially nominated by the national authorities to verify the consistency of the results of the reporting process against the situation in the field, or to develop and implement a custom methodology to estimate indicator SO 3-2 where national data is preferred to default data. The key institution in this case is a country’s national statistical office, however universities and research centres may also provide valuable inputs.

### 3.2.3. Reporting process and step-by-step procedure

The step-by-step procedure for reporting is described in the following. If the default data is used, Steps 2 to 4 are unnecessary.

#### Step 1: Select the population dataset

Suitable data for the calculation of indicator SO 3-2 is a spatially gridded population product, or a georeferenced set of sub-national population data that covers the full extent of the country. It must represent the number of people living in each location (grid cell), ideally annually, within the baseline and reporting periods. Where possible, data should be disaggregated by sex.

There are various publicly available, fine-resolution population datasets available at the global scale and two of these, WorldPop and Gridded Population of the World, version 4 (GPWv4), are recommended by the UNCCD for deriving indicator SO 3-2. However, WorldPop is provided to country Parties by default.

Parties wishing to use in-country or regional datasets can use the decision tree in figure 2 to assess whether the in-country (or regional) population data is more appropriate to derive indicator SO 3-2 over the globally available datasets.

_Figure 2. Decision tree to help Parties choose the best population data source to derive indicator SO 3-2_
````{ifconfig} language == 'en'
```{image} /img/SO3_2_Decision_tree.jpg
```
````
````{ifconfig} language == 'ru'
```{image} /img/Figure_2-RU.jpg
```
````
````{ifconfig} language == 'ar'
```{image} /img/Figure_2-AR.jpg
```
````
````{ifconfig} language == 'zh'
```{image} /img/Figure_2-ZH.png
```
````
````{ifconfig} language == 'es'
```{image} /img/Figure_2-ES.png
```
````
````{ifconfig} language == 'fr'
```{image} /img/Figure_2-FR.png
```
````

This decision-making process should help Parties identify data that meets the specifications summarized in table 20.

{{pagebreak}}

```{tabularcolumns} |p{3cm}|p{6cm}|p{6cm}|
```

```{flat-table} *__Table 20__. Data specifications for SO 3-2 Indicator*
---
header-rows: 2
widths: 1 3 3
---
* - {rspan}`1` Item
  - {cspan}`1` Specifications
* - Default data
  - National data
* - __Input data__
    
    (Data needed to generate indicator SO 3-2, as described in Steps 2 to 4)
  - WorldPop data for the period 2000–2020, disaggregated by sex.
    
    Drought intensity class data as determined by indicator SO 3-1.
  - Gridded population products derived from national official statistics from the year 2000 to the reporting year, ideally annual and, if available, disaggregated by sex.
    
    Drought intensity class data as determined by indicator SO 3-1.
* - __Output data__
    
    (Gridded products resulting from the analysis described in Steps 2 to 4)
  - Annual gridded products of total, female and male population exposed to the four drought intensity classes from the year 2000 to the reporting year.
    
    Count and percentage of total, female and male population exposed to drought and to each drought intensity class.
    
    Gridded spatial summary in four-year epochs.
  - Annual gridded product of population exposed to the four drought intensity classes from the year 2000 to the reporting year.

    Count and percentage of total, female and male population exposed to drought and to each drought intensity class.

    Gridded spatial summary in four-year epochs.
* - __Spatial resolution__
  - Worldpop: 3-arc seconds (~100 m)
  - Assessed by national authorities based on available data.
* - __Quality__
  - Specified in the datasets’ metadata.
  - To be indicated in the dataset metadata.
* - __Metadata__
  - Metadata information is provided with default data.
  - Minimum metadata content as per the mandatory fields listed in Annex II.
```

#### Step 2:  Overlay gridded population data with indicator SO 3-1 spatial output

Indicator SO 3-2 is calculated by overlaying the population data on the hazard intensity spatial data for each year. Gap years should be filled with the closest available population data. For example, if the 2019 data is missing, it should be replaced by the 2020 data (or the closest available year), then 2020 data would be used for both 2019 and 2020. In addition to the total population, sex-disaggregated population data grids, if available, should be used in the overlay process to generate sex-disaggregated drought exposure values.

Population and drought hazard intensity data should have the same coordinate reference system and projection, which should be consistent across the reporting periods.

#### Step 3: Calculate the total population and the number and percentage of people within each drought intensity class

```{note}
Related areas in the PRAIS 4 platform: tables SO3-2.T1, SO3-2.T2 and SO3-2.T3
```

The yearly total population is obtained by adding the population residing in each land unit (e.g., grid cell) of a country area for each year within the baseline and the reporting periods (i.e., from 2000 to the reporting year).

Using the outputs of Step 2, the number of people falling within each of the four drought intensity classes, as well as the total number of people exposed to drought (i.e., to all drought intensity classes), can be estimated for each year. The respective percentages are then calculated out of the total population.

Similarly, if sex disaggregated data is used, the number of males and females that lie within each drought intensity class, as well as the total number of males and females exposed to drought, can also be calculated. The percentage share between female and male is then calculated out of the total number of people exposed to each drought intensity class and to drought overall for each year. Note that the share within each drought intensity class should equal to 100 per cent.

#### Step 4:  Create a gridded spatial summary in four-year epochs

In addition to the annual values of indicator SO 3-2, a gridded spatial summary for the entire reporting period is also produced. This gridded spatial summary output gives an indication of the number of people exposed to the most extreme drought intensity class over the four-year reporting period for each grid cell.

To summarize the reporting period spatially, the most recent population dataset from the current reporting period is overlaid on the output generated for indicator SO 3-1 in Step 5, which represents the most extreme drought intensity class for each year within the reporting period.

Similarly, baseline exposure summary spatial data products are generated for each of the four-year baseline periods (i.e., 2000–2003, 2004–2007, 2008–2011 and 2012–2015) by overlaying the most recent population data of each group of years on the output generated for indicator SO 3-1 in Step 5.

These gridded spatial summaries give an indication of the number of people exposed to the most extreme drought intensity class in four-year epochs.

#### Step 5:  Verify the results

The methodology only considers population density and distribution and does not cover ecosystem exposure to drought. A more comprehensive measure of drought exposure may take into account other physical entities at risk, such as agricultural yields, livestock counts, sectoral water and certain types of vegetation. In addition, being exposed to drought does not equate to drought vulnerability.

Parties should be aware of these limitations and critically review the results before submitting the reports to the UNCCD.

#### Step 6: Generate reports

Once verified by the Parties, the estimated population exposure to drought hazard values for the reporting and baseline periods should be officially submitted to the UNCCD. Observed changes and their interpretation may be described in the “Qualitative Assessment” field of the PRAIS 4 platform.

Default maps or maps generated in Trends.Earth using national data representing population exposed to drought for the baseline/reporting period are made available in the PRAIS 4 platform. More specifically, the following maps will be available online:

- Total population exposed to drought in first epoch of baseline period (2000–2003)
- Total population exposed to drought in second epoch of baseline period (2004–2007)
- Total population exposed to drought in third epoch of baseline period (2008–2011)
- Total population exposed to drought in fourth epoch of baseline period (2012–2015)
- Total population exposed to drought in the reporting period (2016–2019)

These maps show the most extreme drought intensity class a population was exposed to within each epoch, as explained in Step 4.

Parties are also encouraged to submit narratives on the methodology, data sources and data accuracy in the event that the estimates are derived from national data using the “General Comment” field. It would also be beneficial to report on special cases and issues, describing situations where values might be less reliable and providing the rationale to adopt a different methodology.

### 3.2.4. Dependencies

Drought exposure data relies on the SO 3-1 spatial outputs.

### 3.2.5. Challenges

#### Data availability and quality

- The WorldPop sex-disaggregated national datasets are offered as several individual rasters, each representing an age/sex class per year. This amounts to a large volume of spatial data in Geotiff format. Capacity in raster data processing and access to appropriate computing power, e.g., a cloud service, is required to store and process the data, especially for large countries. The UNCCD is developing a procedure for the bulk pre-processing of raster data, which will eventually make sex-disaggregated data available on the PRAIS 4 platform as default data. Parties will be notified when the challenge is solved and the forms pre-filled with the default data.

- Global data quality and resolution might not be sufficiently accurate for national population estimates. The integration of global and national data might improve the quality and accuracy of the results but will require additional processing capacity and technical skills.

### 3.2.6. Summary (main actions)

Key actions for reporting population exposure to drought hazard are as follows:

1. **Select the population dataset**: Parties may decide to use the default data or alternative national sources, provided they comply with the data specifications listed in table 20. If Parties decide to use alternative data sources, they should follow Steps 2 to 4 below:

2. **Overlay population data on indicator SO 3-1 spatial output**: indicator SO 3-2 is calculated by overlaying the yearly population data on yearly hazard intensity data derived from the SO 3-1 analysis.

3. **Calculate the total population as well as the number and percentage of people within each drought intensity class**: the entire population exposed to drought and the population exposed to each of the drought intensity classes are estimated and reported as a population count and percentage of the total population.

4. **Create a gridded spatial summary of indicator SO 3-2 in four-year epochs**: the gridded spatial summary for each four-year epoch provides information on the number of people exposed to the most extreme drought intensity class over each four-year epoch, from 2000 to the reporting year, at the scale of the grid cell. These four-year periods should be consistent with the gridded spatial summaries reported at SO 3-1.

5. **Verify the results**: aware of the limitations of the estimated values of drought exposure, Parties may verify the accuracy and reliability of such an indicator in their countries before officially submitting estimates for UNCCD reporting.

6. **Generate reports**: once verified by the Parties, the data and supporting narrative should be officially submitted to the UNCCD.

### 3.2.7. Further reading

- Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3. Chapter 2. Level 2 Indicator (<https://www.unccd.int/publications/good-practice-guidance-national-reporting-unccd-strategic-objective-3-mitigate-adapt>)

## 3.3. SO 3-3 – Trends in the degree of drought vulnerability

### 3.3.1. Introduction

The UNCCD approach to assessing drought vulnerability is based on a composite index, the Drought Vulnerability Index (DVI), which incorporates three components to reflect the vulnerability of the population of an individual country to drought: i) social, ii) economic and iii) infrastructural. The DVI does not, at present, address ecological or ecosystem vulnerability.

The DVI may be derived through three alternative processes, corresponding to three increasing levels of computational complexity:

- Tier 1 Vulnerability Assessment (VA) – uses at least one factor per vulnerability component, represented by country-level metrics.

- Tier 2 VA – uses more than one factor per vulnerability component, where the factors are represented by country-level metrics, with the inclusion of sex-disaggregated data (where applicable).

- Tier 3 VA – uses more than one factor per vulnerability component, where factors are represented by sub-national metrics (which may be gridded or disaggregated by administrative regions  ), with the inclusion of sex-disaggregated data (where applicable).

Parties may opt for the approach best suited to their current capacity to collect and process data, subject to data availability.

The UNCCD provides Parties with default data derived from the global DVI dataset of the European Commission Joint Research Centre (JRC) to facilitate the reporting process. This data is based on globally available datasets and should be used in the absence of more accurate data at national level.

### 3.3.2. Prerequisites for reporting

- An in-depth reading of chapter 3 of the “[Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3](https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_Strategic-Objective-3_2021.pdf): To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems” detailing the methodology used to estimate drought vulnerability.

- Data complying with the specifications listed in table 21.

- A pool of national experts officially nominated by the national authorities to verify the consistency of the results of the reporting process against the situation in the field, or to develop and implement a custom methodology to estimate indicator SO 3-3 where national data is preferred to the default data. The key institution in this case is a country’s national statistical office, however universities and research centres may also provide valuable inputs.

### 3.3.3. Reporting process and step-by-step procedure

The step-by-step procedure for reporting is described in the following and applies to both the baseline and reporting periods. If the default data is used, Steps 2 to 4 are unnecessary.

#### Step 1: Select tier of vulnerability assessment based on data availability

The vulnerability factors recommended by the UNCCD to derive the DVI (listed in figure 3) provides a snapshot of a Party’s socio-economic vulnerability to drought. The three core factors that have been recommended for the minimum Tier 1 VA – ‘Literacy rate (% of people aged 15 and above)’, ‘Proportion of population below the international poverty line’ and the ‘Proportion of population using safely managed drinking water services’ – were selected because they were identified by experts as critical to understanding vulnerability and due to their use for other reporting requirements such as SO 2 and the Sustainable Development Goals.

_Figure 3. Social, economic, and infrastructural components and their associated factors recommended for calculating the Drought Vulnerability Index_
````{ifconfig} language == 'en'
```{image} /img/SO3_3_Decision_tree.jpg
```
````
````{ifconfig} language == 'ru'
```{image} /img/Figure_3-RU.jpg
```
````
````{ifconfig} language == 'ar'
```{image} /img/Figure_3-AR.jpg
```
````
````{ifconfig} language == 'zh'
```{image} /img/Figure_3-ZH.png
```
````
````{ifconfig} language == 'es'
```{image} /img/Figure_3-ES.png
```
````
````{ifconfig} language == 'fr'
```{image} /img/Figure_3-FR.png
```
````

The UNCCD provides default data from the global DVI dataset of the JRC. The method used to derive the default DVI is similar to the one presented in this manual and in the “Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3”, but presents some key differences in terms of the normalization method (see Step 2) and number of factors included. Two additional factors are used in the default DVI: “Disaster Prevention and Preparedness (US$/Year/Capital)” and “Global map of Accessibility: Travel time to major cities”. The default DVI value represents the median DVI across the country for the period 2000–2018.

Country Parties that do not have data available to calculate the minimum Tier 1 VA can report using the default DVI data. However, it is recommended that efforts are made over successive reporting cycles to move up the tiers of VA in order to increase the sensitivity of the DVI and improve the granularity of the assessment. The decision tree in figure 4 helps Parties select the tier of VA based on data availability.

National/regional data products used to calculate the DVI should conform with the specifications listed in table 21.

_Figure 4. Decision tree to help Parties choose the best tier of vulnerability assessment for the SO 3-3 Indicator reporting according to data availability_
````{ifconfig} language == 'en'
```{image} /img/SO3_3b_Decision_tree.jpg
```
````
````{ifconfig} language == 'ru'
```{image} /img/Figure_4-RU.jpg
```
````
````{ifconfig} language == 'ar'
```{image} /img/Figure_4-AR.jpg
```
````
````{ifconfig} language == 'zh'
```{image} /img/Figure_4-ZH.png
```
````
````{ifconfig} language == 'es'
```{image} /img/Figure_4-ES.png
```
````
````{ifconfig} language == 'fr'
```{image} /img/Figure_4-FR.png
```
````

_DVI: Drought Vulnerability Index_{{br}}
_VA: Vulnerability Assessment_

{{pagebreak}}

```{tabularcolumns} |p{3cm}|p{6cm}|p{5cm}|
```

```{flat-table} *__Table 21__. Data specifications for SO 3-3 Indicator*
---
header-rows: 2
widths: 1 3 3
---
* - {rspan}`1` Item
  - {cspan}`1` Specifications
* - Default data (Drought Vulnerability Index dataset produced by the Joint Research Centre)
  - National data
* - __Input data__
    
    (Data needed to generate indicator SO 3-3 as described in Steps 2 to 4)
  - Input data used to calculate the default Drought Vulnerability Index (DVI) is drawn from various sources such as World Bank, Organisation for Economic Cooperation and Development, Food and Agriculture Organization of the United Nations, and Joint Research Centre.
  - Freely available datasets for the calculation of the factors needed to derive the DVI are listed in table 14 of the "[Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3](https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_Strategic-Objective-3_2021.pdf)".
  
    Alternatively, if available, in-country datasets with higher spatial resolution and fewer gaps over the baseline and reporting period.
* - __Output data__

    (DVI indicator resulting from the analysis described in Steps 2 to 4)
  - 2018 DVI for the baseline and the reporting period. Regions where droughts could be meaningless, such as deserts and cold areas, are masked.
  - Annual or near-annual DVI for the baseline and reporting periods.
* - __Classification__
  - Continuous, fractional scale from 0 to 1 but classification based on quantiles to group the vulnerability classes.
  - Continuous scale from 0 to 1.
* - __Spatial resolution__
  - Country level
  - National and/or sub-national levels
* - __Quality__
  - Specified in the datasets’ metadata.
  - To be indicated in the dataset metadata.
* - __Metadata__
  - Metadata information is provided with default data.
  - Minimum metadata content as per the mandatory fields listed in Annex II.
```

#### Step 2:  Factor normalization

In all tiers of VA, factors should be normalized before they can be compared and aggregated, as the vulnerability factors used are all measured using different units.

The UNCCD recommends normalizing factors using the maximum and minimum values within the country using all historic data up to, and including, the reporting period. This provides the largest range possible, ensuring that the maximum and minimum values are representative for the country.

Each time the DVI is calculated to report indicator SO 3-3, the factor range (i.e., the minimum and maximum values) should be recalculated, and if values on the reporting periods fall out outside the range, the factor should be re-normalized using the new range.

Where there is a positive correlation/relationship between vulnerability and the factor[^3]  (i.e., if the factor value increases, vulnerability also increases), the data should be normalized using the equation below:

$Factor = \frac{X_{i} - X_{min}}{X_{max} - X_{min}}$

Where:

- X{sub}`i` is the value of the considered factor in the year “i”
- X{sub}`min` is the minimum value of the considered factor observed in the entire time series
- X{sub}`max` is the maximum value of the considered factor observed in the entire time series

In case of negative correlation/relationship between vulnerability and the factor, the equation is:

$Factor = 1 - \frac{X_{i} - X_{min}}{X_{max} - X_{min}}$

After normalization, all factors have a value of between zero and one, relative to the historical maximum and minimum of the country.

Normalization of sex-disaggregated data for Tier 1 and 2 VA uses the same formulas described above, applied once for each piece of sex-related data.

For sub-national level data (Tier 3 VA), the calculation should be applied to the data from all spatial units (e.g., administrative units) combined, and the factor range should reflect the minimum and maximum values of the whole country.

For the default DVI, each factor was normalized using the global maximum and minimum values, rather than historical ranges for the given country. Normalization at the global scale means the resulting vulnerability assessment is less sensitive to the local/in-country situation than when the national range is used.

[^3]: See Table 13 of the Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3 indicating relationship of the 13 recommended factors with vulnerability

#### Step 3: Derive the Drought Vulnerability Index components

This step aims to derive aggregated values for each of the three DVI components. For Parties adopting the Tier 1 VA approach, the values of the factor normalized in Step 2 are also representative of the corresponding component. Instead, Tier 2 and Tier 3 VAs require the calculation of the arithmetic mean of the normalized factors to derive the aggregated value of each component.

The result of this step is a single value for each component and each geographic unit of the country. If sex-disaggregated data is used, separate values for male and female are produced for each component.

Parties may assign weights to the vulnerability factors if their relative importance and relevance is known. It is recommended to apply the weights to the vulnerability factors and not to the three components.

#### Step 4:  Calculate the Drought Vulnerability Index

```{note}
Related areas in the PRAIS 4 platform: table SO3-3.T1
```

In all tiers of VA, the three components (C{sub}`social`, C{sub}`economic` and C{sub}`infrastructural`) derived in the previous steps are used to produce the DVI by calculating their mean value.

$DVI = \frac{C_{social} + C_{economic} + C_{infrastructural}}{3}$

The DVI ranges from 0 to 1, with 1 being the most vulnerable.

A Tier 1 VA would result in one DVI at country-level for each reporting period. For Tier 2 and 3 VAs, where sex-disaggregated factors are used, it is recommended that sex-specific DVIs are also calculated, in addition to the country-level DVI. Hence, a Party would report at least three DVI values for each reporting period, i.e., for the total, female and male populations. For sub-national or gridded components under Tier 3 VA, the DVI is to be calculated for the smallest spatial unit separately for males, females and total populations.

#### Step 5:  Verify the results

The DVI method has not yet been validated at the local or national scale and, as such, may not accurately characterize vulnerability at these scales, either in terms of the factors most relevant to each country or the most effective factor weighting scheme. Therefore, Parties may verify the appropriateness of the default factors and add relevant ones as needed. The weighting scheme should also be thoroughly considered to improve results at national and subnational level.

Moreover, the most vulnerable populations and underrepresented groups should be involved in the determination of the factors to be used to calculate the components, in order to develop a country-specific and more effective index.

#### Step 6: Generate reports

Once verified by the Parties, the estimated vulnerability values for the reporting and baseline periods should be officially submitted to the UNCCD. Information on the method used (selected tier and factors per component) should be reported using the dedicated “Method” field in the PRAIS 4 platform. Observed changes and their interpretation may be described in the “Qualitative Assessment” table of the PRAIS 4 platform (table SO3-3.T2).

Maps generated in Trends.Earth using national data under Tier 3 VA and representing vulnerability to drought for the baseline/reporting period can be uploaded to the PRAIS 4 platform. More specifically, it is recommended to upload the following maps:

- Drought Vulnerability in the baseline period (2000–2015)
- Drought Vulnerability in the reporting period (2016–2019)

Information on data sources, data accuracy and any weighting scheme applied to the vulnerability factors can be submitted using the “General Comment” field. It would also be beneficial to report on special cases and issues, describing situations where values might be less reliable and providing the rationale to include different factors.

### 3.3.4. Dependencies

SO 2-1 and SO 2-2 can be used for the calculation of SO 3-3.

### 3.3.5. Challenges

#### Data availability and quality

- The availability of data for the considered factors varies substantially from country to country and the complete set of recommended data might not be accessible everywhere.

#### Methodological approach

- The reliability of the DVI method at national and sub-national levels is still to be verified.

- Due to the methods used for factor normalization (i.e., using in-country historic data), DVI values should not be compared between countries.

- Assuming a consistent methodology has been used over time, changes in the DVI may reflect the efficacy of drought mitigation and adaptation policies, but they may also reveal the impacts of social and economic changes disconnected from drought management measures.

### 3.3.6. Summary (main actions)

Key actions for reporting population vulnerable to drought hazard are as follows:

1. **Select tier of vulnerability assessment based on data availability**: Parties are encouraged to opt for one of the three Tiers of VA based on data availability. In the absence of data to calculate the minimum Tier 1 VA, Parties may use the default data. National/regional data products used to calculate the DVI should comply with the specifications listed in table 21. If Parties use national/regional data products, they should follow Steps 2 to 4 below:

2. **Factor normalization**: factors for each vulnerability component should be normalized before they can be compared and aggregated, as the vulnerability factors used are all measured using different units.

3. **Derive the DVI components**: the aggregated values for each of the three DVI components are calculated as the arithmetic mean of the normalized factors.

4. **Calculate the DVI**: the three components – social, economic and infrastructural – derived in the previous steps are used to produce the DVI by calculating their mean value.

5. **Verify the results**: aware of the fact that the DVI method has not yet been validated at the local or national scale, Parties may verify the appropriateness of the default factors and add relevant ones as needed before officially submitting estimates for UNCCD reporting.

6. **Generate reports**: once verified by the Parties, the data and supporting narrative for the reporting and baseline periods should be officially submitted to the UNCCD.

### 3.3.7. Further reading

- Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3. Chapter 3. Level 3 Indicator (<https://www.unccd.int/sites/default/files/documents/2021-09/UNCCD_GPG_Strategic-Objective-3_2021.pdf>).
