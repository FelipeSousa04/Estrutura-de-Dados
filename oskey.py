#Usa [] Colchetes
#As listas são mutáveis, porem mais lentas ao serem processadas as vezes não aparenta,
#mas em relação a tuplas elas são mais lentas, e listas são organizadas, podem ser adicionados novos conteudos dentro e removidos






#Criando uma Lista:
Lista_pares = [2, 4, 6, 8, 10, 12]
print(Lista_pares)
#Alterando Elementos da Lista:
Lista_pares[0]= 3
print(Lista_pares)
#Acessando Elementos da Lista:
Lista_pares = [2, 4, 6, 8, 10, 12]
print(Lista_pares[0])  # Acessa o primeiro elemento (índice 0)
print(Lista_pares[-1])  # Acessa o último elemento (índice -1)
#Adicionando conteudo
Lista_pares= [2, 4, 6, 8, 10, 12]
Lista_pares.append(14)  # Adiciona o número 14 ao final da lista
print(Lista_pares)
#Removendo Elementos da Lista:
Lista_pares = [2, 4, 6, 8, 10, 12]
Lista_pares.pop(2)  # Remove o elemento no índice 2 (6)
print(Lista_pares)
#verificando conteudo
Lista_pares = [2, 4, 6, 8, 10, 12]
if 2 in Lista_pares:
    print("O número 2 está na lista.")
else:
    print("O número 2 não está na lista.")


#TUPLAS: Trabalhada com parênteses, não mutáveis e nao organizaveis, mais rapida que listas Usa () parenteses

dias_das_semanas= ('segunda', 'terça' ,'quarta', 'quinta', 'sexta','sabado','domingo') 
print(dias_das_semanas[0]) 


#sets/conjuntos: Nao permite valor duplicado, são processados rapidez. Usa ([]) Parenteses e colchetes

Lista_Mercado= set(['Cebola','Alface','tomate','Cebola'])
print(Lista_Mercado)
Lista_Mercado.add('Carne moida')
print(Lista_Mercado)
if 'Cebola' in Lista_Mercado:
    print ("Cebola está contida")
else: 
    print ('Não tem cebola na lista')

Lista_1ano_de_namoro= set(['Pousada','almoçar na praia','lanchar porcaria','ver um filminho','jantar sushi na praia', 'Pousada'])
print(Lista_1ano_de_namoro)
if 'sexo' in Lista_1ano_de_namoro:
    print('Está Fudendo')
else:
    print('Não ta metendo')
Lista_1ano_de_namoro.add('sexo')
print(Lista_1ano_de_namoro)
if 'sexo' in Lista_1ano_de_namoro:
    print('Ta metendo pra krl e indo dentro')
else:
    print('Não ta metendo ta dando uma de cabaço')

#DICIONARIOS: DIFERENTE de todos os outros mencionados , possui entradas para melhor identificação e busca de um conteúdo . Usam {} (Chaves)
telefones= {'Felipe': '98988877050', 'Amanda':'98996171772'}
if 'Felipe' in telefones:
    print('O Gostoso pirocudo Está Nos contatos KARALHO! pega o numero dele rapariga')
else:print('infelizmente o delicia não está')
print(telefones['Felipe'])
