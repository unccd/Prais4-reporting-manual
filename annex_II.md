# Annex II: Metadata 

## 1. Introduction 

This annex details the structure of the metadata used by the Performance Review and Assessment of the Implementation System (PRAIS) 4 platform.  

Metadata is information about data, the primary instrument to provide data users with a comprehensive description of the data, including its accuracy and quality, and provides key information to appropriately use data for decision-making. Without metadata, the user is extremely limited in interpreting and understanding the data.  

Therefore, the availability of metadata increases the data’s value because it provides information on the data’s origin, its reliability and trustworthiness. Metadata is an inseparable component that makes data usable in Geographic Information System applications and other geospatial contexts. For several data exchange platforms, metadata provides the required information and structure for discovering and accessing data for different types of uses. In this context, the compliancy of metadata information with well-known standards is important in order to implement methods and tools enabling semantic searches and ensuring interoperability between systems. Accordingly, the PRAIS 4 platform metadata aims to maintain compatibility with one of the most used international metadata standards (ISO 19115, developed by the Technical Committee ISO/TC 211, Geographic information/Geomatics), which is specifically designed to describe geospatial data. 

 

## 2. Metadata structure and content 

The current version of the PRAIS 4 metadata is organized in a single form containing three types of information: 

- Data content: a description of the essential characteristics of the data and its categorization; 

- Contact point: details on the person or entity to be contacted in order to request information about the data; 

- Geographic location: expressed as coordinates of the bounding box or as a placename. 

The specific list of fields is described below. 

### Data content 

- Title: the textual label used to identify the data (data type: free text); 

- Abstract: an overview of the main characteristics of the data and a summary of the information it contains in an easily understandable manner for technical and non-technical users (data type: free text); 

- Date: the date of data creation (data type: date); 

- Topics: the formalized list of words used to describe the data (data type: list); 

- Character set encoding: the name of the character coding standard used by the data (data type: list). 

### Contact point 

- Name: the name of the person or entity authorized to provide information about the data (data type: free text); 

- Role: the function performed by the data contact point, such as the owner, distributor or custodian (data type: list); 

- Organization: the name of the responsible organization (data type: free text);  

- Email: the email address of the organization or individual (data type: free text); 

- Phone: the telephone number of the organization or individual (data type: free text); 

- Address: the physical address at which the organization or individual may be contacted (data type: free text). 

### Geographic location 

- Auto-detect bounding box: option to request the platform to derive the coordinates of a box, including the data; 

- Specify a placename: option to specify the name of the location that fully includes the data. 
