# Evoloop Finanças

Sistema simples de controle financeiro, trazendo facilidade no uso e mobilidade — permitindo acompanhar suas finanças de qualquer local e a qualquer momento.

## Objetivo / Motivação

Terminei o Mundo 4 de Python do curso do Gustavo Guanabara (Programação Orientada a Objetos) e decidi colocar em prática o que aprendi, aplicando os conceitos num problema real, em vez de deixar como só mais uma informação teórica.

Além do aprendizado, esse projeto resolve uma dor pessoal: hoje uso uma planilha básica de Excel para controlar minhas finanças, e quero substituir isso por um sistema próprio.

## Funcionalidades atuais

> ⚠️ Projeto em desenvolvimento — hoje funciona via terminal, através de um menu interativo, sem interface gráfica ainda.

- **Cadastro**: adição de movimentações financeiras (entradas e saídas) pelo menu, informando valor, descrição, categoria, tipo e origem
- **Data automática**: cada movimentação registra a data do dia automaticamente, sem precisar ser digitada
- **Cálculo**: saldo geral, total gasto por origem (Pessoal/Trabalho) e total investido
- **Visualização**: extrato completo das movimentações registradas
- **Tratamento de erros**: o menu não trava se o usuário digitar uma opção inválida ou um valor não-numérico

## Tecnologias usadas

- **Python 3**
- `datetime` (biblioteca nativa do Python) — usada para capturar a data atual automaticamente

## Arquitetura — as classes

O projeto é modelado em torno de duas classes principais, que representam o domínio do problema (controle financeiro):

### `Movimentacao`

Representa um único evento financeiro (uma entrada ou uma saída), seja pessoal ou de trabalho.

**Atributos**

| Atributo | Tipo | Descrição |
|---|---|---|
| `valor` | `float` | quantia da movimentação |
| `data` | `str` | capturada automaticamente no momento do cadastro |
| `descricao` | `str` | texto livre, ex: "IFOOD SEXTA" |
| `categoria` | `str` | ex: "LAZER", "CONTA FIXA", "INVESTIMENTO" |
| `tipo` | `str` | `"ENTRADA"` ou `"SAIDA"` — define o efeito no saldo |
| `origem` | `str` | `"PESSOAL"` ou `"TRABALHO"` — de onde partiu a movimentação |

**Métodos**

| Método | O que faz |
|---|---|
| `exibir()` | mostra os dados formatados (tipo, descrição, categoria, data, valor, origem) |

### `Caixa`

Representa o caixa único do sistema (chamado "Geral"), responsável por guardar e somar todas as movimentações, sejam pessoais ou de trabalho.

> Nota de arquitetura: inicialmente o projeto tinha dois objetos `Caixa` separados (Pessoal e Trabalho). Essa abordagem foi revista: hoje existe um único saldo real (assim como acontece na prática — o dinheiro é um só), e a origem de cada gasto é apenas uma categorização dentro da `Movimentacao`, usada para gerar totais filtrados.

**Atributos**

| Atributo | Tipo | Descrição |
|---|---|---|
| `nome` | `str` | nome do caixa (hoje, sempre "Geral") |
| `saldo_inicial` | `float` | valor que inicia o caixa |
| `movimentacoes` | `list` | lista de objetos `Movimentacao` |

**Métodos**

| Método | O que faz |
|---|---|
| `adc_movimentacao(mov)` | recebe uma `Movimentacao` e guarda na lista |
| `calcular_saldo()` | retorna `saldo_inicial` + soma de entradas − soma de saídas (saldo real) |
| `listar_extrato()` | exibe todas as movimentações registradas |
| `calcular_investimento()` | soma o valor das movimentações com categoria `"INVESTIMENTO"` |
| `calcular_pessoal()` | soma o valor das movimentações com origem `"PESSOAL"` |
| `calcular_trabalho()` | soma o valor das movimentações com origem `"TRABALHO"` |

## Como rodar o projeto

```bash
# 1. Tenha o Python 3 instalado
python --version

# 2. Rode o menu interativo
python main.py
```

Ao rodar, um menu aparece no terminal com as opções: adicionar movimentação, ver saldo, ver extrato e sair.

> ⚠️ Os dados existem apenas durante a execução do programa — ao fechar o terminal, tudo é perdido. Persistência ainda não foi implementada (ver "Próximos passos").

## Próximos passos

- [x] Testar múltiplas movimentações com origens diferentes, validando os totais calculados
- [x] Criar menu interativo no terminal (`main.py`) para cadastro sem precisar editar código
- [x] Automatizar a captura da data
- [x] Tratar erros de entrada do usuário (opção inválida, valor não-numérico)
- [ ] Persistir os dados (arquivo ou banco de dados — atualmente em estudo via curso de SQL do Guanabara)
- [ ] Melhorar o tratamento de erro no cadastro para não perder os dados já digitados quando um campo falha
- [ ] Criar interface web com Flask, conectando as classes já existentes a rotas e páginas HTML
- [ ] Criar formulários (Jinja2/HTML) para cadastro de movimentações pela web
- [ ] Adicionar testes automatizados para `Movimentacao` e `Caixa`

---

*Projeto pessoal de estudo, feito para fixar conceitos de Programação Orientada a Objetos em Python.*
