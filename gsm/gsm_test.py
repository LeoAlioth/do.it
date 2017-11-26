from gsm import *
from time import sleep
import threading

p1 = Gsm("+38651884931")
last_msg = ""

f = print

while p1.check_for_new_msg():
    p1.del_msg(p1.check_for_new_msg())
    sleep(1)


def check_for_msg():
    while 1:
        if p1.check_for_new_msg():
            f(p1.read_msg(p1.check_for_new_msg()))
        sleep(1)


rec_t = threading.Thread(check_for_msg())
