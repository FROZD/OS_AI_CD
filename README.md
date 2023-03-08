# Example pdf parser application using GROBID
[![DOI](https://zenodo.org/badge/604130539.svg)](https://zenodo.org/badge/latestdoi/604130539)  
This project has been developed within the  Open Science and Artificial Intelligence in Research Software Engineering class.  
This framework shows the power of the pdf parser grobid in combination with different xml parser by showing result for the following questions for scientific papers provided by the user.
1. Keywordcloud of the abstract
2. Number of figures
3. List of links

##How to start
1. Make sure you have [GROBID](https://grobid.readthedocs.io/en/latest/) installed and running
- For example by using docker. Run:  
`docker pull lfoppiano/grobid:0.7.2`  
to install and  
`docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2`  
to start GROBID
- For further information see the [documentation](https://grobid.readthedocs.io/en/latest/)

2. Set up your environment
- By running 
`conda create --name <env> --file requirements.txt`

3. Provide your pdfs and run
- Move your pdf to the [resources](resources) directory OR choose your own directory by changing the *RESOURCE_DIRECTORY* constant in [xml_parser.py](xml_parser.py)
- Start the application by running `python xml_parser.py`

## XML Mode
If you want parse existing xml files. Set the MODE constant in [xml_parser.py](xml_parser.py) to *"XML"* provide your xml files in a directory and assign your directory to the *XML_RESSOURCE_DIRECTORY* constant in [xml_parser.py](xml_parser.py)
- Now just start the feature extraction for xml files by running `python xml_parser.py`

## Documentation
See full documentation at https://os-ai-cd.readthedocs.io/en/latest/