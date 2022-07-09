#Faça um programa que leia uma frase pelo teclado e mostre:
frase =str(input('Digite uma frase:')).strip().upper()
print('Quantas vezes aparece a letra "A":', frase.count('A'))
print('Aparece a primeira vez na posição:', frase.find('A')+1)
print('Aparece a última vez na posição:', frase.rfind('A')+1)