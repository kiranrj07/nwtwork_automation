import paramiko, time
connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('192.168.0.101', username='admin', password='root@123', look_for_keys=False, allow_agent=False)
new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output)
time.sleep(3)

# new_connection.send("show version | i V\n")
# time.sleep(3)
# output = new_connection.recv(5000)


new_connection.send("en")
time.sleep(5)
output = new_connection.recv(5000)
print(output)

time.sleep(5)
new_connection.send("root@123")
time.sleep(2)
output = new_connection.recv(5000)
print(output)

new_connection.send("configure terminal \n")
time.sleep(2)
output = new_connection.recv(5000)
print(output)

new_connection.send("do sh ip inter br \n")
time.sleep(2)
output = new_connection.recv(5000)
print(output)

new_connection.close()