import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from collections import defaultdict
import pickle
import json
import dill

endpoint_url = "https://query.wikidata.org/sparql"

query = """SELECT DISTINCT ?person ?personLabel ?article WHERE {
  ?person wdt:P641 wd:Q5375;
          wdt:P31 wd:Q5.
  ?article schema:about ?person;
           schema:isPartOf <https://hi.wikipedia.org/>.
  
  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "hi". 
  }
}"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

results = get_results(endpoint_url, query)

def extract_id(id):
    start = id.find('Q')
    return id[start:]

ids = []
for result in results['results']['bindings']:
    ids.append((extract_id(result['person']['value']), result['personLabel']['value']))

query = """SELECT ?propertyLabel ?objectLabel WHERE {
  wd:%s ?predicate ?object.
  ?property wikibase:directClaim ?predicate.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""
dict = defaultdict(lambda: [])
for id in ids:
    results = get_results(endpoint_url, query%id[0])
    dict[id[0]] = {}
    dict[id[0]]['personLabel'] = id[1]
    dict[id[0]]['triples'] = [{'propertyLabel': result['propertyLabel']['value'], 'objectLabel': result['objectLabel']['value']} for result in results['results']['bindings']]

with open('cricketers.json', 'w') as outfile:
    json.dump(dict, outfile)



