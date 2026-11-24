#revisa si es primo
def es_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# calcula el inverso de e módulo phi segun la formula
def inverso(e, phi):
    r0, r1 = phi, e % phi
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    return t0 % phi


#calcula una potencia módulo n
def exp_mod(b, e, n):
    res = 1
    b = b % n
    while e > 0:
        if e % 2 == 1:
            res = res * b % n
        b = b * b % n
        e = e // 2
    return res


#revisa los datos y calcula n y phi
def revisar(p, q, e):
    try:
        p = int(p)
        q = int(q)
        e = int(e)
    except ValueError:
        raise ValueError("p, q y e tienen que ser enteros")
    if not es_primo(p) or not es_primo(q):
        raise ValueError("p y q tienen que ser primos")
    if p == q:
        raise ValueError("p y q tienen que ser distintos")
    n = p * q
    phi = (p - 1) * (q - 1)
    if n <= 126126 or n >= 1000000:
        raise ValueError(f"n = {n} no esta entre 126126 y 1000000")
    if e <= 1 or mcd(e, phi) != 1:
        raise ValueError(f"e tiene que ser mayor a 1 y MCD(e, {phi}) = 1")
    return e, n, phi


#encripta el mensaje de dos caracteres en dos
def encriptar(msg, p, q, e):
    e, n, phi = revisar(p, q, e)
    if msg == "":
        raise ValueError("El mensaje esta vacio")
    for c in msg:
        if ord(c) < 32 or ord(c) > 126:
            raise ValueError(f"Caracter no permitido: {c!r}")
    L = len(msg)
    #agrega un espacio si queda un carácter solo
    if L % 2 == 1:
        msg = msg + " "
    txt = f"n = {n}\nphi = {phi}\nL = {L}\nRelleno: {'si' if L % 2 == 1 else 'no'}\n\n"
    C = []
    for i in range(0, len(msg), 2):
        a = str(ord(msg[i])).zfill(3)
        b = str(ord(msg[i + 1])).zfill(3)
        c = str(exp_mod(int(a + b), e, n)).zfill(6)
        C.append(c)
        txt += f"'{msg[i]}' = {a}, '{msg[i + 1]}' = {b}  ->  m = {a + b}  ->  c = {c}\n"
    C = " ".join(C)
    txt += f"\nC = {C}\nL = {L}\nLlave publica (e, n) = ({e}, {n})"
    return C, L, txt


#desencripta los bloques y recupera el mensaje
def desencriptar(C, L, p, q, e):
    e, n, phi = revisar(p, q, e)
    bloques = C.split()
    if len(bloques) == 0:
        raise ValueError("C esta vacio")
    for c in bloques:
        if len(c) != 6 or not all(x in "0123456789" for x in c):
            raise ValueError(f"El bloque {c} no tiene 6 digitos")
        if int(c) >= n:
            raise ValueError(f"El bloque {c} es mayor o igual a n = {n}")
    try:
        L = int(L)
    except ValueError:
        raise ValueError("L tiene que ser entero")
    k = len(bloques)
    if L != 2 * k and L != 2 * k - 1:
        raise ValueError(f"Con {k} bloques L tiene que ser {2 * k} o {2 * k - 1}")
    d = inverso(e, phi)
    txt = f"n = {n}\nphi = {phi}\nd = {d}\nL = {L}\nRelleno: {'si' if L % 2 == 1 else 'no'}\n\n"
    msg = ""
    for c in bloques:
        m = str(exp_mod(int(c), d, n)).zfill(6)
        a = int(m[:3])
        b = int(m[3:])
        if a < 32 or a > 126 or b < 32 or b > 126:
            raise ValueError(f"El bloque {c} no da codigos ASCII validos")
        msg += chr(a) + chr(b)
        txt += f"c = {c}  ->  m = {m}  ->  {m[:3]} = '{chr(a)}', {m[3:]} = '{chr(b)}'\n"
    #quita el espacio que se agregó como relleno
    if L % 2 == 1:
        if msg[-1] != " ":
            raise ValueError("L es impar pero el ultimo caracter no es espacio")
        msg = msg[:-1]
    txt += f"\nd = {d}\nMensaje = \"{msg}\""
    return msg, txt