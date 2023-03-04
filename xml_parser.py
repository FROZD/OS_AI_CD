import grobid_tei_xml
import xmltodict
import os
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from grobid_client.grobid_client import GrobidClient

# constants
RESOURCE_DIRECTORY = "./resources"


# use grobid to parse pdf to xml
client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", RESOURCE_DIRECTORY, output="./xml_data",
               consolidate_citations=True, tei_coordinates=True, force=True, verbose=True)

# load xml files
documents = []
for file in os.listdir('xml_data'):
    documents.append(file)

# parse xml files
links = []
num_figures = []
for doc in documents:

    with open(f"xml_data/{doc}", mode='r') as handle:
        grob_data = grobid_tei_xml.parse_document_xml(handle.read())

    with open(f"xml_data/{doc}") as handle:
        dict_data = xmltodict.parse(handle.read())

    # get abstract and create world cloud
    abstract = grob_data.abstract
    wordcloud = WordCloud(width=1000, height=500).generate(abstract)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.title(f"{grob_data.header.title}")
    plt.axis("off")

    # get link if exists
    link = grob_data.header.url
    if link:
        links.append(link)

    # get number of figures
    figures = len(dict_data['TEI']['text']['body']['figure'])
    num_figures.append(figures)

# save links as file
with open('links.txt', mode='w') as handle:
    for link in links:
        handle.write(link)

# plot number of figures and show all figures
plt.figure()
plt.bar(range(1, len(num_figures)+1), num_figures)
plt.xlabel('paper')
plt.ylabel('number of figures')
plt.title('Number of figures in each paper')
plt.show()
