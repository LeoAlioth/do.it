from gsm import *
from time import sleep

p1 = Gsm("+38651884931")

while p1.check_for_new_msg():
    p1.del_msg(p1.check_for_new_msg())
    sleep(1)

while 1:
    if p1.check_for_new_msg():
        print(p1.read_msg(p1.check_for_new_msg()))
    sleep(1)
