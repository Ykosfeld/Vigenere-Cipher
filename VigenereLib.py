def contador_senha(c, s):
    if c >= len(s):
        conts = abs(c % len(s))
    else:
        conts = c
    return conts

def crypto(mens, snh):
    result = []
    for cont in range(len(mens)):
        newl = (ord(snh[contador_senha(cont, snh)]) - 64) + (ord(mens[cont]) - 64) - 1
        if newl > 26:
            newl -= 26
        result += chr(newl+64)
    return result

def decrypto(mens, snh):
    result = []
    for cont in range(len(mens)):
        newl = (ord(mens[cont]) - 64) - (ord(snh[contador_senha(cont, snh)]) - 64) + 1
        if newl < 0:
            newl += 26
        result += chr(newl+64)
    return result

def print_bolado(coisa):
    for l in coisa:
        print(l, end='')
    print('')
    return