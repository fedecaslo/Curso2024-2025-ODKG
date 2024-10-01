# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10LWDHBJ_-F8WOoI0a6mTJfVBVrQNoHdA

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
from rdflib import FOAF, RDFS, RDF

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

q1 = prepareQuery('''
  SELECT DISTINCT ?subclass WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing.
  }
  ''',
  initNs = { "ns": NS,
           "rdfs": RDFS}
)

# Visualize the results
for r in g.query(q1):
    print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

q1 = prepareQuery('''
  SELECT DISTINCT ?person WHERE {
    { ?person a ns:Person ; }
        UNION
    { ?person a ?type .
    ?type rdfs:subClassOf ns:Person ;
    } .
  }
  ''',
  initNs = {"ns": NS ,
           "rdfs": RDFS}
)

## Could I use FILTER with || as an alternative?
## Should this query also return people who are not explicitly Person, e.g., a person that is Researcher ?

# Visualize the results

for r in g.query(q1):
    print(r)
# Visualize the results

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

# TO DO
q1 = prepareQuery('''
  SELECT DISTINCT ?individual WHERE {
    { ?individual a ns:Person } UNION { ?individual a ns:Animal } .
  }
  ''',
  initNs = {"ns": NS}
)

# Visualize the results

for r in g.query(q1):
    print(r)
# Visualize the results

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
q1 = prepareQuery('''
  SELECT DISTINCT ?person WHERE {
     ?person foaf:knows ns:RockySmith .
  }

  ''',
  initNs = {"ns": NS,
            "foaf": FOAF,
            "vcard": VCARD
           }
)
# ?person vcard:Given ?name ; this line does not work, WHY?

# Visualize the results
for r in g.query(q1):
    print(r)

print(g.serialize(format="ttl"))

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
q1 = prepareQuery('''
    SELECT DISTINCT ?animal WHERE {
        ?animal a ns:Animal .
        ?animal foaf:knows ?animal2 .
        ?animal2 a ns:Animal ;
        }

    ''',

    initNs= {"ns": NS,
            "foaf": FOAF,
            "vcard":VCARD})
# this case is the same as before, using vcard:Given returns None...
# Visualize the results
for r in g.query(q1):
    print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
q1 = prepareQuery('''
    SELECT ?age WHERE {

        {
        ?individual a ?type .
        ?type rdfs:subClassOf ns:LivingThing ;
        }
        UNION
        {
        ?individual a ns:LivingThing ;
        }.

        ?individual foaf:age ?age .
        }
    order by desc(?age)
    ''',

    initNs= {"ns": NS,
            "foaf": FOAF,
            "vcard":VCARD})

# Visualize the results
for r in g.query(q1):
    print(r.age)