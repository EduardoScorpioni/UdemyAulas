#Quantificadores ( continuação da aula 2)  
# # * 0 ou n ('n' é ilimitadas vezes)
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max} (repetições)
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+ 
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem""!
jão
'''

print(re.findall(r'jo+ão+', texto, flags=re.I)) # Encontra a palavra "joão" com 1 ou mais "o"
#print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.sub(r'jo+ão+','Felipe', texto, flags=re.I)) # Substitui a palavra "joão" com 1 ou mais "o"  por "Felipe"
#print(re.sub(r'jo*ão*','Felipe', texto, flags=re.I)) o * significa que pode ter zero ou mais "o" 
#print(re.sub(r'jo?ão+','Felipe', texto, flags=re.I)) o ? significa que pode ter 1 ou mais vezes
#print(re.sub(r'jo{1,}ão{1,}','Felipe', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I)) #dizendo pra ele encontrar uma quantidade especifica indicada a letra desajada, deixando na sair as palavras Veeemm e veeem

texto2 = 'João ama ser amado'
print(re.findall(r'ama[od]*', texto2, flags=re.I)) #o {2} significa que ele vai procurar as palabras desejadas, e o "*" serve para todos