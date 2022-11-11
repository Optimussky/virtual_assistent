# Programa que permite agregar cadena de texto a un archivo de imagen
with open('cat.jpg','rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex(''))
    #print(offset)

    last=[]
    #last=f.seek(offset)
    f.seek(offset)
    last= f.read()
    #print(f.read())
    
    print(b'Este es el ultimo elemento: %b',last)
    
