import re 

# findall search sub
# compile , serve para compilar uma expressao regular antes de us-la e reutilizar ela mais vezes

string = 'Este é um teste de expressões regulares.'
# o 'r' é importante para que não seja necassario o uso de barras invertidas
#search serve para mostrar aonde esta tal texto desejado
#findall serve para mostrar todos os textos desejados
#sub serve para substituir o texto desejado por outro texto
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','EUAMOPEITOS', string))

teste_de_compile = re.compile (r'teste')
print (teste_de_compile.search(string))
print (teste_de_compile.findall(string))
print (teste_de_compile.sub('EuAmoMinhaNaMORADA', string))
