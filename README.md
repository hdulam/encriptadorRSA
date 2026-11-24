# Parcial 3 (Encriptacion RSA) - MM2015 Matematica Discreta 1

Hector Duarte y Luis Gutierrez


## Instalacion y ejecucion

La interfaz la hicimos con Streamlit. Hay que instalarlo una vez:

```
pip install -r requirements.txt
```

Y para correr la app final:

```
python -m streamlit run app.py
```

Se abre solo en el localhost.

Archivos:
- `rsa.py`: toda la parte de matematica y validaciones
- `app.py`: la interfaz

## Uso

Hay dos pestañas.

**Encriptar:** llenar Mensaje M, p, q y e y darle a "Encriptar". Abajo sale el cifrado C, la longitud L y el detalle: n, phi, L, si hubo relleno, cada caracter con su ASCII, los bloques m y c, y la llave publica (e, n).

**Desencriptar:** copiar C (bloques de 6 digitos separados por espacio) y L de la otra pestaña, poner p, q y e y darle a "Desencriptar". Sale el mensaje M y el detalle: n, phi, d, y cada bloque c con su m y sus caracteres.

Si algun dato esta mal sale el error en un cuadro rojo.

## Algoritmos (en rsa.py)

- `es_primo`: primalidad de p y q
- `mcd`: maximo comun divisor (Euclides)
- `inverso`: inverso modular con Euclides extendido, para sacar d
- `exp_mod`: exponenciacion modular (elevar al cuadrado y multiplicar, reduciendo mod n en cada paso)

## Comprobaciones realizadas

Se probo que se recupera exacto el mensaje con longitud par e impar, mayusculas y minusculas, numeros y signos, espacios seguidos y espacios al inicio y al final, con varios p, q, e.

Tambien se probo que da error con: p o q no primos, p = q, n fuera de rango, e = 1, e no coprimo con phi, e no entero, caracteres como ñ o tabulador, mensaje vacio, bloques de menos de 6 digitos o con letras, bloques mayores o iguales a n, L que no cuadra con los bloques, L no entero, y bloques que no dan ASCII validos.
