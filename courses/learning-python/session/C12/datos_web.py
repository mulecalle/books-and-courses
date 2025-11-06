import socket

def get_remote_machine_info():

    remote_host = 'www.asd.frba.utn.edu.ar'

    try:

        print("IP address: %s" % socket.gethostbyname(remote_host))

    except socket.error as err_msg:

        print("Cannot reach: %s -- Error message: %s" % (remote_host, err_msg))


if __name__ == '__main__':
    get_remote_machine_info()