import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from collections import defaultdict
import pickle
import json
import dill
from tqdm import tqdm
import os

endpoint_url = "https://query.wikidata.org/sparql"

query1 = """SELECT DISTINCT ?person ?personLabel ?article WHERE {
  ?person wdt:P106 wd:Q82955;
          wdt:P31 wd:Q5.
  ?article schema:about ?person;
           schema:isPartOf <https://hi.wikipedia.org/>.
  
  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". 
  }
}"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

results1 = get_results(endpoint_url, query1)

def extract_id(id):
    start = id.find('Q')
    return id[start:]

query2 = """SELECT ?propertyLabel ?objectLabel WHERE {
  wd:%s ?predicate ?object.
  ?property wikibase:directClaim ?predicate.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

dict = defaultdict(lambda: [])
success, fail = 0, 0
fail_ids = []
  
with tqdm(results1['results']['bindings'], desc="fetching entity data", ) as pbar:
  for result1 in pbar:
    Q_id = extract_id(result1['person']['value'])
    try:
      results2 = get_results(endpoint_url, query2%Q_id)
      success += 1
    except:
      fail += 1
      fail_ids.append(Q_id)
      continue
    else:
      dict[Q_id] = {}
      dict[Q_id]['personLabel'] = result1['personLabel']['value']
      dict[Q_id]['Hindi sitelink'] = result1['article']['value']
      dict[Q_id]['triples'] = [{'propertyLabel': result2['propertyLabel']['value'], 'objectLabel': result2['objectLabel']['value']} for result2 in results2['results']['bindings']]
    finally:
      pbar.set_description_str("success: %d, fail: %d" % (success, fail))
      
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'politicians.json'), 'w') as outfile:
    json.dump(dict, outfile)
