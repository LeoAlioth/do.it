import subprocess


class Gsm:

    def __init__(self):
        while self.check_for_new_msg():
            self.del_msg(self.check_for_new_msg())
        self.init_msg_check_thread()

    def send_msg(self, number, content):
        print("Sending")
        msg = "--messaging-create-sms=number=\"" + number + "\",text=\"" + content + "\",smsc=\"+38641001333\",validity=100,class=1,delivery-report-request=no"
        print(msg)

        p = subprocess.Popen(["mmcli", "-m", "0", msg], stdout=subprocess.PIPE)
        p.wait()
        print("woke up")
        msg_id = self.check_for_new_msg()
        p = subprocess.Popen(["mmcli", "-m", "0", "-s", str(msg_id), "--send"], stdout=subprocess.PIPE)
        p.wait()
        return None

    def read_msg(self, msg_id):
        p = subprocess.Popen(["mmcli", "-s", str(msg_id)], stdout=subprocess.PIPE)
        p.wait()
        output = str(p.stdout.read(), "utf-8")
        output = output.split("text: ")[-1].split("\n")[0].strip("'")
        self.del_msg(msg_id)
        return output

    def check_for_new_msg(self):
        p = subprocess.Popen(["mmcli", "-m", "0", "--messaging-list-sms"], stdout=subprocess.PIPE)
        p.wait()
        output = str(p.stdout.read(), "utf-8")
        if output.find('No SMS messages were found') != -1:
            return False
        else:
            return int(output.split("/")[-1].split(" ")[0])

    def del_msg(self, msg_id):
        p = subprocess.Popen(["mmcli", "-m", "0", "--messaging-delete-sms="+str(msg_id)], stdout=subprocess.PIPE)
        p.wait()
        output = str(p.stdout.read(), "utf-8")
        if output.find("successfully deleted SMS from modem") != -1:
            return True
        else:
            return False

    def init_msg_check_thread(self):
        rec_t = threading.Thread(target=msg_check_thread)
        rec_t.start()

    def msg_check_thread(self):
        while 1:
            if self.check_for_new_msg():
                print(self.read_msg(p1.check_for_new_msg()))

