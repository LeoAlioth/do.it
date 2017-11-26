from gsm import *
from time import sleep
from threading

p1 = Gsm("+38651884931")
last_msg = ""

while p1.check_for_new_msg():
    p1.del_msg(p1.check_for_new_msg())
    sleep(1)

t = Timer(3,check_for_msg)
t.start()

def check_for_msg():
    if p1.check_for_new_msg():
        last_msg = p1.read_msg(p1.check_for_new_msg())
    t.start()
