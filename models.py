#Esse será meu primeiro programa, onde vou utilizar para controle de caixa,
# a qual hoje utilizo uma planilia simples do excel

#Aqui começa nossa Classe Mãe onde vamos colher os dados de cada movimentacao

class Movimentacao:
    def __init__(self, valor, data, descricao,categoria, tipo):
        self.valor = valor
        self.data = data
        self.descricao = descricao.upper()
        self.categoria = categoria.upper()
        self.tipo = tipo.upper()

    
    def exibir(self):
        print(f' Foi feito {self.tipo} do item {self.descricao} na categoria {self.categoria} na data {self.data} no valor de {self.valor:,.2f}')


class Caixa:
    # Representa um caixa (pessoal ou trabalho), com nome, saldo inicial 
    # e uma lista de movimentações que será preenchida aos poucos
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial
        self.movimentacoes = []

    #aqui acrescentamos cada movimentacao para nossa lista
    def adc_movimentacao(self, mov):
        self.movimentacoes.append(mov)
    
    def calcular_saldo(self):
        #agora vamos separar o que entra e o que sai
        saldo = self.saldo_inicial
        for mov in self.movimentacoes:
            if mov.tipo == "ENTRADA":
                saldo += mov.valor
            else:
                saldo -= mov.valor
        return saldo

    def listar_extrato(self):
        #aqui vamos gerar o extrato bancario, como aquele papel impresso que sai do banco
        for mov in self.movimentacoes:
            mov.exibir()
    
    def calcular_investimento(self):
        #aqui vejo o que investi durante o mes
        investimento = 0
        for mov in self.movimentacoes:
            if mov.categoria == "INVESTIMENTO":
                investimento+= mov.valor
        return investimento
            







caixa_pessoal = Caixa("Policarpo", 1000)


a1 = Movimentacao(120, '01/09', "Manutenção de celular", "servico", "entrada" ) 

caixa_pessoal.adc_movimentacao(a1)

a2 = Movimentacao(550, "10/09", "Aluguel Loja", "Despesa fixa loja", "saida")

caixa_pessoal.adc_movimentacao(a2)

a3 = Movimentacao(300, "05/09", "compra de tela", "investimento", "saida")
caixa_pessoal.adc_movimentacao(a3)

print(caixa_pessoal.calcular_saldo())
print()
print(caixa_pessoal.calcular_investimento())
caixa_pessoal.listar_extrato()