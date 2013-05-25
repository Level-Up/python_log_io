import socket


class Send():
    """Send log message to log.io"""
    config_dict = {}

    def __init__(self, msg):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = self.config_dict['host']
        port = self.config_dict['port']
        client_socket.connect((host, port))
        client_socket.send(msg)
        client_socket.close()
