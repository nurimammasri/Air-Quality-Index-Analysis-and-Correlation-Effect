## **Deploy Streamlit**

To deploy an app, click "New app" from the upper right corner of your workspace, then fill in your repo, branch, and file path, and click "Deploy". As a shortcut, you can also click "Paste GitHub URL".

## **Deploy Heroku**

https://dashboard.heroku.com/apps/airqualityindextetris/deploy/


### **Deploy using Heroku Git**

Use git in the command line or a GUI tool to deploy this app.

### **Install the Heroku CLI**

Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

### **Clone the repository**

Use Git to clone airqualityindextetris's source code to your local machine.

```
$ heroku git:clone -a airqualityindextetris 
$ cd airqualityindextetris
```

### **Deploy your changes**

Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```