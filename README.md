# Evoloop Finanças

Sistema simples de controle financeiro, trazendo facilidade no uso e mobilidade — permitindo acompanhar suas finanças de qualquer local e a qualquer momento.

## Objetivo / Motivação

Terminei o Mundo 4 de Python do curso do Gustavo Guanabara (Programação Orientada a Objetos) e decidi colocar em prática o que aprendi, aplicando os conceitos num problema real, em vez de deixar como só mais uma informação teórica.

Além do aprendizado, esse projeto resolve uma dor pessoal: hoje uso uma planilha básica de Excel para controlar minhas finanças, e quero substituir isso por um sistema próprio.

## Funcionalidades atuais

> ⚠️ Projeto em desenvolvimento — hoje funciona apenas via código/terminal, sem interface gráfica.

- **Cadastro**: criação de movimentações financeiras (entradas e saídas) diretamente no código
- **Cálculo**: soma de entradas, saídas e total investido, com saldo final do caixa
- **Visualização**: extrato das movimentações registradas, exibido no terminal

## Tecnologias usadas

- **Python 3**
- [**rich**](https://github.com/Textualize/rich) — biblioteca usada para formatação colorida no terminal

## Arquitetura — as classes

O projeto é modelado em torno de duas classes principais, que representam o domínio do problema (controle financeiro):

### `Movimentacao`

Representa um único evento financeiro (uma entrada ou uma saída).

**Atributos**

| Atributo | Tipo | Descrição |
|---|---|---|
| `valor` | `float` | quantia da movimentação |
| `data` | `str` | quando aconteceu |
| `descricao` | `str` | texto livre, ex: "IFOOD SEXTA" |
| `categoria` | `str` | ex: "LAZER", "CONTA FIXA", "INVESTIMENTO" |
| `tipo` | `str` | `"ENTRADA"` ou `"SAIDA"` — define o efeito no caixa |

**Métodos**

| Método | O que faz |
|---|---|
| `exibir()` | mostra os dados formatados (data, categoria, descrição, valor) |

### `Caixa`

Representa um caixa (Pessoal ou Trabalho), responsável por guardar e somar as movimentações.

**Atributos**

| Atributo | Tipo | Descrição |
|---|---|---|
| `nome` | `str` | "Pessoal" ou "Trabalho" |
| `saldo_inicial` | `float` | valor que inicia o caixa no mês |
| `movimentacoes` | `list` | lista de objetos `Movimentacao` |

**Métodos**

| Método | O que faz |
|---|---|
| `adc_movimentacao(mov)` | recebe uma `Movimentacao` e guarda na lista |
| `calcular_saldo()` | retorna `saldo_inicial` + soma de entradas − soma de saídas |
| `listar_extrato()` | exibe todas as movimentações registradas nesse caixa |
| `calcular_investimento()` | soma o valor das movimentações com categoria `"INVESTIMENTO"` |

## Como rodar o projeto

```bash
# 1. Tenha o Python 3 instalado
python --version

# 2. Instale a dependência do projeto
pip install rich

# 3. Rode o arquivo principal
python models.py
```

## Próximos passos

- [ ] Criar e testar o segundo `Caixa` ("Trabalho"), validando os dois funcionando lado a lado
- [ ] Persistir os dados (hoje tudo é perdido ao fechar o terminal — salvar em arquivo ou banco de dados)
- [ ] Criar interface web com Flask, conectando as classes já existentes a rotas e páginas HTML
- [ ] Criar formulários (Jinja2/HTML) para cadastro de movimentações pela web
- [ ] Revisar padronização de texto (`.upper()`) em todos os campos comparados pelo sistema
- [ ] Adicionar testes automatizados para `Movimentacao` e `Caixa`

---

*Projeto pessoal de estudo, feito para fixar conceitos de Programação Orientada a Objetos em Python.*
