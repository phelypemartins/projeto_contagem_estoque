#Definição de variáveis/interação com usuário   

nome_produto = input('Digite o nome do produto: ')
categoria = input('Digite a categoria: ')
quantidade_atual = input('Digite a quantidade atual: ')

#Definição do estoque mínimo

estoque_alimentos = 50
estoque_bebidas = 75
estoque_limpeza = 30

#Nesse bloco, foi desenvolvido um programa para retornar ao usuário, qual a quantidade disponível em estoque. Também acrescentei ao bloco de código, sistema de verificação, onde o usuário deve digitar a categoria correta para ter acesso a quantidade.

if nome_produto and categoria and quantidade_atual:
    
    quantidade_atual = int(quantidade_atual)

    if categoria == 'Bebidas':
        if quantidade_atual < estoque_bebidas:
            estoque_negativo = estoque_bebidas - quantidade_atual
            print(f'{estoque_negativo} em estoque.')
        else:
            print('Estoque está cheio')
    elif categoria == 'Alimentos':
        if quantidade_atual < estoque_alimentos:
            estoque_negativo = estoque_alimentos - quantidade_atual
            print(f'{estoque_negativo} em estoque.')
        else:
            print('Estoque está cheio')
    elif categoria == 'Limpeza':   
        if quantidade_atual < estoque_limpeza:
            estoque_negativo = estoque_limpeza - quantidade_atual
            print(f'{estoque_negativo} em estoque.')
        else:
            print('Estoque está cheio')     


else:
    print('Preencha todas as informações')
