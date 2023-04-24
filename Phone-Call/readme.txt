Heres how to create a phone call app using python

STEP 1
create the director and cd into it

STEP 2
install pip (python package manager)
pip install --upgrade pip (installs python)
pip --version (checks version)

STEP 3
install virtualenv
pip install virtualenv

STEP 3
create the virtual env and enter it
python3 -m venv venv (creates virtual env)
source venv/bin/activate (activate virtual env)
which Python (command confirms which env)
pip install twilio (install Twilio Python Helper library, which is used to work with phone calls.)

STEP 4
Login and Auth with Twilio acct credentials
credentials can be found on twilio dashboard
In terminal add credentials as env variabls
export TWILIO_ACCOUNT_SID=xxxxxxxxx
export TWILIO_AUTH_TOKEN=xxxxxxxxx

STEP 5
buy twilio phone number

STEP 6
Create a TwiML Bin
(Twillio markup language, stores instructions on how to handle a call)
when a call is made, twilio sends a request to url associated to number, url responds, uses bin to define how to handle call

add this to your bin:
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>Hello, from Python!</Say>
</Response>

now hit create

STEP 7
copy url thats generated to clipboard

STEP 8
in your main.py copy and paste all this and replace appropriate lines:

from twilio.rest import Client

client = Client()
call = client.calls.create(
    from_='<your-twilio-phone-number>',
    to='<your-phone-number>',
    url='<your-twiml-bin-url>'
)

STEP 9
run it!
python call.py
replace the word call with the name of your python file

Project explanation:
v1
Using a Twilio number purchased and hosted by twilio, the app can make calls to listed and verified numbers.
The caller response is stored in TwiML Bin, which we edit using Twillios Markup language. Using a webhook http post method, Twillio
is able to send and receive calls. Using the Twilio.rest module and importing the Client class, we created a client
using python that enables calls to be sent from the twillio number, to specific numbers, providing responses from TwiML BIn
We run the python scripts and that's how we can make calls

v2 automate





Cleanup
run which Python to check the dir of your venv and delete
Deleteing venv just involves deleting folder
sudo rm -rf venv

Extra tips
to port your phone number you have to upgrade twilio acct
printenv (views all env variables)
echo $JAVA_HOME (shows specific env variable value)
The value of the temporary environment variable is lost when the application process ends or when you terminate it.
export MY_VAR=value
print out temp variable
export $MY_VAR
Since the latest macOS uses the Zsh shell, So we can add the environment variables to the ~/.zshrc or ~/.zshenv file for the current user
export JAVA_HOME=$(/usr/libexec/java_home -v11)
export PATH="$JAVA_HOME/bin:$PATH"
First line sets the JAva_home env varialbe value
second sets the path
Older than macOS 10.15 uses the Bash shell as default. That user’s edit ~/bash_profile for adding permanent environment variables.
zshrc is runtime config, zshenv is zshell env
Twillio reference guide: https://www.twilio.com/docs/voice/twiml
crontab -e to create a crontab
format: schedule / full path to python / full path to script
crontab -l to see scheduled ones
crontab -r deletes crontab

venv
python3 -m venv (directory path)
source (directory path)/bin/activate
deactivate (while in venv)
rm -r (directory path) to delete
echo -n > /tmp/stdout.log
pip list --local to see a list of installed python files


import os
OS Module
It is possible to automatically perform many operating system tasks.
The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents,
changing and identifying the current directory, etc.

from dotenv import load_dotenv
used to allow data to be loaded from .env files

from twilio.rest import Client
to be able to create a client to make calls using twilio


