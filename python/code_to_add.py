from neo4j.v1 import GraphDatabase
uri             = "bolt://172.17.2.109:7687"

userName        = "neo4j"

password        = "PILLOWS112012;"

graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password)) 



name=['rose','jack','ron','hermonine']

for i in name:
  query="create("+i+":family{name:" '"'+i+'"' "})"
  print(query)
  with graphDB_Driver.session() as graphDB_Session:
    graphDB_Session.run(query)












    

