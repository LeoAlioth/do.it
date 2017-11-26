import subprocess


class Gsm:

    def __init__(self, phone_num):
        self.phone_num = phone_num

    def send_msg(self):
        return None

    def read_message(self, msg_id):
        return msg_id

    def check_for_new_msg(self):
        p = subprocess.Popen(["mmcli", "-m", "0", "--messaging-list-sms"], stdout=subprocess.PIPE)
        output = str(p.stdout.read(), "utf-8")
        if output.find('No SMS messages were found'):
            print("None")
            return False
        else:
            print(output)
            return output
