# Drill

#### Apache Drill Installation

1.In a terminal window, change to the directory where you want to install Drill.

2.Download the latest version of Apache Drill here or from the Apache Drill mirror site with the command appropriate for your system:

- wget http://apache.mirrors.hoobly.com/drill/drill-1.15.0/apache-drill-1.15.0.tar.gz
- curl -o apache-drill-1.15.0.tar.gz http://www.apache.org/dyn/closer.cgi/drill/drill-1.15.0/apache-drill-1.15.0.tar.gz

3.Copy the downloaded file to the directory where you want to install Drill.

4.Extract the contents of the Drill .tar.gz file. Use sudo only if necessary:

- tar -xvzf <.tar.gz file name>

#### Start Apache Drill

1.Navigate to the Drill installation directory.

2.Issue the following command to start the Drill shell:

-bin/drill-embedded

The 0: jdbc:drill:zk=local> prompt appears.

#### Stop Drill

Issue the following command when you want to exit the Drill shell:

- !quit



