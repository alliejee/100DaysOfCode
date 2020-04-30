import paramiko
import getpass

PORT = 22

def run_command(username, password, cmd, target, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(target, port, username, password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read())



def main():
    username = input("username: ")
    pword = getpass.getpass(prompt="password: "))
    target = input("host: ")
    cmd = 'ls -l /dev'
    
if __name__ == '__main__':
    main()