# Accessing Neo4j remotely

#### To access the neo4j

##### With default configuration Neo4j only accepts local connections.
##### To accept non-local connections, uncomment this line:
- dbms.connectors.default_listen_address=0.0.0.0

##### Bolt connector
- dbms.connector.bolt.listen_address=0.0.0.0:7687

##### HTTP Connector. There can be zero or one HTTP connectors.
- dbms.connector.http.listen_address=0.0.0.0:7474

##### HTTPS Connector. There can be zero or one HTTPS connectors.
- dbms.connector.https.listen_address=0.0.0.0:7473





