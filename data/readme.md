This directory contains the data used in our project. Description for different versions of data is as follows:

Ver 1: This directory contains JSON files with triples along with Hindi wikipedia sitelink. It does not contain wikipedia article sentences.

Ver 2: This directory contains JSON files with Hindi wikipedia content in text format present in addition to version 1 data. Wikipedia content is NOT sentence tokenized.

Ver 3: The article content in previous ver 2 is sentence tokenized and stored as list of sentences along with the triple information in this version.

Ver 4: Triples are arranged in list of tuples format. For use in swayatta's task.

Ver 5: Updated triple and sentence data by performing statistical analysis and removing unsuitable data. 

-----------------

stats.csv contains number of entities, success count, failure count for preprocessing steps. 
