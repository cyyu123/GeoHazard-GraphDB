# Supplementary Technical Documentation

## Georgia EPD Hazardous Waste Site to Chemical Relation Neo4j Database Hosting

**Author:** Ken Nakatsu  
**Date of Supplementary Documentation:** January 2024

### Introduction

This supplementary documentation aims to provide an in-depth understanding of the technologies and methodologies employed in the development of the Georgia EPD Hazardous Waste Site to Chemical Relation Neo4j Database Hosting. This project leverages a graph database to represent and query complex relationships between hazardous waste sites and chemicals in Georgia, USA.

### Technologies and Methodologies

#### 1. Python Shiny App

- **Overview and History:** Python is a high-level, interpreted programming language known for its readability and versatility. It was created in the late 1980s by Guido van Rossum and has since become one of the most popular programming languages, especially for data science and web applications.
- **Use Case in Project:** In this project, Python is used to develop a Shiny application. Shiny, originally a package for R, enables the creation of interactive web applications directly from R (or in this case, Python). The app provides a user-friendly interface for querying the database without needing to know the Cypher query language.

#### 2. Data Processing and Graph Creation

- **Graph Database (Neo4j):**
  - **History:** Neo4j is a graph database management system developed by Neo4j, Inc. Described as an ACID-compliant transactional database with native graph storage and processing, Neo4j is widely recognized for its performance in connected data operations.
  - **Use Case in Project:** Neo4j is used for creating, hosting, and managing the graph database. It allows for efficient representation and querying of complex relationships between various environmental data points, such as hazardous sites and chemicals.

#### 3. Cypher Query Language

- **Overview and History:** Cypher is a declarative graph query language that allows for expressive and efficient querying and updating of a graph database. It was developed by Neo4j for its graph database and is designed to be intuitive and easy to learn.
- **Use Case in Project:** Cypher is used for querying the Neo4j database. It allows users to retrieve complex relational data, like finding all sites with a specific chemical attribute or establishing new relationships between nodes.

#### 4. Data Sources

- **EPD Hazardous Site Inventory, TOXRIC Database, and HSDB from Pubchem:** These sources provide comprehensive data on hazardous sites, chemical properties, and their environmental and health effects. Integrating these diverse data sets into a single graph database enables complex analyses that would be challenging with traditional relational databases.

### Accessing and Updating the Database and Setting Up the Environment

This information can be found in the original Readme. Please consult that file for further information in regards to setting up the environment. The graph dump can be obtained from Ken Nakatsu (knakats@emory.edu)

Based on the requirements, here is the markdown file:

## Literature Review on Computational Methods and Chemical Hazard Prediction

### Methods for Predicting Chemical Half Life

The team will explore some of these methods. Access to high performance computing can be accomodated if needed. Models here utilize extracted data to generate predictions. 

#### Evidence
- Quantum Structure-Property Relationship (QSPR) models can predict photolysis half-lives of polycyclic aromatic hydrocarbons (PAHs) under sunlight based on quantum chemical descriptors. They use regression models based on quantum descriptors. [(Chen et al., 2001)](https://pubmed.ncbi.nlm.nih.gov/11444002/).
- A rapid screening method for chemical persistence in the environment uses physical-chemical equilibrium partitioning information [(Gouin et al., 2000)](https://pubs.acs.org/doi/epdf/10.1021/es991011z).

### Obtaining Structures from Chemical Formulas

#### Evidence
- Algorithms like OMG (Open Molecule Generator) produce non-isomorphic chemical structures matching elemental compositions and prescribed substructures [(Peironcely et al., 2012)](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-4-21).

### Predicting Hazardous Chemicals for Human Health

#### Evidence
- The ExpoCast project uses high-throughput models for exposure-based chemical prioritization, predicting human exposure potential and identifying hazards [(Wambaugh et al., 2013)](https://pubs.acs.org/doi/10.1021/es400482g).
- PTDMs (Predictive Toxicogenomics-Derived Models) integrate networks of chemical-gene interactions, chemical-disease associations, and gene-disease associations to infer chemical hazard profiles [(Cheng et al., 2013)](https://pubs.rsc.org/en/content/articlelanding/2013/mb/c3mb25309k).
- The ToxCast program uses computational chemistry, high-throughput screening, and toxicogenomic technologies to predict potential toxicity and prioritize testing of environmental chemicals [(Dix et al., 2007)](https://pubmed.ncbi.nlm.nih.gov/16963515/).

### Databases with Established Half-Lives of Chemicals
   - The EPI Suite software, particularly its BIOWIN models, is used for predicting environmental persistence, including half-lives, of chemicals [(Aronson et al., 2006)](https://pubmed.ncbi.nlm.nih.gov/16297427/).

   Based on this source, it appears that we can use this software,  [EPI Suite](https://www.epa.gov/tsca-screening-tools/epi-suitetm-estimation-program-interface) from the EPA to predict information about chemicals including half life. 

### Predicting More Information about Chemicals Relevant to People

1. **Publicly Available QSPR Models for Environmental Media Persistence**: These models use fragment descriptors and machine-learning methods to predict the persistency of chemicals in water, soil, and sediment, which is key in persistent, bioaccumulative and toxic (PBT) assessments [(Lunghini et al., 2020)](https://pubmed.ncbi.nlm.nih.gov/32588650/). (Review)

2. **Integrated In Silico Strategy for Assessment and Prioritization of Persistence under REACH**: This strategy combines multiple models, structural alerts, and chemical classes to predict persistence and prioritize substances for regulatory purposes [(Pizzo et al., 2016)](https://pubmed.ncbi.nlm.nih.gov/26773396/). (They collect datasets here which could be helpful for our purposes)

3. **DeepTox: Toxicity Prediction using Deep Learning**: DeepTox pipeline applies Deep Learning for toxicity prediction, including environmental persistence, by constructing a hierarchy of chemical features [(Mayr et al., 2016)](https://www.frontiersin.org/articles/10.3389/fenvs.2015.00080/full). (Computational method that we can use, or can we use the training/test data from 2014) [(Link)](https://paperswithcode.com/dataset/tox21-1)

4. **Predicting Persistence in Sediment Compartment Using k-NN Algorithm**: This program uses the k-Nearest Neighbor (k-NN) algorithm for identifying persistence in the sediment compartment based on half-life data [(Manganaro et al., 2016)](https://www.sciencedirect.com/science/article/abs/pii/S0045653515302484).

5. **Screening and Ranking of POPs for Global Half-Life**: This study uses QSAR approaches to rank chemicals according to their global half-life index, aiding in the identification of persistent organic pollutants [(Gramatica & Papa, 2007)](https://pubs.acs.org/doi/10.1021/es061773b).

## OCR Application and How we Need to Improve It
### Utilizing Python's PDFMiner and PyTesseract for Document Parsing and OCR

In the Georgia EPD Hazardous Waste Site to Chemical Relation Neo4j Database Hosting project, we employ Python's PDFMiner and PyTesseract packages to automate the parsing of documents and Optical Character Recognition (OCR). This combination allows for efficient extraction of text and symbols from PDF documents, particularly useful in processing environmental reports, research papers, and other relevant documents which include unstructured data.

#### 1. PDFMiner: PDF Text Extraction

- **Overview:** PDFMiner is a tool for extracting information from PDF documents. Unlike other PDF-related tools, it focuses entirely on getting and analyzing text data. PDFMiner allows for obtaining the exact location of texts in a page, as well as other information such as fonts or lines. It includes a PDF parser, a PDF renderer, a PDF converter, and more.

**Example Command:**

```python
from pdfminer.high_level import extract_text

text = extract_text('document.pdf')
print(text)
```

This command extracts all the text from 'document.pdf' and prints it. This can be further processed to isolate specific data like chemical names.

#### 2. PyTesseract: OCR Implementation

- **Overview:** PyTesseract is an OCR tool for Python. It will recognize and “read” the text embedded in images. Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine.
- **Use in Project:** We use PyTesseract in combination with PDFMiner for cases where the text is not selectable (such as scanned documents). The current focus with PyTesseract is on detecting simpler elements like checkmarks, which indicate the presence of certain chemicals or attributes. We use the percentage of the box that has black pixels to predict the presence of a checkmark. 

**Example Command:**

```python
from PIL import Image
import pytesseract

image = Image.open('scanned_document.jpg')
text = pytesseract.image_to_string(image)
print(text)
```

This command converts the text from an image file 'scanned_document.jpg' into a string. For our purpose, we can process this string to find checkmarks or other simpler symbols.

#### 3. Combining PDFMiner and PyTesseract

- **Workflow:** First, use PDFMiner to extract text where possible. When encountering images or scanned documents where text extraction is not feasible, employ PyTesseract to perform OCR.
- **Specific Use Case:** For chemical names, rely primarily on PDFMiner for accuracy. Use PyTesseract to detect checkmarks or other simple symbols in the document. Once a checkmark is detected indicating the presence of a chemical, refer back to the corresponding section extracted by PDFMiner for the accurate chemical name.

#### 4. Addressing the Weakness in OCR for Chemical Names (This is a goal of the project)

- **Current Limitation:** The challenge in using OCR for chemical names lies in its tendency to inaccurately recognize complex scientific terms and symbols.
- **Solution:** By using OCR to only detect checkmarks and then cross-referencing with the accurate text extracted by PDFMiner, we maintain data integrity and ensure accurate chemical name identification.