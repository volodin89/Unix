import socket


def coder(msg, shift):
    russian_lower = "".join(map(chr, range(ord("а"), ord("я") + 1)))
    russian_upper = "".join(map(chr, range(ord("А"), ord("Я") + 1)))
    latin_lower = "".join(map(chr, range(ord("a"), ord("z") + 1)))
    latin_upper = "".join(map(chr, range(ord("A"), ord("Z") + 1)))
    res = ""
    for i in msg:
        if i in russian_lower:
            ind = russian_lower.index(i)
            res += russian_lower[(ind + shift) % len(russian_lower)]
        elif i in russian_upper:
            ind = russian_upper.index(i)
            res += russian_upper[(ind + shift) % len(russian_upper)]
        elif i in latin_lower:
            ind = latin_lower.index(i)
            res += latin_lower[(ind + shift) % len(latin_lower)]
        elif i in latin_upper:
            ind = latin_upper.index(i)
            res += latin_upper[(ind + shift) % len(latin_upper)]
        else:
            res += i
    return res


def decoder(msg, shift):
    russian_lower = "".join(map(chr, range(ord("а"), ord("я") + 1)))
    russian_upper = "".join(map(chr, range(ord("А"), ord("Я") + 1)))
    latin_lower = "".join(map(chr, range(ord("a"), ord("z") + 1)))
    latin_upper = "".join(map(chr, range(ord("A"), ord("Z") + 1)))
    res = ""
    for i in msg:
        if i in russian_lower:
            ind = russian_lower.index(i)
            res += russian_lower[(ind - shift) % len(russian_lower)]
        elif i in russian_upper:
            ind = russian_upper.index(i)
            res += russian_upper[(ind - shift) % len(russian_upper)]
        elif i in latin_lower:
            ind = latin_lower.index(i)
            res += latin_lower[(ind - shift) % len(latin_lower)]
        elif i in latin_upper:
            ind = latin_upper.index(i)
            res += latin_upper[(ind - shift) % len(latin_upper)]
        else:
            res += i
    return res


while True:
    sock = socket.socket()
    sock.connect(('localhost', 9040))

    command = input()
    encrypt = coder(command, 15)
    sock.send(encrypt.encode())

    data = sock.recv(1024)
    sock.close()
    decrypt = decoder(data.decode(), 20)
    print(decrypt)
