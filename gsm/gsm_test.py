from gsm import *
from time import sleep
import threading

p1 = Gsm()
last_msg = ""

f = print

while p1.check_for_new_msg():
    p1.del_msg(p1.check_for_new_msg())
    sleep(1)







print("almost")
p1.send_msg("+38651884931", "Please work!")
