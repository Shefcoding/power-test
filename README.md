# *** Final Assignment: CD Report***

## *** Main components used ***
The main components I used in this exercise were Github Actions, SSH Keys and configuration my flask app with Gunicorn.

### **Github Actions** 
One of the main components of the solution was GitHub Actions, which is a tool for automating and streamlining workflows.  In this case, GitHub Actions was used to automatically deploy the app to the remote server whenever code was pushed to the repository. The following steps were taken. First off, a job is triggered if a push to repo is executed. The job then performs certain tests to check the new code. Once the tests succeeded, it logged into my digital ocean vps and pulled the newest version from github and restarted the application

### **SSH Keys** 
Another important component was the use of SSH keys, which are a secure way to authenticate with a remote server. They allow for the creation of a secure connection between a local machine and a remote server, without the need for a password. This was necessary for connecting to the remote server to github and pulling the code to the server.

### **Guniorn**
The final component was the configuration of the app with Gunicorn, which is a Python web server that can be used to run the app. This involved installing Gunicorn and configuring it to run the app, as well as setting up a reverse proxy to redirect incoming requests to the correct port.

### ***Problems***
One of the problems I encountered was using the secrets to connect to the remote server. I first had to figure out if the secrets I uploaded to Github were my github account or remote server credentials. The next step was figuring out the exact username and host to connect to, which I was able to do with a Google search. It turns out that Digital Ocean has a default user "root" that I was able to use. 

Another problem was initially pulling the program from GitHub. I had initially tried to use a git pull command, but this didn't work because the directory was not a Git repository. I had to use git clone instead to properly download the code from the repository.

The final problem I encountered was using my GitHub SSH key to pull the program automatically in my YAML script. I followed the instructions and created a Github SSH key, created a SSH key on my remote server as well but I kept getting the message: 
``` 
-err: fatal: could not read Username for 'https://github.com': No such device or address
-git@github.com: Permission denied (publickey).
``` 
It seemed that I couldn't get connection with github through my remote server. 
I eventually had to use a different method with github deploy keys, which allows for the creation of a separate SSH key specifically for a single repository. This allowed me to properly authenticate with the remote server and access the code. 
After solving this issue, the server needed to start automatically as well. I had to make a new .service file in the directory: `/etc/systemd/system` and change my default file at `/etc/nginx/sites-available`. 
