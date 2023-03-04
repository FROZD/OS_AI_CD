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
`pip install requirements.txt`


3. Provide your pdfs and run
- Move your pdf to the [resources](resources) directory OR choose your own directory by changing the *RESOURCE_DIRECTORY* constant in [xml_parser.py](xml_parser.py)
- Start the application by running `python xml_parser.py`