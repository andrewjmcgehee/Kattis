ins = input()
while ins != '0':
    ins = [int(i) for i in ins.split()]
    key_len = ins[0]
    key = ins[1:]

    for i in range(len(key)):
        key[i] -= 1

    message = input()
    length = len(message)
    padding = key_len - length % key_len
    if length % key_len != 0:
        message += (' ' * padding)

    length = len(message)
    num_parts = length//key_len
    parts = []

    for i in range(num_parts):
        parts.append(message[key_len*i:key_len*(i+1)])

    for i in range(len(parts)):
        copy = ''
        for index in key:
            copy += parts[i][index]
        parts[i] = copy

    encrypted = "'"
    encrypted += ''.join(parts)
    encrypted += "'"
    print(encrypted)
    ins = input()
