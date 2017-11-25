import requests


class Srm:
    def __init__(self, url):
        self.url = url
        r = requests.get(self.url, verify=False)
        print("INIT:", r.status_code, r.reason)

    def alloc_gpio(self, gpio):
        r = requests.post(self.url + "/phy/gpio/alloc", data=str(gpio), verify=False)
        print("GPIO ALLOC:", r.status_code, r.reason)

    def set_gpio_dir(self, gpio, direction="in"):
        r = requests.get(self.url + "/phy/gpio/" + str(gpio) + "/cfg/value", verify=False)
        print("DIR:", r.status_code, r.reason)
        cfg = r.json()
        cfg["dir"] = direction
        r = requests.put(self.url + "/phy/gpio/" + str(gpio) + "/cfg/value", json=cfg, verify=False)
        print("DIR:", r.status_code, r.reason)

    def set_gpio_value(self, gpio, value):
        r = requests.put(self.url + "/phy/gpio/" + str(gpio) + "/value", data=str(value), verify=False)
        print("SET VALUE", r.status_code, r.reason)

    def get_gpio_value(self, gpio):
        r = requests.get(self.url + "/phy/gpio/" + str(gpio) + "/value", verify=False)
        print("GET VALUE", r.status_code, r.reason)
        return r.text

    def alloc_i2c(self, i2c):
        r = requests.post(self.url + "/phy/i2c/alloc", data=str(i2c), verify=False)
        print("I2C ALLOC:", r.status_code, r.reason)