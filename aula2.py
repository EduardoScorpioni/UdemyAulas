#Meta Caracteres ( continuação da aula 1)   . ^ $ * ? { } [ ] \ | ( ) + - = !
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|adultos', texto))
# Saída: ['João', 'Maria', 'adultos']  
# O comando re.findall() procura por todos os padrões especificados na string e retorna uma
print(re.findall(r'João|Maria|ad..tos', texto)) # O '.' Serve para dizer que pode entrar qualquer caracter neste valor desejado
print(re.findall(r'João|joão|Maria|adultos', texto))
print(re.findall(r'[Jj]oão|[a-zA-Z]aria', texto)) # O '[a-zA-Z]' Serve para dizer que pode entrar qualquer letra maiuscula ou minuscula
print(re.findall(r'jOãO|mAriA|aDuLtOs', texto, flags=re.I)) # este serve para dizer que não importa o caracter mas sim o seu resultado