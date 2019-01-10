# Solr

1.Install Solr in Docker
- docker pull solr

2.To run a single Solr server
- docker run --name my_solr -d -p 8983:8983 -t solr

3.To use Solr, you need to create a "core", an index for your data. For example
- docker exec -it --user=solr my_solr bin/solr create_core -c gettingstarted

4.If you want to load some of the example data that is included in the container
- docker exec -it --user=solr my_solr bin/post -c gettingstarted example/exampledocs/manufacturers.xml

In the UI, find the "Core selector" popup menu and select the "gettingstarted" core, then select the "Query" menu item. This gives you a default search for *:* which returns all docs. Hit the "Execute Query" button, and you should see a few docs with data. Congratulations!

