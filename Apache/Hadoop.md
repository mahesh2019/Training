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





