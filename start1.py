from wakeonlan import send_magic_packet
import json

def wake(dev):



    device=json.loads(dev)
    print("from wake block printing ip address: ", device['device']['ip_addr'])
    try:
        send_magic_packet(device['device']['mac'],
        ip_address = device['device']['ip_addr'],
        port = 9)
        return "initiated wake up call"
    except:
        return "Failed to initiated wake up call"