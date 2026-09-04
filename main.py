from models import *

meu_caixa = Caixa("Geral", 1000)

while True:
    print("[1] Adicionar movimentações")
    print("[2] Ver Saldo")
    print("[3] Ver Extrato")
    print("[4] Sair")
    try:
        decisao = int(input("Escolha sua opção: "))
    except: 
        print("Opcao invalida, digite novamente!")
        continue
    if decisao == 4:
        break
    if decisao == 1:
        origem =input("Digite a origem: ")
        descricao = input("Descreva o item: ")
        try:
            valor = float(input("Qual valor: "))
        except:
            print("Valor invalido, digite novamente")
            continue
        categoria = input("Qual categoria: ")
        tipo = input("Qual tipo: ")
        nova_mov = Movimentacao(valor=valor, descricao=descricao, categoria=categoria, tipo=tipo, origem=origem)
        meu_caixa.adc_movimentacao(nova_mov)
        print("=-"*20)
    if decisao == 2:
        print(f"Seu saldo é {meu_caixa.calcular_saldo():,.2f}")
        print('-'*20)
        print(f"Total Pessoal: R${meu_caixa.calcular_pessoal():,.2f}")
        print(f"Total Trabalho: R${meu_caixa.calcular_trabalho():,.2f}")
        print(f"Total Inestido: R${meu_caixa.calcular_investimento():,.2f}")
        print("=-"*20)
    if decisao == 3:
        meu_caixa.listar_extrato()
        print("=-"*20)
    else:
        print("Opcao invalida, digite novamente")
        