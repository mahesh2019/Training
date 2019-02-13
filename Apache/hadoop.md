# Hadoop Installation

#### STEP 1 – Separate Login

- sudo addgroup hadoop
- sudo adduser –ingroup hadoop hduser
- sudo adduser hduser sudo

#### STEP 2 – Getting Environment Ready
- sudo apt-get update

##### 2.1 Install JAVA
- java -version

##### 2.2 Install SSH
- sudo apt-get install ssh

Passwordless entry for localhost using SSH

- su hduser
- sudo ssh-keygen -t rsa

Note: When ask for file name or location, leave it blank.

- cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
- chmod 0600 ~/.ssh/authorized_keys

Check if ssh works,

- ssh localhost

Once we are logged in localhost, exit from this session using following command.

- exit

#### STEP 3 – Install Hadoop on Ubuntu
##### 3.1 Download Hadoop

- wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz

Unzip it

- tar xvzf hadoop-3.0.0.tar.gz

##### 3.2 Hadoop Configuration
Make a directory called hadoop and move the folder ‘hadoop-3.0.0’ to this directory

- sudo mkdir -p /usr/local/hadoop
- cd hadoop-3.0.0/
- sudo mv * /usr/local/hadoop
- sudo chown -R hduser:hadoop /usr/local/hadoop

#### STEP 4 – Setting up Configuration files
##### 4.1 ~/.bashrc
- update-alternatives –config java

Now open the ~/.bashrc file
- sudo nano ~/.bashrc

Now once the file is opened, append the following code at the end of file,

'#HADOOP VARIABLES START'

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

export HADOOP_HOME=/usr/local/hadoop

export PATH=$PATH:$HADOOP_HOME/bin

export PATH=$PATH:$HADOOP_HOME/sbin

export HADOOP_MAPRED_HOME=$HADOOP_HOME

export HADOOP_COMMON_HOME=$HADOOP_HOME

export HADOOP_HDFS_HOME=$HADOOP_HOME

export YARN_HOME=$HADOOP_HOME

export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

export HADOOP_OPTS=”-Djava.library.path=$HADOOP_HOME/lib”

'#HADOOP VARIABLES END'

Update .bashrc file to apply changes

- source ~/.bashrc

##### 4.2 hadoop-env.sh

Open the file

- sudo nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh

Now, the first variable in file will be JAVA_HOME variable, change the value of that variable to

- export JAVA_HOME=usr/lib/jvm/java-8-openjdk-amd64

##### 4.3 core-site.xml

Create temporary directory

- sudo mkdir -p /app/hadoop/tmp
- sudo chown hduser:hadoop /app/hadoop/tmp

Open the file,

- sudo nano /usr/local/hadoop/etc/hadoop/core-site.xml

Append the following between configuration tags. Same as below.

<configuration>

<property>

<name>hadoop.tmp.dir</name>

<value>/app/hadoop/tmp</value>

<description>A base for other temporary directories.</description>

</property>

<property>

<name>fs.default.name</name>

<value>hdfs://localhost:54310</value>

<description>The name of the default file system.  A URI whose scheme and authority determine the FileSystem implementation.  The uri’s scheme determines the config property (fs.SCHEME.impl) naming the FileSystem implementation class.  The uri’s authority is used to determine the host, port, etc. for a filesystem.</description>

</property>

</configuration>

##### 4.4 hdfs-site.xml
Mainly there are two directories,

Name Node
Data Node
Make directories

- sudo mkdir -p /usr/local/hadoop_store/hdfs/namenode
- sudo mkdir -p /usr/local/hadoop_store/hdfs/datanode
- sudo chown -R hduser:hadoop /usr/local/hadoop_store

Open the file,

- sudo nano /usr/local/hadoop/etc/hadoop/hdfs-site.xml

Change the content between configuration tags shown as below.

<configuration>

 <property>

  <name>dfs.replication</name>

  <value>1</value>

  <description>Default block replication.The actual number of replications can be specified when the file is created. The default is used if replication is not specified in create time.

  </description>

 </property>

 <property>

   <name>dfs.namenode.name.dir</name>

   <value>file:/usr/local/hadoop_store/hdfs/namenode</value>

 </property>

 <property>

   <name>dfs.datanode.data.dir</name>

   <value>file:/usr/local/hadoop_store/hdfs/datanode</value>

 </property>

</configuration>

##### 4.5 yarn-site.xml
Open the file,

- sudo nano /usr/local/hadoop/etc/hadoop/yarn-site.xml

Just like the other two, add the content to configuration tags.

<configuration>

   <property>

      <name>yarn.nodemanager.aux-services</name>

      <value>mapreduce_shuffle</value>

   </property>

</configuration>

#### STEP 5- Format Hadoop file system
Hadoop installation is now done. All we have to do is change format the name-nodes before using it.

- hadoop namenode -format

#### STEP 6- Start Hadoop daemons
Now that hadoop installation is complete and name-nodes are formatted, we can start hadoop by going to following directory.

- cd /usr/local/hadoop/sbin
- start-all.sh

Just check if all daemons are properly started using the following command:

- jps

#### STEP 7 – Stop Hadoop daemons
Step 7 of hadoop installation is when you need to stop Hadoop and all its modules.
- stop-all.sh

Let’s run MapReduce job on our entirely fresh Hadoop cluster setup. Go to the following directory

- cd /usr/local/hadoop

Run the following command

- hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-3.0.0.jar pi 2 5



