import socket
import functools

ConnectionRefusedError = socket.error

msgs = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn = s.connect(('localhost', 80))
    # normal way
    # while True:
    #    msg = coon.recv(1024)
    #    if recv:
    #        msgs.append(msg)
    # else:  # when no msg come, break
    #         break

    # hack way with iter and functools.partial
    # this circle will auto break when msg is empty ''
    for msg in iter(functools.partial(conn.recv, 1024), b''):
        msgs.append(msg)
except (socket.error, ConnectionRefusedError):
    pass