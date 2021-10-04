# 3. Strategic objective 3: To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems

## 3.1. SO 3-1 – Trends in the proportion of land under drought over the total land area 

### 3.1.1. Introduction

Drought is defined as a period of dry weather long enough to cause a serious hydrological imbalance (World Meteorological Organization (WMO), 1992). The United Nations Convention to Combat Desertification (UNCCD) defines drought as the naturally occurring phenomenon that exists when precipitation has been significantly below normal recorded levels, causing serious hydrological imbalances that adversely affect land resource production systems[^1].

[^1]: "UNCCD. 1994. Article 1 of the Convention Text: http://www2.unccd.int/sites/default/files/relevant-links/2017-01/UNCCD_Convention_ENG_0.pdf "

There are several drought indices that might be used to estimate national drought hazard. The UNCCD methodology to estimate indicator SO 3-1 recommends using a globally accepted drought index, the Standardized Precipitation Index (SPI), to characterize the meteorological drought hazard. However, Parties may report using other indices if already in use at national level. For example, the Standardized Precipitation Evapotranspiration Index (SPEI) may represent an alternative index, readily comparable to the SPI, that provides more reliable signals of drought in arid areas. Parties using the SPEI can apply the same methods recommended in this manual and in the “Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3” to report indicator SO 3-1. For other indices currently in use, Parties may need to ensure statistical consistency with the SPI drought intensity classes described in table 19[^2]. 

[^2]: "The Global Drought Classification System (GDCS, formerly the Global Drought Indicator or GDI), currently under development by WMO through the Global Multi-Hazard Alert System (GMAS) framework, will provide methods on how a multitude of drought indices can be translated onto a harmonized legend of drought classes.
Indicator SO 3-1 specifically describes the status of meteorological drought hazards that occurred during the baseline and reporting periods within a country."

The overall objective is for Parties to assess drought hazard and identify areas exposed to extreme drought in order to prioritize mitigation efforts in conjunction with assessments of drought exposure (SO 3-2) and vulnerability (SO 3-3). National reporting is facilitated though the provision of default data.

### 3.1.2. Prerequisites for reporting

- An in-depth reading of chapter 1 of the [“Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3: To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems”](https://www.unccd.int/publications/good-practice-guidance-national-reporting-unccd-strategic-objective-3-mitigate-adapt) detailing the methodology used to estimate drought hazards and the changes over time.

- Data complying with the specifications listed in figure 1 and table 18.

- A pool of national experts officially nominated by the national authorities to verify the consistency of the results of the reporting process with the situation in the field, or to develop and implement a custom methodology to estimate indicator SO 3-1 where national data are preferred to the default data. Key institutions might include a country’s national meteorological and hydrological service (NMHS), ministry of environment, ministry of agriculture, remote sensing centre and national statistical office, as well as relevant universities and research centres.

### 3.1.3. Reporting process and step-by-step procedure

The step-by-step procedure for reporting is described in the following. If the default data is used, steps 2 to 5 are unnecessary.

_Step 1: Select precipitation dataset_

The UNCCD provides default data from the Global Precipitation Climatology Centre (GPCC) Monitoring Product, a gridded precipitation product derived from rain gauge data. Parties have the option to use an alternative default dataset in Trends.Earth: the Climate Hazards Group InfraRed Precipitation with Stations (CHIRPS), which produces high-resolution estimates based on satellite observations and gauged station data. While the higher spatial resolution of CHIRPS and slightly longer recording period are advantageous when deriving the SPI, it has a ‘quasi-global’ coverage that spans 50°S to 50°N. Therefore, Parties with country boundaries exceeding this range will not be able to use the CHRIPS dataset. In contrast, the GPCC precipitation data has global coverage. 

Parties wishing to use in-country data provided by the NMHS or regional, rather than global, precipitation products can use the decision tree in figure 1 to assess whether the in-country (or regional) precipitation data is more appropriate to derive indicator SO 3-1 over the globally available datasets. 

_Figure 1. Decision tree to help Parties chose the best precipitation data source to derive indicator SO 3-1_

![](/img/SO3_Decision_tree.jpg "GPCC: Global Precipitation Climatology Centre
SPI: Standardized Precipitation Index
CHIRPS: Climate Hazards Group InfraRed Precipitation with Stations
")

This decision-making process should help Parties identify data that meets the specifications summarized in table 18.

_Table 18. Data Specifications for SO 3-1 indicator_

**Table**

_* As stated in Step 3, the December SPI-12 values represent the precipitation deficits (or excesses) over the Gregorian (January–December) calendar year._

_Step 2:  Calculate the Standardized Precipitation Index_

Monthly time series of the SPI are based on the selected gridded precipitation data and calculated using the SPI-12 method, which provides an annual summary of precipitation deficits for each month using a 12-month accumulation method. For example, the 12-month precipitation accumulation for April 2019 is the total monthly precipitation for May 2018 to April 2019. 

In order to normalize the 12-month precipitation accumulation data distributions, the WMO climatological standard normal period of 1981–2010 is used as a reference period. The normalization method is based on a Gamma probability distribution function fitted to the 12-month precipitation accumulations in this reference period. Thus calculated, these probability distribution parameters are then applied to any time series of monthly 12-month precipitation accumulations to produce the normalized monthly SPI-12 time series for each grid cell for the entire recording period. However, a change in the standard climate normal period necessitates a recalculation of the SPI for the baseline and all historic reporting periods. As such, it is recommended that the reference period used to calculate the SPI be clearly stated in national reports of indicator SO 3-1 to the UNCCD.

Default SPI data is available in Trends.Earth for the purposes of SO3 monitoring. However, there are various open access tools that can be used to derive the SPI, a selection of which is listed in table 3 of the Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3.

_Step 3: Identify the drought intensity class of each grid cell based on the calculated Standardized Precipitation Index value_

**Table**

To assess the SPI time series for the baseline and reporting periods, the December SPI-12 values for each year should be extracted. The December SPI-12 values represent the precipitation deficits (or excesses) over the Gregorian (January–December) calendar year. 

For each of the December SPI-12 grids, the number of cells belonging to each of the SPI drought intensity classes listed in table 19 should be counted. Positive SPI values are discarded, since they indicate that there was no drought in the given period.

_Table 19.  Standardized Precipitation Index (SPI) drought intensity classes_

**Table**

The total area under each drought intensity class should be derived in a two-step process:

(i)	Project the drought intensity class grid into a suitable equal area projection (e.g., Mollweide) to obtain the cells’ area in km2.

(ii)	Combine all cells’ area in a given drought class to get the total area under each drought intensity class.

_Step 4:  Calculate proportion of land under drought_

**Table**

The proportion of land in each drought intensity class is calculated for each reporting year as a percentage of the total land area. 
For each of the SPI-12 grids in the baseline and reporting period, the number of cells falling under each of the SPI drought intensity classes is counted (cellCount). Then, for each reporting year, the percentage of the total land area in each drought intensity class is calculated. The formula is as follows: 
%cellCountij = (cellCountij / Total number of cells) × 100

Where:

“cellCount” is the number of pixels under a drought intensity class in one year
“%cellCount” is the proportion of land under the related drought intensity class
“i” is the drought intensity class
“j” is the reporting year
“Total number of cells’” is all the grid cells within the country Party’s land area.

The total area falling under each of the drought intensity classes in each year is calculated by multiplying cellCount by the area of the cells (a constant value, since the drought intensity class grid was previously converted to an equal-area projection).

_Step 5:  Create a gridded spatial summary for the baseline and reporting periods_

In addition to the tabular reports described above, indicator SO 1-3 should also be summarized spatially to map the most extreme conditions that occurred in the baseline and reporting periods.

To summarize the reporting period spatially, the most extreme drought intensity class should be identified for each grid cell for each reporting year within the reporting period.

Data for the baseline period should be summarized spatially using the gridded SPI-12 data in four-year intervals (2000–2003, 2004–2007, 2008–2011 and 2012–2015), reflecting the reporting periods used for SO3 monitoring. In this case, the most extreme drought intensity class should be reported for each grid cell for each four-year period within the baseline.

_Step 6: Verify the results_

Parties should be aware of the limitations related to the use of SPI as a single drought indicator and critically review the default data vis-à-vis the national rain gauge data and other meteorological sources before submitting the reports to the UNCCD.
 
_Step 7: Generate reports_

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

_Data availability and quality_

- Internationally available precipitation data might not be sufficiently accurate to estimate the intensity of drought hazard at national level. The use of national data is recommended because it is assumed to be more precise and reliable. However, national precipitation data might not be readily available in digital form and/or might be affected by gaps in the time series.

_Limitations of the SPI-based estimates_

- While the SPI is recommended as a well-established, flexible and robust drought index to quantify drought hazard on a global scale, it only quantifies the meteorological deficits, since it is solely based on precipitation, and other types of drought (e.g., hydrological, agricultural) may not be well captured. Moreover, in regions with very low and/or a high proportion of months with zero precipitation, the SPI values should be used and interpreted with caution; the application of the SPEI might be more appropriate in such regions. Being aware of this limitation, the national expert may highlight areas where estimates based on the SPI may not produce sufficiently accurate results and may base the estimates on alternative indexes.

- Because of the natural climate variability, any observed changes or trends in the proportion of land under drought over the short baseline and reporting time frames should be interpreted with caution. Anomalies and uncertainties in the estimates should be described in the “Qualitative Assessment” field.

- The adopted timescale, based on the 12-month cycle, might not always be suitable for characterizing drought impacts in some environments where other aggregation periods, e.g., 24 months, might be more appropriate.

### 3.1.6. Summary (main actions)

Key actions for reporting drought hazard intensity values are as follows:

1.**Select precipitation dataset**: Parties may decide to use the default data or alternative national sources, provided they comply with the data specifications listed in table 18. If Parties decide to use alternative data sources, they should follow Steps 2 to 5 below:

2.	**Calculate the SPI**: the SPI should be derived for all months in the full available time series; however, Parties may choose alternative indexes better suited to their local environmental conditions.

3.	**Identify the drought intensity class of each grid cell**: based on the SPI calculation, the number of cells belonging to each of the SPI drought intensity classes should be counted and converted to areas by projecting the drought intensity class grids into a suitable equal area projection, and calculating the total areas under each drought intensity class in km2. Data is then reported in table SO3-1.T1.

4.	**Calculate proportion of land under drought**: the proportion of land in each drought intensity class and the overall proportion of land under drought over the total land area are calculated for each reporting year and reported in tables SO3-1.T1 and SO3-1.T2.

5.	**Create a gridded spatial summary for the baseline and reporting periods**: data for the entire time series from 2000 to 2019 should be summarized spatially using the gridded SPI-12 data in four-year intervals (2000–2003, 2004–2007, 2008–2011, 2012–2015 and 2016–2019) to map the most extreme conditions in each period.

6.	**Verify the results**: aware of the limitations related to the adoption of the SPI for estimating drought intensity, Parties may verify the suitability of such an index to describe drought occurrence and intensity in their countries before officially submitting estimates for UNCCD reporting.

7.	**Generate reports**: once verified by the Parties, the data and supporting narrative for the reporting and baseline periods should be officially submitted to the UNCCD.

### 3.1.7. Further reading

- Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3. Chapter 1. Level 1 Indicator (https://www.unccd.int/publications/good-practice-guidance-national-reporting-unccd-strategic-objective-3-mitigate-adapt) 

## 3.2. SO 3-2 – Trends in the proportion of the total population exposed to drought

### 3.2.1. Introduction

Indicator SO 3-2 defines the exposure of the population to drought hazard (identified by indicator SO 3-1) as the total count of people exposed as well as the percentage of the total population exposed. This indicator may be further disaggregated by sex if data is available. 

The method of computation uses the spatial distribution of the population or sub-population group (i.e., by sex) to establish its exposure to drought, based on the location and extent of the drought intensity classes as determined by indicator SO 3-1. Using this information, the percentage of the total population located within each drought intensity class, as well as the percentage of the total population exposed to drought (i.e., to all drought intensity classes), is calculated and reported.
National reporting is facilitated though the provision of default data.

### 3.2.2. Prerequisites for reporting

- An in-depth reading of chapter 2 of the “Good Practice Guidance for National Reporting on UNCCD Strategic Objective 3: To mitigate, adapt to, and manage the effects of drought in order to enhance resilience of vulnerable populations and ecosystems” detailing the methodology used to estimate drought exposure.

- Data complying with the specifications listed in figure 2 and table 20.

- A pool of national experts officially nominated by the national authorities to verify the consistency of the results of the reporting process against the situation in the field, or to develop and implement a custom methodology to estimate indicator SO 3-2 where national data is preferred to default data. The key institution in this case is a country’s national statistical office, however universities and research centres may also provide valuable inputs.

### 3.2.3. Reporting process and step-by-step procedure

The step-by-step procedure for reporting is described in the following. If the default data is used, Steps 2 to 4 are unnecessary.

_Step 1: Select the population dataset_

Suitable data for the calculation of indicator SO 3-2 is a spatially gridded population product, or a georeferenced set of sub-national population data that covers the full extent of the country. It must represent the number of people living in each location (grid cell), ideally annually, within the baseline and reporting periods. Where possible, data should be disaggregated by sex.

There are various publicly available, fine-resolution population datasets available at the global scale and two of these, WorldPop and Gridded Population of the World, version 4 (GPWv4), are recommended by the UNCCD for deriving indicator SO 3-2. However, WorldPop is provided to country Parties by default.  

Parties wishing to use in-country or regional datasets can use the decision tree in figure 2 to assess whether the in-country (or regional) population data is more appropriate to derive indicator SO 3-2 over the globally available datasets.  

_Figure 2. Decision tree to help Parties choose the best population data source to derive indicator SO 3-2_

