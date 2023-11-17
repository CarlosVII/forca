from palavras import *
import random

palavra = random.choice(palavras).lower()
letrasU = []
chances = 6
acertos = 0
corpo = [
'''
+------+
|      |
|
|
|
|
|
==========''',
'''
+------+
|      |
|      O
|
|
|
|
==========''',
'''
+------+
|      |
|      O
|      | 
|
|
|
==========''',
'''
+------+
|      |
|      O
|      |\ 
|
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|       \_
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|    _/ \_
|
|
=========='''
]

print ('')
print(f'A palavra tem {len(palavra)} Letras\ne você tem  {chances} tentativas de acerto. ')
print('')
print('-=' * 20)

while chances > 0:

    for letra in palavra:
        if letra.lower() in letrasU:
            print(letra, end=' ')
        else:
            print(' _ ', end='')
    print('')

    print('-=' * 20)
       
    
    if chances == 6:
        print(corpo[0])
    elif chances == 5:
        print(corpo[1])
    elif chances == 4:
        print(corpo[2])
    elif chances == 3:
        print(corpo[3])
    elif chances == 2:
        print(corpo[4])
    elif chances == 1:
        print(corpo[5])
        
    print('')
    if chances >=2:
        print(f'Você tem {chances} tentativas.')
    else:
        print('-='*20)
        print(f'Você tem {chances} tentativa.')
    print('')
    tentativa = (input("Escolha uma letra: "))
    
    letrasU.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
            chances -= 1

    






    if acertos == (len(palavra)):
        print("ganhou", palavra)
    elif chances == 0:
        print (corpo[6])
        print('')
        print (f'FIM DE JOGO, você perdeu, a palavra era: {palavra}')
        print("kkk")