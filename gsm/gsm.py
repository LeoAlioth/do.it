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
        output = p.stdout.read()
        print(type(str(output)))
        print(type('No SMS messages were found'))
        if output.find('No SMS messages were found'):
            print(output)
            return p
        else:
            print("None")
            return None
