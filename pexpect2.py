import subprocess

python2_command = 'C:\Python27\python2.exe pexpect1.py'
process = subprocess.Popen(python2_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
#print(error)
# python3_command = 'python python3_script.py arg1'
# process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()