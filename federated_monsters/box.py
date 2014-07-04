# -*- coding: utf-8 -*-
"""This contains the Box class, which is used to run a server."""

import socket
# import sys
import threading


class Box:

    """A class to contain represent a storage server instance.

    Attributes:
        enc (str): The text encoding to be used to transfer data.
        host (str): The host to be used. Left blank since it's a local server.
        port (int): The port to run the server on.
    """

    enc = "UTF-8"

    def __init__(self, port=8888):
        """Init Box with port.

        Args:
            port (int, optional): The port on which the server will be run.
        """
        self.host = ''   # Symbolic name meaning all available interfaces
        self.port = port  # Arbitrary non-privileged port

    def client_thread(self, conn):
        """Handle connections to the server. Used to spawn threads.

        Args:
            conn (socket.socket): A socket object to connect to.

        Returns:
            None
        """
        # Sending message to connected client
        self.print_stream(conn,
                          'Welcome to the server.\
 Type something and hit enter\n')

        # Infinite loop so that function do not terminate and thread do not end
        while True:
            # Receiving from client
            data = conn.recv(1024)
            # reply = 'OK...' + data.decode(self.enc)
            if not data:
                break

            self.respond_to_input(conn, data.decode(self.enc))
            # self.print_stream(conn, reply)

        # Come out of loop
        conn.close()

    def respond_to_input(self, conn, text):
        """Parse and respond to data sent to the server.

        Args:
            conn (socket.socket): The socket to which the string is sent.
            text (str): The text to be parsed by the server.

        Returns:
            bool: True if successful, False if error.
        """
        words = text.split(" ")
        cmd = words[0]
        args = words[1:]
        try:
            self.print_stream(conn, "%s %s\n" % (cmd, args))
        except socket.error:
            return False

        return True

    def print_stream(self, conn, text):
        """Send text to a socket connection.

        Args:
            conn (socket.socket): The socket to which the string is sent.
            text (str): The text to send.

        Returns:
            None

        Raises:
            socket.error: If conn.sendall encounters an error.
        """
        conn.sendall(bytes(text, self.enc))

    def run(self):
        """Execute the main loop of the server.

        Returns:
            bool: True if successful, False if socket error.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        # Bind socket to local host and port
        try:
            sock.bind((self.host, self.port))
        except socket.error as msg:
            print('Bind failed. Error Code: '+str(msg[0])+' Message '+msg[1])
            # sys.exit()
            return False

        print('Socket bind complete')

        # Start listening on socket
        sock.listen(10)
        print('Socket now listening')

        # Keep talking with the client
        while True:
            # Wait to accept a connection - blocking call
            conn, addr = sock.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))

            # Start a new thread
            thr = threading.Thread(target=self.client_thread, args=(conn,))
            thr.start()

        sock.close()
        return True
