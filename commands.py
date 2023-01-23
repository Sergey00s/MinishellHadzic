from dbmanage import Users
import os
import subprocess
import sys
import time

class Command:
    _command = ""
    _args = []
    cases = 0
    def __init__(self, string : str):
        if (len(string) > 6):
            self._command = string[5:]
            self._args = self._command.split()
            self._command = self._args[0]
        else:
            self._args = None
            self._command = None

    def get_command(self):
        return self._command

    def get_args(self):
        return self._args

    def codeCheck(self, data):
        path = f"./checks/{data[0]}"
        os.system(f"git clone {self.get_args()[1]} {path}")
        time.sleep(10)
        day = int(data[2])
        p = 1
        # Compile the code
        print("done")
        for i in range(0, self.cases):
            result_s = subprocess.run(["gcc", f"./today/case{i}.c", f"{path}/case{i}/case.c", "-o", f"{path}/case{i}/a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result_s.returncode != 0:
                os.system(f"rm -rf {path}")
                print(result_s.stderr.decode())
                return -1
            result = subprocess.run([f"{path}/case{i}/a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = result.stdout.decode()
            exp = result.stderr.decode()
            os.system(f"rm -rf {path}")
            if out != exp:
                return 0
            p+=1
        os.system(f"rm -rf {path}")
        return p


    def run(self, message, users):
        if self.get_command() == "regme":
            data = users.get_user_by_id(message.author.id)
            if data is None:
                users.new_user(message.author.id, message.author.name, 0, 0)
                return "User registered!"
            else:
                return "User already registered!"
        if self.get_command() == "stats":
            data = users.get_user_by_id(message.author.id)
            if data is None:
                return "User not found"
            else:
                return data

        if self.get_command() == "delme":
            data = users.get_user_by_id(message.author.id)
            if data is None:
                return "User not found"
            else:
                users.delete_user_by_id(message.author.id)
                return "User deleted"

        if self.get_command() == "testcase":
            data = users.get_user_by_id(message.author.id)
            if data is None:
                return "Kayit olmak icin '!nth regme'"
            elif message.author.name == "Sergey00":
                self.cases = int(self.get_args()[2])
                os.system("rm -rf today")
                os.system(f"git clone {self.get_args()[1]} today")
                return "done"
        if self.get_command() == "help":
            return "Commands: !nth regme, !nth stats"
        if self.get_command() == "checkme":
            data = users.get_user_by_id(message.author.id)
            if data is None:
                return "Kayit olmak icin '!nth regme'"
            else:
                mark = self.codeCheck(data)
                if mark > 0:
                    users.update_user(message.author.id, message.author.name, 1, (int(data[2])) + mark)
                    return "levelup!!"
                else:
                    return "levelup failed! :("
        return "Command not found" 


