from wakeonlan import send_magic_packet

def wake(device):

    print("from wake block printing mac: ", device['device']['mac'] )
    # print("from wake block printing ip address: ", device['device']['ip_addr'])

    #print(device)
    try:
        send_magic_packet(device['device']['mac'],
        ip_address = device['device']['ip_addr'],
        port = 9)
        return "initiated wake up call"
    except:
        return "Failed to initiated wake up call"