# Elasticsearch Installation

#### Step 1 — Downloading and Installing Elasticsearch
First, update your package index.

- sudo apt-get update

Download the latest Elasticsearch version, which is 2.3.1 at the time of writing.

- wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.3.1/elasticsearch-2.3.1.deb

Then install it in the usual Ubuntu way with dpkg.

- sudo dpkg -i elasticsearch-2.3.1.deb

To make sure Elasticsearch starts and stops automatically with the server, add its init script to the default runlevels.

- sudo systemctl enable elasticsearch.service

#### Step 2 — Configuring Elasticsearch
To start editing the main elasticsearch.yml configuration file with nano or your favorite text editor.

- sudo nano /etc/elasticsearch/elasticsearch.yml

Change following names

- cluster.name: mycluster1
- node.name: "My First Node"

#### Step 3 — Testing Elasticsearch

By now, Elasticsearch should be running on port 9200. You can test it with curl, the command line client-side URL transfers tool and a simple GET request.

- curl -X GET 'http://localhost:9200'

we will get output like this

{
  "name" : "My First Node",
  "cluster_name" : "mycluster1",
  "version" : {
    "number" : "2.3.1",
    "build_hash" : "bd980929010aef404e7cb0843e61d0665269fc39",
    "build_timestamp" : "2016-04-04T12:25:05Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.0"
  },
  "tagline" : "You Know, for Search"
}





