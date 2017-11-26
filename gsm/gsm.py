import subprocess


class Gsm:

    def __init__(self, phone_num):
        self.phone_num = phone_num

    def send_msg(self):
        return None

    def read_msg(self, msg_id):
        p = subprocess.Popen(["mmcli", "-s", str(msg_id)], stdout=subprocess.PIPE)
        output = str(p.stdout.read(), "utf-8")
        output = output.split("text: ")[-1].split("\n")[0].strip("'")
        return output

    def check_for_new_msg(self):
        p = subprocess.Popen(["mmcli", "-m", "0", "--messaging-list-sms"], stdout=subprocess.PIPE)
        output = str(p.stdout.read(), "utf-8")
        if output.find('No SMS messages were found') != -1:
            return False
        else:
            return int(output.split("/")[-1].split(" ")[0])

    def del_msg(msg_id):
        p = subprocess.Popen(["mmcli", "-m", "0", "--messaging-delete-sms=" str(msg_id)], stdout=subprocess.PIPE)
        output = str(p.stdout.read(), "utf-8")
        if output.find("successfully deleted SMS from modem") != -1:
            return True
        else:
            return False
