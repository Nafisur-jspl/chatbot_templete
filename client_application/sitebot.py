import apiai
import json
import requests
import random
from termcolor import colored

CLIENT_ACCESS_TOKEN = '<YOUR CLIENT ACCESS TOKEN>'

def print_bot_message(message):
    print colored("Bot  ::  "+message, 'blue',attrs=['dark','bold'])

def send_message_to_apiai(message):
    pass

#Intro message
print_bot_message("Hi for now I am an echo bot I am gonna just repeat what you say !! if you are tired of me just say 'exit'")

while True:
    message = raw_input("User ::  ")
    #send message to API.ai
    response = send_message_to_apiai(message)

    #process response json to extract the reply message
    #for now it is the same 
    reply_message = message

    #print reply message
    if message.lower() == "exit":
        print_bot_message("Bye !! take care")
        exit()

    print_bot_message(reply_message)
    
