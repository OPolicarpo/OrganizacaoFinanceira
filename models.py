class Movimentacao:
    def __init__(self, valor, descricao, categoria, tipo, data=0):
        self.valor = valor
        self.descricao = descricao.upper()
        self.categoria = categoria.upper()
        self.tipo = tipo.upper()
        self.data = data

    def exibir(self):
        print(f' Foi feito {self.tipo} do item {self.descricao} na categoria {self.categoria} na data {self.data} no valor de {self.valor:,.2f}')


class Caixa:
    # Representa um caixa (pessoal ou trabalho), com nome, saldo inicial 
    # e uma lista de movimentações que será preenchida aos poucos
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial
        self.movimentacoes = []

    # aqui acrescentamos cada movimentacao para nossa lista
    def adc_movimentacao(self, mov):
        self.movimentacoes.append(mov)

    def calcular_saldo(self):
        # agora vamos separar o que entra e o que sai
        saldo = self.saldo_inicial
        for mov in self.movimentacoes:
            if mov.tipo == "ENTRADA":
                saldo += mov.valor
            else:
                saldo -= mov.valor
        return saldo

    def listar_extrato(self):
        # aqui vamos gerar o extrato bancario, como aquele papel impresso que sai do banco
        for mov in self.movimentacoes:
            mov.exibir()

    def calcular_investimento(self):
        # aqui vejo o que investi durante o mes
        investimento = 0
        for mov in self.movimentacoes:
            if mov.categoria == "INVESTIMENTO":
                investimento += mov.valor
        return investimento


caixa_pessoal = Caixa("Policarpo", 1000)

a1 = Movimentacao(valor=120, descricao="Manutenção de celular", categoria="servico", tipo="entrada", data='01/09')
caixa_pessoal.adc_movimentacao(a1)

a2 = Movimentacao(valor=550, descricao="Aluguel Loja", categoria="Despesa fixa loja", tipo="saida", data="10/09")
caixa_pessoal.adc_movimentacao(a2)

a3 = Movimentacao(valor=300, descricao="compra de tela", categoria="investimento", tipo="saida", data="05/09")
caixa_pessoal.adc_movimentacao(a3)

# aqui estamos testando o caixa trabalho

caixa_trabalho = Caixa("Trabalho", 1000)

b1 = Movimentacao(valor=280, descricao="Man cell", categoria="servico", tipo="entrada", data="09/09")
caixa_trabalho.adc_movimentacao(b1)

b2 = Movimentacao(valor=200, descricao="conta de luz", categoria="despesa fixa variavel", tipo="saida", data="09/09")
caixa_trabalho.adc_movimentacao(b2)

print(caixa_pessoal.calcular_saldo())
print()
print(caixa_pessoal.calcular_investimento())
caixa_pessoal.listar_extrato()

print('=-' * 50)
print(caixa_trabalho.calcular_saldo())
caixa_trabalho.listar_extrato()