# Solr Installation and working with example data

1.Install Solr in Docker
- docker pull solr

2.To run a single Solr server
- docker run --name my_solr -d -p 8983:8983 -t solr

3.To use Solr, you need to create a "core", an index for your data. For example
- docker exec -it --user=solr my_solr bin/solr create_core -c gettingstarted

4.If you want to load some of the example data that is included in the container
- docker exec -it --user=solr my_solr bin/post -c gettingstarted example/exampledocs/manufacturers.xml

In the UI, find the "Core selector" popup menu and select the "gettingstarted" core, then select the "Query" menu item. This gives you a default search for *:* which returns all docs. Hit the "Execute Query" button, and you should see a few docs with data. Congratulations!


# Sending the data to solr

1.If you want load your own data, you'll have to make it available to the container, for example by copying it into the container
- docker cp $HOME/mydata/mydata.xml my_solr:/opt/solr/mydata.xml

2.Then we need to execute the xml file in the core
- docker exec -it --user=solr my_solr bin/post -c gettingstarted mydata.xml

# Updating data

1.First step is we need to write xml or any file to update existing file
2.Then we need to add it to the same core that was used before for this file.
- docker cp $HOME/mydata/update.xml my_solr:/opt/solr/update.xml
- docker exec -it --user=solr my_solr bin/post -c gettingstarted update.xml





