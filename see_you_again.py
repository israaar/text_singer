import fbchat
from fbchat import Client 
from getpass import getpass 
import time
import os
from sing import send_lyric

def see_you_again(client):
    lyrics_raw = "Okay, okay, okay, okay Okay, okay, oh You live in my dream state We're lowkey my fantasy I stay in reality You live in my dream state Any time I count sheep That's the only time we make up, make up You exist behind my eyelids, my eyelids Now I don't wanna wake up 20/20, 20/20 vision Cupid hit me, cupid hit me with precision I wonder if you look both ways When you cross my mind, I said, I said I'm sick of, sick of, sick of, sick of chasing You're the one that's always running through my daydream, I I can only see your face when I close my eyes Can I get a kiss? And can you make it last forever? I said I'm 'bout to go to war I don't know if I'ma see you again Can I get a kiss? (Can I) And can you make it last forever? (Can you) I said I'm 'bout to go to war ('Bout to) I don't know if I'ma see you again (Uh, switch it up) I said, okay, okay, okay, okidokie, my infatuation Is translatin' to another form of what you call it? Love Oh yeah, oh yeah, oh yeah, oh yeah, I ain't met you I've been looking, stuck here waiting for I Stop the chasing, like an alcoholic You don't understand me, what the fuck do you mean? It's them rose to the cheeks, yeah it's them dirt-colored eyes Sugar honey iced tea, bumblebee on the scene Yeah I'd give up my bakery to have a piece of your pie Yugh! 20/20, 20/20 vision Cupid hit me, cupid hit me with precision I wonder if you look both ways When you cross my mind, I said, I said I'm sick of, sick of, sick of, sick of chasing You're the one that's always running through my daydream, I I can only see your face when I close my eyes (So) Can I get a kiss? (Can I get a kiss?) And can you make it last forever? (Oh, forever) I said I'm 'bout to go to war (Go to war) I don't know if I'ma see you again (See you again) Can I get a kiss? (Can I) And can you make it last forever? (Can you) I said I'm 'bout to go to war ('Bout to) I don't know if I'ma see you again Okay, okay, okay, okay Okay, okay, okay, oh La la, la la la la, la la La la, la la la, la la One more time?" 
    lyrics = lyrics_raw.split()

    name = str(input("Friend to sing to: "))
    friend = client.searchForUsers(name)[0]

    time.sleep(2)

    for word in range(0,7):
        send_lyric(word, friend)
        # print(lyrics[word])
        time.sleep(0.35)

    time.sleep(0.65)

    for word in range(7,12):
        send_lyric(word, friend)
        # print(lyrics[word])
        time.sleep(0.15)

    time.sleep(0.77)
    send_lyric(lyrics[12], friend)
    # print(lyrics[12])

