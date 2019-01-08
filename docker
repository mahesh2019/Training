# Docker
# Installing the Docker using Repository:
1.Update the apt package index:
- sudo apt-get update

2.Install packages to allow apt to use a repository over HTTPS:
- sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

3.Add Docker’s official GPG key:
- $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.
- sudo apt-key fingerprint 0EBFCD88
pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22

4.Use the following command to set up the stable repository. You always need the stable repository, even if you want to install builds from the edge or test repositories as well. To add the edge or test repository, add the word edge or test (or both) after the word stable in the commands below.
- sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# INSTALL DOCKER CE

1.Update the apt package index.
- sudo apt-get update

2.Install the latest version of Docker CE, or go to the next step to install a specific version:
- sudo apt-get install docker-ce

3.Verify that Docker CE is installed correctly by running the hello-world image.
- sudo docker container run hello-world

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

