**Purpose:** Read the messages of a user chat. Filters the messages and sends it to a recipient.

**Use Case:** When you act as a middleman to get orders from customer and send it to your vendor or an admin clerk to process the information.

**Requirements:** set up Telegram Client ID. 
  - Step1 : Go to https://my.telegram.org/auth?to=apps 
  - Step2: Go to app development tools
  - Step3: Obtain the API_ID and API_HASH
  - Step4: Create a config.py file and update the values of the variables below. The respective Usernames are the Telegram account usernames.

```
#TELEGRAM API
API_ID = ""
API_HASH = ""
MY_USERNAME = <YOUR USERNAME>
READUSER = <READUSER USERNAME>
SENDUSER = <SENDUSER USERNAME>
```
