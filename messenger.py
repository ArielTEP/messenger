
import fbchat 
from getpass import getpass 
from fbchat import Client
from fbchat.models import *
username = str(raw_input("Username: ")) 
#client = fbchat.Client('espindola_ipn@hotmail.com', getpass()) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(raw_input("Number of friends: ")) 
for i in xrange(no_of_friends): 
    name = str(raw_input("Name: ")) 
    friends = client.searchForUsers(name)  # return a list of names 
    
    friend = friends[0] 
    print("users' names: {}".format([friend.name]))
    msg = str(raw_input("Message: ")) 
    n = int(raw_input("Number of messages: ")) 
    for x in range(n):
    	msg += ' ' + str(x)
    	client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    print("Message sent successfully!") 
client.logout()