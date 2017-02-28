import paramiko
import time
import csv
import getpass


csvFile = csv.reader(open(input('File Path of CSV of data that needs to be imported: ')))

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


if __name__ == '__main__':


    # VARIABLES
    
    ip = input("Type IP of WLC: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print("SSH connection established to %s" % (ip))

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print("Interactive SSH session established")

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print (output)
    remote_conn.send("\n")
    remote_conn.send("%s\n" % (username))
    remote_conn.send("%s\n" % (password))
    remote_conn.send("config\n")

    for row in csvFile:
        col1, col2 = row
    # Send the controller a list of commands
        remote_conn.send("ap name %s %s\n" % (col1, col2))
        print(output)
   
    # Wait for the command to complete
    time.sleep(10)
    
    output = remote_conn.recv(5000)
    print (output)
