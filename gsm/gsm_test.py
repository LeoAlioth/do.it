from gsm import *

p1 = Gsm("+38651884931")
print(p1.read_msg(p1.check_for_new_msg()))