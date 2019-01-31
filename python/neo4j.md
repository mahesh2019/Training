# Neo4j

##### Neo4j Installation

1.First we’ll add the repository key to our keychain.
- wget --no-check-certificate -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -

2.Then add the repository to the list of apt sources.
- echo 'deb http://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list

3.Finally update the repository information and install Neo4j.
- sudo apt update
- sudo apt install neo4j

4.The server should have started automatically and should also be restarted at boot. If necessary the server can be stopped with
- sudo service neo4j stop

5.and restarted with
- sudo service neo4j start

6.You should now be able to access the database server via http://localhost:7474/browser/.

##### Neo4j Configuration

1.Go to vi /etc/neo4j/neo4j.conf in terminal, a file will be opened comment this line(dbms.directories.import=/var/lib/neo4j/import)

2.Just restart neo4j using
- sudo service neo4j restart

##### Creating nodes

1.To create a node
- CREATE (node:label),(node1:label1)

2.To see the nodes
- MATCH (n) RETURN n 

##### Creating relation

1.To create a relation
- CREATE (node1)-[:RelationshipType]->(node2) 











