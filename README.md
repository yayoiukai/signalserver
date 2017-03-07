# signalserver

SignalServer is intended to become a web app to accompany [QCTools](https://github.com/bavc/qctools). Some early planning documentation is available in this [Vision doc](https://docs.google.com/document/d/1zXtVf47LVEYJvc9nPbLY-0pTDouyyNlsbeFu1YdmMlI/edit?usp=sharing).

## Installation

### Dependency - Requirement before you install Signal Server.

Signalserver can run anywhere as long as the host OS has docker-engine and docker compose are installed.

Signalsever is designed using docker in mind. So please install docker-engine and docker-compose before you start.

If you are using mac or windows, you can also install docker made for either Window or Mac. You can refer to following documentations for docker installation.

##!!! Please follow docker's documentation for these installation exactly according to your OS. !!!

Linux: https://docs.docker.com/engine/installation/

OSX: https://docs.docker.com/engine/installation/mac/#/docker-for-mac

Windows: https://docs.docker.com/engine/installation/windows/


Once you are installed docker engine, docker compose also need to be installed.
Docker-compose needs to be above version 1.7. So if you have an older version of docker-engine or
docker-compose, it probably need to be updated for both. Docker compose instruction for install is below.

https://docs.docker.com/compose/install/

Once you have docker installed and confirmed docker is running, you can install signal server.

### For Mac Users:

If you installed Docker by using Docker for Mac... there is one more step:

Create a directly where you want to mount the file volume for signalserver. (default is /file)
So create /file directly if you don't have a strong preference about it.

Also make sure you give the /file directly the full permission. It may give an error if you don't give full permission. ß

Then you click on docker icon on the top right bar and select "preferences" and select "File Sharing" tab


![screen shot 2017-02-09 at 12 49 30 am](https://cloud.githubusercontent.com/assets/720709/22776921/6bd7e742-ee66-11e6-8eb9-e5072a4bb62e.png)


In the File Shareing tab, click '+' icon and select /file (the directly you created in previous step). And /file should be added to "File Sharing"


![screen shot 2017-02-09 at 12 49 54 am](https://cloud.githubusercontent.com/assets/720709/22776939/80c84282-ee66-11e6-9f6a-6d128af6ca06.png)



Then, you need to comment out the first 4 lines of quickstart.sh or quickstartdev.sh

These four lines needs to be commented out.

```

#docker-machine create --driver virtualbox default
#docker-machine start default
#docker-machine env default
#eval "$(docker-machine env default)"

```

### Non Docker for mac users, window users

If you are using older version of mac or windows, you still need these above four lines, so please uncomment these before you run the quickstart.

Now signalserver is ready to be installed.

### Trouble Shooting

If you run this script often, or if your script got stuck and don't produce any output, you may want to remove the intermediate containers/images every once in a while.

```
docker ps -a -q | xargs docker rm -f
docker images -a -q | xargs docker rmi -f
```



### From git

```
git clone https://github.com/bavc/signalserver.git
cd signalserver
FILES_VOLUME_PATH=/files ./quickstart.sh

```




### Environment variable

Singal server has a capacity to accept large number of files. Thus, we also want to give a user to determine where the files are stored in your host OS.

For example, the host OS has 8G of the storage but you mounted extra spece in /data directly of your host OS.  And you want to designate your file storage would be in your /data directly. In this case, your file storage path is :

```
FILES_VOLUME_PATH=/data
```

You can set this value either in the .env file or you can run with ./quickstart script. Default value for this value is:

```
FILES_VOLUME_PATH=/files
```

If you don't have any special arrangement for space, you can just create the .env file with above line in the project root directly. (It is already created in this folder). In docker container, it will be stored in /var/signalserver/files directly.


### Running the application

#### First Step

When you have docker-engine and docker-compose is installed and .env file is created with above value, you just need to run below script.

```
./quickstart.sh
```

Then, it should tell you where the IP address of the web server docker container is running.

If you didn't set up the .env file, but you still want to store the files at the specific location,
you can also run the command following way.

```
FILES_VOLUME_PATH=/data ./quickstart.sh
```

### Second Step

In this point, your application is running on port of the localhost that quickstart.sh tells you.
However, you may not have frontend asset.

If it is the case, you need to open frontend.sh file and change the 1st line as below. In this example,
this person's signalserver folder is located on Users/username/signalserver/Dockerfile-frontend
So in this example, the first line of the frontend.sh is changed as as below.

```
docker build -t signalserver-frontend  -f /Users/username/signalserver/Dockerfile-frontend
```
Once you changed your frontend.sh to your project's Dockerfile-frontend path, save the file and run frontend.sh.

After you run frontend.sh, run quickstart.sh again following the first step.

And it should be it!


### API usage

#### Fileupload

Once you are running the signalserver and you create your credential at the site, you can upload the file not only from the site, but also using the API from signalserver. The curl command is as below.

```
curl -i -u "username:password" [signalserver IP]:8000/fileuploads/upload/ --upload-file [your file name]
```

Example:
You want to upload the filename '5A_born_digital_ffv1.qctools.xml.gz' to the server 192.168.99.100
and your username and password is user1 and password2

```
curl -i -u "user1:password2" 192.168.99.100:8000/fileuploads/upload/ --upload-file 5A_born_digital_ffv1.qctools.xml.gz
```

#### Check file existance

The file existance check returns true or false by given filename.

```
curl -i -u "username:password" [signalserver IP]:8000/fileuploads/check_exist/[your file name]
```
Example:
You want to check the filename '5A_born_digital_ffv1.qctools.xml.gz' exist in the server or not. The server is 192.168.99.100
and your username and password is user1 and password2

```
curl -i -u "user1:password2" 192.168.99.100:8000/fileuploads/check_exist/5A_born_digital_ffv1.qctools.xml.gz
```

#### Delete a file from the server

The delete a file by given filename.

```
curl -i -u "username:password" [signalserver IP]:8000/fileuploads/delete_file/ --data "filename=[yourfilename]"
```
Example:
You want to delete the filename '5A_born_digital_ffv1.qctools.xml.gz' from the server. The server is 192.168.99.100
and your username and password is user1 and password2

```
curl -i -u "user1:password2" 192.168.99.100:8000/fileuploads/delete_file/ --data="filename=5A_born_digital_ffv1.qctools.xml.gz"
```

#### Create a new group

The create group allow you to create a new group. The name needs to be unique.
(It will return error message if it is not.)

```
curl -u "username:password" [signalserver IP]:8000/groups/create_group -data="groupname=[your groupname]"
```
Example:
You want to create a new group named  'panda_group'. The server is 192.168.99.100
and your username and password is user1 and password2

```
curl -i -u "user1:password2" 192.168.99.100:8000/groups/create_group/ --data "groupname=panda_group"
```

#### Add a file to a group

The Add file allow you to add a file to a group. Both file and group needs to be exist in the server.
(It will return error message if one or both of them is not.)

```
curl -u "username:password" [signalserver IP]:8000/groups/add_file -data="groupname=[your groupname]&filename=[your filename]"
```
Example:
You want to add a file named 'cucumber.gocart.xml.gz' 'panda_group'. The server is 192.168.99.100
and your username and password is user1 and password2

```
curl -i -u "user1:password2" 192.168.99.100:8000/groups/add_file/ --data "groupname=panda_group&filename=cucumber.gocart.xml.gz"
```

# For Developers

Congratulations for reading this far. So you want to customize or change signal server or contribute. Great. Here is what you need to know.

## Pre-Requisite

- Be able to install Docker and can follow the basic command and have a basic understanding of what Docker is and be able to do basic system adminining.

If you have no idea what docker is, please go over some of the tutorial. (video or web)

## Docker Video Tutorial
https://www.youtube.com/watch?v=bV5vbNK3Uhw&list=PLkA60AVN3hh_6cAz8TUGtkYbJSL2bdZ4h

Also, please go over this docker compose tutorial for wordpress and please actulally do deploy for wordpress site by yourself. This project depends on docker compose. So it is good to have a basic understanding.

Welcome back. Assume you watched at least some of the tutorials and followed along the all the basics and you also deployed wordpress site. So now you know, how you deploy web application by single bash file. I hope you enjoyed your docker journey so far.

So let me explain SignalServer's architecture overall. There are roughly three components of this system. Froendend, backend, and queue system. I will list these below but they are all put together by docker and docker compose. So you don't have to do any configuration for each of the application.

- Frontend - Bower Packagemement, Node Server (Bower's dependency)
            bootstrap, d3, jquery (all frontend asessets are installed by bower)

- Backend - Django and Django RestFramework, Porgress (database)

- Queue System - Celery, Rabbit MQ, Radis

When you open the docker-compose.yml file, you see this application uses 5 docker containers to put these application together. (Also, you can easily add one more worker for your queue system by changing docker-compose.yml e.g. your CPU utilization is low with one queue.)

Lastly, I recommend to use docker with it but it is not absolute requirement. You are free to choose whatever development environtment you like. Just to make sure it works with entire system at the end of the day.

Good luck and Have fun!