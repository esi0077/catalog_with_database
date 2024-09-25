# setup ubuntu on Raspberry pi
> 1. Download the Ubuntu iso on your pc
    [Ubunto](https://ubuntu.com/download/raspberry-pi/thank-you?version=24.04.1&architecture=desktop-arm64+raspi)
> 1. Download Raspberry manager [Raspberry Manager](https://www.raspberrypi.com/software/)
> 1. install python [Download](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe)

> install ubunto on the sd card of your Raspberry pi
<img src="https://i.imgur.com/9RzFxUw.png">
-> Step 1 : click on choose device </br>
-> Step 2 : click on the Raspberry that you have </br>
-> Step 3 : click on choose Os</br>
-> Step 4 : Find "Use Custom"
<img src="https://i.imgur.com/FzshqK6.png">
-> Step 5 : Use the iso file that you downloaded </br>
-> Step 6 : click on "Choose Storage"</br>
-> Step 7 : Choose your SD card</br>
</br>
Now you have ubuntu on your sd card you just need to put your name and password on the ubunto os 

<ls>

## Setup your OS 

### now you can update your linux machine (Ubunto)

Write this commands to update your OS 
```
sudo apt-get update
sudo apt update
sudo apt upgrade
```

## lets setup MariaDB

Use this commands one by one to install MariaDB
```
sudo apt install mariadb-server
sudo mysql_secure_installation
sudo apt install mariadb-server
sudo systemctl start mariadb.service
sudo mysql_secure_installation
```

For checking if you have MariaDb you can use it with this command

```
Sudo mariadb
```

## For connecting to your PI you need to install SSH

here is how you can install SSH
```
sudo apt install openssh-server
```
# Now ou need to connect to your server

use this command to connect to your server 
```
ssh username@ip
Note : Replace username with your PI user 
```

For finding IP adress you can use this commend

```
hostname -I
```

## Use Databases and python

when you are connected to your database then you need to do the following steps 

> 1. open sql file 
> 1. open mariadb 
```
Sudo mariadb
```
> 3. write the sqls from first to last 

## Run the python code
you dont need to run the code on Raspberry pi,run the code on your local pc 
```
python telefonkatalog_oppdatert_sql.py
```

# Note Change your python
change this part in your python code with your Raspberry information
```
conn = mysql.connector.connect(
    host="10.2.2.136",
    user="test",
    password="test",
    database="telefonkatalog"
)
```



## Error Fix

if you get error that your port is not open use this commands 

```
ufw status verbose
sudo ufw allow ssh
sudo ufw allow 22/tcp
sudo ufw allow from 192.168.1.100 to any port 22
sudo ufw allow from 192.168.2.0/24 to any port 22 proto tcp
```

if you dont get your ip with hostname -I use this insted 

```
ifconfig

~~~ Or ~~~

ip address show

~~~ Or ~~~

ip a

```




if you have any other questions you can ask me by sending me mail </br>
```
   _                  _           __                    _ _ _ 
  /_\  _ __ _ __ ___ (_)_ __     /__\__ _ __ ___   __ _(_) (_)
 //_\\| '__| '_ ` _ \| | '_ \   /_\/ __| '_ ` _ \ / _` | | | |
/  _  \ |  | | | | | | | | | | //__\__ \ | | | | | (_| | | | |
\_/ \_/_|  |_| |_| |_|_|_| |_| \__/|___/_| |_| |_|\__,_|_|_|_|

                                                              
```
[Mail](mailto:armines765@gmail.com)