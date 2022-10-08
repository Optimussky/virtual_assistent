# Programa que permite agregar cadena de texto a un archivo de imagen
with open('cat.jpg','rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex(''))
    #print(offset)

    f.seek(offset + 2)
    print(f.read())
