#FELIZ-NATAL

# Natal com Python
# estrela da árvore
print('☆'.center(20))#center(int) para centralizar a estrela
# construindo a árvore
for i in range(1, 20, 2):
    print(('*'*i).center(20))
# tronco da árvore
for r in range(2):
    print(('||').center(19))
# base da árvore
print('\====/'.center(19))
print()
# mensagem final
print('O importante é não parar de questionar; a curiosidade tem sua própria razão de existir, FELIZ NATAL.',end='\n\n')
