import subprocess

def ping(hostname):
  #hostname = "192.168.0.103"
  output = subprocess.Popen(["ping.exe",hostname],stdout = subprocess.PIPE).communicate()[0]

  print("In ping fun putput is: ",output)

  if ('unreachable' in str(output)):
    result='unreachable'
  elif( 'timed out' in str(output)):
    result='time-out'
  else:
    result='success'

  arr=output.split()
  print(str(arr[-1]).replace('b',''))
  avg=str(arr[-1]).replace('b','')
  return result+avg

