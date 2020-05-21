import socket
import ssl

hostname = 'docs.python.org'
protocols_to_test = [ssl.PROTOCOL_TLSv1, ssl.PROTOCOL_TLSv1_1, ssl.PROTOCOL_TLSv1_2]

for protocol in protocols_to_test:
    context = ssl.SSLContext(protocol=protocol)
    try:
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(ssock.version())
                print(ssock.cipher())
    except ssl.SSLError as e:
        print(f'SSL error with protocol {protocol}')
        print(e)
