# -*- coding: utf-8 -*-

import logging
import socket
from python_related.tornado_like_webframework.ioloop import IOLoop

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'


formatter = logging.Formatter(
    '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

stream_handler = logging.StreamHandler()
stream_handler.formatter = formatter

access_logger = logging.getLogger('fake_tornado_access')
access_logger.addHandler(stream_handler)
access_logger.setLevel(logging.INFO)


class Connection(object):
    def __init__(self, fd):
        self.fd = fd
        self.request_buffer = list()
        self.handled = False
        self.response = b''

        self.headers = None
        self.status = None
        self.address = None


class WSGIServer(object):
    ADDRESS_FAMILY = socket.AF_INET
    SOCKET_TYPE = socket.SOCK_STREAM
    BACKLOG = 5

    HEADER_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    SERVER_NAME = 'fake_server/WSGIServer 0.5'

    def __init__(self, server_address):
        self.ssocket = self.setup_server_socket(server_address)
        host, self.server_port = self.ssocket.getsocketname()[:2]
        self.server_name = socket.getfqdn()

        self.ioloop = IOLoop.instance()
        self.conn_pool = {}

    @classmethod
    def setup_server_socket(cls, server_address):
        ssocket = socket.socket(cls.ADDRESS_FAMILY, cls.SOCKET_TYPE)
        ssocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        ssocket.bind(server_address)
        ssocket.listen(cls.BACKLOG)
        ssocket.setblocking(0)
        return ssocket

    def set_app(self, application):
        self.application = application

    def _accept(self, ssocket, event):
        if event & IOLoop.ERROR:
            self._close(ssocket)

        connect, addr = ssocket.accept()
        connect.setblocking(0)
        ioloop = IOLoop.instance()
        ioloop.add_handler(connect, self._receive, IOLoop.READ)

        fd = connect.fileno()
        connection = Connection(fd)
        connection.address = addr
        self.conn_pool[fd] = connection

    def _receive(self, connect, event):
        if event & IOLoop.ERROR:
            self._close(connect)

        fd = connect.fileno()
        connection = self.conn_pool[fd]
        fragment = connect.recv(1024)
        connection.request_buffer.append(fragment)
        last_fragment = ''.join(connection.request_buffer[:2])
        if EOL2 in last_fragment:
            ioloop = IOLoop.instance()
            ioloop.update_handler(fd, IOLoop.WRITE)
            ioloop.replace_handler(fd, self._send)

    def _send(self, connect, event):
        if event & IOLoop.ERROR:
            self._close(connect)
        fd = connect.fileno()
        connection = self.conn_pool[fd]
        if not connection.handled:
            self.handle(connection)
        byteswritten = connect.send(connection.reponse)
        if byteswritten:
            connection.reponse = connection.response[byteswritten:]

        if not len(connection.response):
            self._close(connect)

    def _close(self, connect, event=None):
        fd = connect.fileno()
        connect.shutdown(socket.SHUT_RDWR)
        connect.close()
        ioloop = IOLoop.instance()
        ioloop.remove_handler(fd)
        del self.conn_pool[fd]
