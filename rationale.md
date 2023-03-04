# Solutions
This file explains how the three questions have been solved.

1. To access the abstract of each paper the *grobid_tei_xml* parser was used. The abstract is available as *.abstract* attribute. To create a worldcloud out of the abstract the *wordcloud* and *pyplot* were used.
2. In order to count the number of figures in each paper the *xmltodict* parser was used. The list of figures can be accessed by *['TEI']['text']['body']['figure']*. To get the total number the *len()* function was applied.
3. In order to get the link the *grobid_tei_xml* parser was used again. If existing the link can be accessed by *header.url* 