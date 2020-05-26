"""TLS Scan
Usage:
    tlsscan.py scan <host>

Options:
    -h --help   Show this screen.
    -j --json   Print the output in JSON.

"""
from docopt import docopt

import socket
import ssl
import json

def scan(host):
    protocols = [ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2]
    available_protocols = []
    unavaile_protocols = []

    for protocol in protocols:
        context = ssl.SSLContext(protocol=protocol)
        try:
            with socket.create_connection((host, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    print(sock)
                    print(ssock)
                    available_protocols.append(protocol)
        except ssl.SSLError:
            unavaile_protocols.append(protocol)

    return {
        'available_protocols': available_protocols,
        'unavailable_protocols': unavaile_protocols
    }


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    if arguments['scan'] is True:
        print("Scanning...")
        print(json.dumps(scan(arguments['<host>'])))
