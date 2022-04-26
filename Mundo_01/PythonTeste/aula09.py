# frase = 'Curso em Vídeo Python'
# print(frase[3])
# print(frase[3:13])
# print(frase[:13])
# print(frase[13:])
# print(frase[1:15])
# print(frase[1:15:2])
# print(frase[1::2])
# print(frase[::2])
#
# print("""Welcome! Are you completely new to programming?
# If not then we presume you will be looking for information about why and how
# to get started with Python. Fortunately an experienced programmer
# in any programming language (whatever it may be)
# can pick up Python very quickly.
# It's also easy for beginners to use and learn, so jump in!""")

frase = 'Curso em Vídeo Python'
# print(frase.count('o'))
# print(frase.upper().count('O'))
# frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[2][3])
