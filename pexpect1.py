import pexpect
child = pexpect.spawn('telnet 10.1.1.177')
child.expect('Username')
child.sendline('root')
child.expect('Password')
child.sendline('root@123')
child.expect('R1>')
child.sendline('enable')
child.expect('Password')
child.sendline('root@123')
child.expect('R1#')
child.sendline('show version | i v')
child.before
child.sendline('configure termainal')


