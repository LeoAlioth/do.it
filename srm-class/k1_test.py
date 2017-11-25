from srmclass import Srm

k1 = Srm("https://k1.srm.bajtahack.si:30100")
#k1.alloc_gpio(26)
#k1.set_gpio_dir(26, "in")
#print(k1.get_gpio_value(26))
k1.alloc_i2c(1)

