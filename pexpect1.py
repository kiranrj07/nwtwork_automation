
import pexpect
# #child = pexpect.spawn('telnet 192.168.1.254')
# child = pexpect.run('cmd.exe')
# child.expect('Username')
# child.sendline('admin')
# child.expect('Password')
# child.sendline('root@458')
# child.expect('TW360ROUTER#')
# print child.before
# print child.after
# child.sendline('show ip dhcp binding | inc 192.168.1.241')
# child.expect('Automatic')
# print child.before
# print child.after




import wexpect
#child = wexpect.run('cmd.exe telnet 192.168.1.254')
child = pexpect.popen_spawn.PopenSpawn('telnet 192.168.1.254')
child.interactive()
child.expect('C:\\Users\\tw360>')
print(child.before)
print(child.after)
#child = wexpect.spawn('telnet 192.168.1.254')
# print(child.expect('>'))
# child.sendline('ls')
# child.expect('>')
# print(child.before)
# child.sendline('exit')