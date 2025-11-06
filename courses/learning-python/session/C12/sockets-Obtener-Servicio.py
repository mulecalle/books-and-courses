import socket

def find_service_name():

    tcpProtocol = 'tcp'

    print('---'+ tcpProtocol)
    for port in [80, 25, 53]:

        try:
            print("Port[tcp]: %s => service name: %s" %(port, socket.getservbyport(port, tcpProtocol)))
        except:
            print("Protocol error at port %s and protocol %s" % (port, tcpProtocol))


    udpProtocol = 'udp'

    print('---' + udpProtocol)
    for port in [80, 25, 53]:

        try:
            print("Port[udp]: %s => service name: %s" %(port, socket.getservbyport(port, udpProtocol)))
        except:
            print("Protocol error at port %s and protocol %s" % (port, udpProtocol))


if __name__ == '__main__':

    find_service_name()