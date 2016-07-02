table = [
    0b1,
    0b11,
    0b1001,
    0b101,
    0b1100,
    0b101,
    0b1101,
    0b1111
]

def crypt(sel, message, key):
    sel %= len(table)
    message = list(map(lambda x: ord(x) << sel, message))
    encryption = []
    counter = 0
    for i, m in enumerate(message):
        if not i % sel:
            encryption += [(table[(_ + counter) % len(table)] << sel << sel) ^ key for _ in range(sel)] + [m]
            counter += 1
        else:
            encryption += [m]
    return encryption

def decrypt(message, key):
    d = message[0] ^ key
    count = 0
    decrypted = []
    while d != table[0]:
        d >>= 2
        count += 1
    print("sel:: ", count)
    ok = False
    for i, m in enumerate(message):
        if ok:
            decrypted.append(m)
        if not i % count:
            ok = not ok
    print("decrypted:: ", decrypted)
    return "".join(chr(c) for c in decrypted)

# c = crypt(int(input("sel> ")), input("message> "), int(input("key> ")))
# print(c)
# print(decrypt(c, int(input("key> "))))
