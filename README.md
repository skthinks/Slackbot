# Slackbot
## API Overview
The SlackBot Application takes input from a slack channel
Using an Outgoing Slack Web Hook, Slack issues a post request to a designated Url, as specified by the programmer. 
From this URL the Application stores the required contents into a Postgres database.

## Setup
1. First setup up a virtual environment using:
      virtualenv env
      source env/bin/activate
2. All required packages are specified in requirements.txt. 
3. Besides the above download and setup the Postgres database
 Further instructions on how to setup are available at http://www.tunnelsup.com/setting-up-postgres-on-mac-osx
4. Follow https://api.slack.com/outgoing-webhooks to setup the web hook. 

## Django Setup
1. Setup a new Django Project in the Virtual Environment using:
      django-admin startproject <proj_name>
      cd <proj_name>
      python manage.py startapp <app_name>
2. Go the <app_name> folder
    Setup the database models in models.py as given below  
    Resource: http://www.djangobook.com/en/2.0/chapter05.html
3. python manage.py makemigrations
   python manage.py migrate
4. Now you should be good to go!

## URL to Post To  
`POST  /slack`
  
## Slack Post Request  
```
token=<some_token>
team_id=T0001
team_domain=example
channel_id=C2147483705
channel_name=general
timestamp=1355517523.000005
user_id=U2147483697
user_name=Romin
text=googlebot: How many APIs are there in the ProgrammableWeb APIs?
trigger_word=ask:
```
