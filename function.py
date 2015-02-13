# coding: utf-8

def calculaFatoresPeQ(num):
	fatotP = 0
	primeiro_primo = 2
	fatorQ = num
	while((primeiro_primo * primeiro_primo) <= fatorQ):
		if(fatorQ % primeiro_primo):
			primeiro_primo += 1
		else:
			fatorQ /= primeiro_primo
			fatorP = primeiro_primo	
	return fatorP, fatorQ		

def calculaTotiente(p,q):
        return (p -1) * (q - 1)
        
def euclides(e, phi, c):
    r = phi % e

    if r == 0:
        return (c / e) % (phi / e)
    if (euclides(r, e, -c) * phi + c) / (e % phi) < 0:
        return (calculaTotiente() + (euclides(r, e, -c) * phi + c)) / (e % phi)
    return (euclides(r, e, -c) * phi + c) / (e % phi)      
    

def encryptString(frase , e , n ):
    fraseASCII = []
    fraseEncrypt = []
    
    for letra in range(len(frase)):
        fraseASCII.append(ord(frase[letra].upper())+ 100) 
    
    for i in range(len(fraseASCII)):
        fraseEncrypt.append((fraseASCII[i]**e) % n)
    return fraseEncrypt

def descryptString(fraseEncrypt , d , n):
    fraseDescrypt = []
    for i in range(len(fraseEncrypt)):
        fraseDescrypt.append(int((int(fraseEncrypt[i])**d) % n))
    return fraseDescrypt

def getString(fraseDescrypt):
    frase = ""
    for i in range(len(fraseDescrypt)):
        frase += chr(fraseDescrypt[i] -100)
    return frase      
