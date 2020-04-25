import fbchat
from fbchat import Client 
from getpass import getpass 
import time
import os
from see_you_again import see_you_again

def login():
    username = str(input("Username: "))
    return fbchat.Client(username, getpass())

def choose_friend(client):
    name = str(input("Friend to sing to: "))
    return client.searchForUsers(name)[0]

def choose_song_and_sing(): # will return a dict
    print("Please choose a song:")
    for song in os.listdir():
        if song == ".git" or song == "sing.py" or song == "__pycache__":
            continue
        else:
            print(song)
    chosen_song = str(input("Your chosen song: "))

if __name__== "__main__":
    client = login()
    chosen_friend = choose_friend(client)
    choose_song_and_sing()
    
    
