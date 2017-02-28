import paramiko
import time


def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


if __name__ == '__main__':


    # VARIABLES
    
    ip = "10.28.0.20"
    ip2 = "10.28.0.24"
    ip3 = "10.220.0.5"
    username = input("Username: ")
    password = input("Password: ")
    site_name = input("Type name of site here with no spaces: ")

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

    # Send the controller a list of commands
    remote_conn.send("\n")
    remote_conn.send("%s\n" % (username))
    remote_conn.send("%s\n" % (password))
    remote_conn.send("config\n")
    remote_conn.send("flexconnect group %s add\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add primary 10.2.9.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add secondary 10.220.11.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap server-key radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority id 00000000000000000000000000000000\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority info\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap pac-timeout 180\n" % (site_name))
    remote_conn.send("flexconnect group %s http-proxy ip-address 0.0.0.0 http-proxy port 0\n" % (site_name)) 
    remote_conn.send("flexconnect group %s vlan enable\n" % (site_name))
    remote_conn.send("flexconnect group %s vlan native 2\n" % (site_name))
    remote_conn.send("flexconnect group %s template-vlan-map add none\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_FIX_LATER\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_NO_INTERNET\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add DENY_ALL_TRAFFIC\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_MACHINE_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_INTERNET_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE_BYOD\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_IT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT1\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_AGENT_REDIRECT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_ORACLE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_SERVICE_DESK_REMEDIATION\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_GENERAL\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 16 add vlan 125\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 11 add vlan 150\n" % (site_name))
    remote_conn.send("wlan apgroup add %s %s\n" % (site_name, site_name))
    remote_conn.send("wlan apgroup qinq tagging eap-sim-aka %s enable\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 16 wwt\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 5 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 3 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 17 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 11 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 16 \n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 5\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 3\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 17\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 11\n" % (site_name)) 
    remote_conn.send("apgroup hotspot venue type %s 0 0\n" % (site_name))
    
    # Wait for the command to complete
    time.sleep(25)
    
    output = remote_conn.recv(5000)
    print (output)



    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip2, username=username, password=password, look_for_keys=False, allow_agent=False)
    print("SSH connection established to %s" % (ip2))

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print("Interactive SSH session established")

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print (output)

    # Send the controller a list of commands
    remote_conn.send("\n")
    remote_conn.send("%s\n" % (username))
    remote_conn.send("%s\n" % (password))
    remote_conn.send("config\n")
    remote_conn.send("flexconnect group %s add\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add primary 10.2.9.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add secondary 10.220.11.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap server-key radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority id 00000000000000000000000000000000\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority info\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap pac-timeout 180\n" % (site_name))
    remote_conn.send("flexconnect group %s http-proxy ip-address 0.0.0.0 http-proxy port 0\n" % (site_name)) 
    remote_conn.send("flexconnect group %s vlan enable\n" % (site_name))
    remote_conn.send("flexconnect group %s vlan native 2\n" % (site_name))
    remote_conn.send("flexconnect group %s template-vlan-map add none\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_FIX_LATER\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_NO_INTERNET\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add DENY_ALL_TRAFFIC\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_MACHINE_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_INTERNET_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE_BYOD\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_IT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT1\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_AGENT_REDIRECT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_ORACLE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_SERVICE_DESK_REMEDIATION\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_GENERAL\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 16 add vlan 125\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 11 add vlan 150\n" % (site_name))
    remote_conn.send("wlan apgroup add %s %s\n" % (site_name, site_name))
    remote_conn.send("wlan apgroup qinq tagging eap-sim-aka %s enable\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 16 wwt\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 5 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 3 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 17 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 11 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 16 \n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 5\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 3\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 17\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 11\n" % (site_name)) 
    remote_conn.send("apgroup hotspot venue type %s 0 0\n" % (site_name))
    
    # Wait for the command to complete
    time.sleep(25)
    
    output = remote_conn.recv(5000)
    print (output)

        # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip3, username=username, password=password, look_for_keys=False, allow_agent=False)
    print("SSH connection established to %s" % (ip3))

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print("Interactive SSH session established")

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print (output)

    # Send the controller a list of commands
    remote_conn.send("\n")
    remote_conn.send("%s\n" % (username))
    remote_conn.send("%s\n" % (password))
    remote_conn.send("config\n")
    remote_conn.send("flexconnect group %s add\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add primary 10.2.9.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius server auth add secondary 10.220.11.10 1812 radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap server-key radius\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority id 00000000000000000000000000000000\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap authority info\n" % (site_name))
    remote_conn.send("flexconnect group %s radius ap pac-timeout 180\n" % (site_name))
    remote_conn.send("flexconnect group %s http-proxy ip-address 0.0.0.0 http-proxy port 0\n" % (site_name)) 
    remote_conn.send("flexconnect group %s vlan enable\n" % (site_name))
    remote_conn.send("flexconnect group %s vlan native 2\n" % (site_name))
    remote_conn.send("flexconnect group %s template-vlan-map add none\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_FIX_LATER\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_NO_INTERNET\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add DENY_ALL_TRAFFIC\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_MACHINE_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_INTERNET_ONLY\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_PRE_POSTURE_BYOD\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_IT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_NONCOMPLIANT1\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_AGENT_REDIRECT\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_ORACLE\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_SERVICE_DESK_REMEDIATION\n" % (site_name))
    remote_conn.send("flexconnect group %s policy acl add WWT_POSTURE_COMPLIANT_GENERAL\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 16 add vlan 125\n" % (site_name))
    remote_conn.send("flexconnect group %s wlan-vlan wlan 11 add vlan 150\n" % (site_name))
    remote_conn.send("wlan apgroup add %s %s\n" % (site_name, site_name))
    remote_conn.send("wlan apgroup qinq tagging eap-sim-aka %s enable\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 16 wwt\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 5 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 3 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 17 management\n" % (site_name))
    remote_conn.send("wlan apgroup interface-mapping add %s 11 wwtshared\n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 16 \n" % (site_name))
    remote_conn.send("wlan apgroup nac-snmp disable %s 5\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 3\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 17\n" % (site_name)) 
    remote_conn.send("wlan apgroup nac-snmp disable %s 11\n" % (site_name)) 
    remote_conn.send("apgroup hotspot venue type %s 0 0\n" % (site_name))
    
    # Wait for the command to complete
    time.sleep(25)
    
    output = remote_conn.recv(5000)
    print (output)

