import subprocess


class Gsm:

    def __init__(self, phone_num):
        self.phone_num = phone_num



    def send_msg(self):
        return None

    def read_message(self, msg_id):
        return None

    def check_for_new_msg(self):
        p = subprocess.call(["mmcli", "-m", "0", "--messaging-list-sms"])
        if "No SMS messages were found" is in p:
            return p
        else:
            return None

