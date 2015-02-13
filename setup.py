# coding: utf-8
from function import *

print "\033[32;1m" + "#" * 40 +"\033[0;0m"
print "\033[32;1m" + "#" + " " * 38 + "#" + "\033[0;0m"
print "\033[32;1m" + "#" + " " * 10 + "CODIGO SIMPLES RSA" + " " * 10 + "#" +"\033[0;0m"
print "\033[32;1m" + "#" + " " * 38 + "#" + "\033[0;0m"
print "\033[32;1m" + "#" * 40 + "\033[0;0m"

try:
    chavePublica = raw_input("\033[32;1m"+"CHAVE PUBLICA: "+"\033[0;0m").split()
    
    n = int(chavePublica[0])
    e = int(chavePublica[1])
    p = int(calculaFatoresPeQ(n)[0])
    q = int(calculaFatoresPeQ(n)[1])
    phi = calculaTotiente(p,q)
    d = euclides(e , phi , 1)
    
    mensagemCifrada = raw_input("\033[32;1m"+"MENSAGEM CIFRADA: "+"\033[0;0m").split()
    
    mensagemDescriptografada = descryptString(mensagemCifrada , d , n)
    mensagemOriginal = getString(mensagemDescriptografada)
    
    chavePrivada = "\nCHAVE PRIVADA: ( %d , %d )" % (n, d)
    
    print "\033[34;1m"+ chavePrivada +"\033[0;0m"
    print "\033[34;1m"+"MENSAGEM ORIGINAL : "+mensagemOriginal+'\033[0;0m'
	
except:
    print  '\033[31;1m'+'ERRO'+'\033[0;0m'

# 2845 437 489 3139 1081 1967 4813 5129 1081 3139 489 1397 3139 3886 3139 437 4921 4921 3139 5064 4813 3122 1081 3896 3139 1731 1081 3581 237 4813 5129 1081 3581
# 2845 437 489 3139 1081 1967 4813 5129 1081 3139 489 1397 3139 3886 3139 437 4921 4921 3139 5064 489 3581 4921 489 437 3581 3139 4813 437
