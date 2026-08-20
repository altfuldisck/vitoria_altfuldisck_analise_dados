# ============================================================================
# 1. VARIÁVEIS — EXERCÍCIOS 1 A 10
# ============================================================================

# Exercício 1 — Dados pessoais
nome = "Carlos"
idade = 25
altura = 1.75
is_estudante = True

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(is_estudante, type(is_estudante))

# Exercício 2 — Saudação
nome_user = input("Digite seu nome: ")
cidade_user = input("Digite sua cidade: ")
print(f"Olá, {nome_user}! Você mora em {cidade_user}.")

# Exercício 3 — Soma de dois números
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print(f"A soma é: {num1 + num2}")

# Exercício 4 — Operações básicas
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(f"Soma: {n1 + n2}")
print(f"Subtração: {n1 - n2}")
print(f"Multiplicação: {n1 * n2}")
print(f"Divisão: {n1 / n2}")

# Exercício 5 — Média de três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")

# Exercício 6 — Idade no futuro
idade_atual = int(input("Digite sua idade atual: "))
print(f"Daqui a 10 anos você terá {idade_atual + 10} anos.")

# Exercício 7 — Conversão de temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperatura em Fahrenheit: {fahrenheit:.1f}°F")

# Exercício 8 — Área de um retângulo
largura = float(input("Digite a largura do retângulo: "))
altura_ret = float(input("Digite a altura do retângulo: "))
area = largura * altura_ret
print(f"A área do retângulo é: {area}")

# Exercício 9 — Manipulação de texto
frase = input("Digite uma frase: ")
print(f"a) Maiúsculas: {frase.upper()}")
print(f"b) Minúsculas: {frase.lower()}")
print(f"c) Quantidade de caracteres: {len(frase)}")

# Exercício 10 — Preço com desconto
prod_nome = input("Nome do produto: ")
prod_preco = float(input("Preço do produto: R$ "))
prod_desc_perc = float(input("Percentual de desconto (%): "))

valor_desconto = prod_preco * (prod_desc_perc / 100)
preco_final = prod_preco - valor_desconto

print(f"Produto: {prod_nome}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")


# ============================================================================
# 2. ESTRUTURA CONDICIONAL — EXERCÍCIOS 11 A 20
# ============================================================================

# Exercício 11 — Positivo, negativo ou zero
numero_11 = float(input("Digite um número: "))
if numero_11 > 0:
    print("O número é positivo.")
elif numero_11 < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")

# Exercício 12 — Par ou ímpar
numero_12 = int(input("Digite um número inteiro: "))
if numero_12 % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Exercício 13 — Aprovação
media_13 = float(input("Digite a média do aluno: "))
if media_13 >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

# Exercício 14 — Aprovação com recuperação
media_14 = float(input("Digite a média do aluno: "))
if media_14 >= 7.0:
    print("Aprovado")
elif 5.0 <= media_14 < 7.0:
    print("Recuperação")
else:
    print("Reprovado")

# Exercício 15 — Maior entre dois números
num_a = float(input("Digite o primeiro número: "))
num_b = float(input("Digite o segundo número: "))
if num_a > num_b:
    print(f"O maior número é {num_a}.")
elif num_b > num_a:
    print(f"O maior número é {num_b}.")
else:
    print("Os dois números são iguais.")

# Exercício 16 — Faixa etária
idade_pessoa = int(input("Digite a idade: "))
if idade_pessoa <= 11:
    print("Criança")
elif idade_pessoa <= 17:
    print("Adolescente")
elif idade_pessoa <= 59:
    print("Adulto")
else:
    print("Idoso")

# Exercício 17 — Desconto na compra
valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 100.0:
    valor_compra *= 0.90
print(f"Total a pagar: R$ {valor_compra:.2f}")

# Exercício 18 — Acesso ao sistema
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

# Exercício 19 — Número dentro do intervalo
num_19 = float(input("Digite um número: "))
if num_19 >= 10 and num_19 <= 50:
    print("O número está entre 10 e 50.")
else:
    print("O número está fora do intervalo de 10 a 50.")

# Exercício 20 — Calculadora simples
n_calc1 = float(input("Digite o primeiro número: "))
n_calc2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, * ou /): ")

if operacao == "+":
    print(f"Resultado: {n_calc1 + n_calc2}")
elif operacao == "-":
    print(f"Resultado: {n_calc1 - n_calc2}")
elif operacao == "*":
    print(f"Resultado: {n_calc1 * n_calc2}")
elif operacao == "/":
    if n_calc2 != 0:
        print(f"Resultado: {n_calc1 / n_calc2}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")


# ============================================================================
# 3. LISTAS — EXERCÍCIOS 21 A 30
# ============================================================================

# Exercício 21 — Criando uma lista
frutas_21 = ["maçã", "banana", "laranja", "uva"]
print(frutas_21)

# Exercício 22 — Acessando elementos
cores = ["azul", "verde", "amarelo", "vermelho"]
print(f"Primeiro elemento: {cores[0]}")
print(f"Último elemento: {cores[-1]}")

# Exercício 23 — Adicionando elementos
nomes = ["Ana", "Bruno", "Carla"]
novo_nome = input("Digite outro nome: ")
nomes.append(novo_nome)
print(nomes)

# Exercício 24 — Removendo elementos
frutas_24 = ["maçã", "banana", "laranja", "uva"]
frutas_24.remove("banana")
print(frutas_24)

# Exercício 25 — Alterando um elemento
frutas_25 = ["maçã", "banana", "laranja", "uva"]
frutas_25[2] = "abacaxi"
print(frutas_25)

# Exercício 26 — Tamanho e presença
numeros_26 = [10, 20, 30, 40, 50]
print(f"Quantidade de elementos: {len(numeros_26)}")
print(f"O número 30 pertence à lista? {30 in numeros_26}")

# Exercício 27 — Soma, maior e menor
valores_27 = [12, 5, 28, 9, 17]
print(f"Soma: {sum(valores_27)}")
print(f"Maior valor: {max(valores_27)}")
print(f"Menor valor: {min(valores_27)}")

# Exercício 28 — Ordenação
cidades = ["Curitiba", "Salvador", "Recife", "Goiânia", "Manaus"]
cidades.sort()
print(cidades)

# Exercício 29 — Concatenação
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# Exercício 30 — Fatiamento
numeros_30 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"a) Três primeiros: {numeros_30[:3]}")
print(f"b) Três últimos: {numeros_30[-3:]}")
print(f"c) Do índice 2 ao 5: {numeros_30[2:6]}")


# ============================================================================
# 4. ESTRUTURAS DE REPETIÇÃO — EXERCÍCIOS 31 A 40
# ============================================================================

# Exercício 31 — Números de 1 a 10
for i in range(1, 11):
    print(i)

# Exercício 32 — Números pares
for i in range(2, 21, 2):
    print(i)

# Exercício 33 — Percorrendo nomes
nomes_33 = ["Ana", "Bruno", "Carla", "Diego"]
for nome in nomes_33:
    print(nome)

# Exercício 34 — Quadrados
numeros_34 = [1, 2, 3, 4, 5]
quadrados = []
for n in numeros_34:
    quadrados.append(n ** 2)
print(quadrados)

# Exercício 35 — Soma com for
valores_35 = [10, 20, 30, 40, 50]
soma_acumulada = 0
for v in valores_35:
    soma_acumulada += v
print(f"Soma acumulada: {soma_acumulada}")

# Exercício 36 — Contando aprovados
notas_36 = [8.0, 5.5, 7.0, 9.2, 4.0, 6.8]
aprovados = 0
for nota in notas_36:
    if nota >= 7.0:
        aprovados += 1
print(f"Quantidade de aprovados: {aprovados}")

# Exercício 37 — Contagem com while
contador_37 = 1
while contador_37 <= 10:
    print(contador_37)
    contador_37 += 1

# Exercício 38 — Contagem regressiva
contador_38 = 10
while contador_38 >= 1:
    print(contador_38)
    contador_38 -= 1
print("Fim!")

# Exercício 39 — Senha correta
senha_digitada = input("Digite a senha: ")
while senha_digitada != "python123":
    senha_digitada = input("Senha incorreta. Digite novamente: ")
print("Acesso liberado!")

# Exercício 40 — Somando até zero
soma_zero = 0
num_zero = int(input("Digite um número (0 para sair): "))
while num_zero != 0:
    soma_zero += num_zero
    num_zero = int(input("Digite outro número (0 para sair): "))
print(f"A soma de todos os valores digitados é: {soma_zero}")


# ============================================================================
# 5. DICIONÁRIOS — EXERCÍCIOS 41 A 50
# ============================================================================

# Exercício 41 — Criando um dicionário
aluno = {
    "nome": "Lucas",
    "idade": 22,
    "curso": "Engenharia de Software"
}
print(aluno)

# Exercício 42 — Acessando valores
produto_42 = {"nome": "Teclado", "preco": 150.0, "estoque": 8}
print(f"Nome: {produto_42['nome']}")
print(f"Preço: R$ {produto_42['preco']}")

# Exercício 43 — Adicionando uma chave
produto_43 = {"nome": "Mouse", "preco": 80.0}
produto_43["marca"] = "Logitech"
print(produto_43)

# Exercício 44 — Atualizando um valor
produto_44 = {"nome": "Monitor", "preco": 900.0, "estoque": 5}
produto_44["estoque"] = 15
print(produto_44)

# Exercício 45 — Removendo uma chave
carro = {"marca": "Ford", "modelo": "Ka", "ano": 2020, "cor": "prata"}
carro.pop("cor")
print(carro)

# Exercício 46 — Verificando uma chave
contato = {"nome": "Marina", "email": "marina@email.com"}
if "telefone" in contato:
    print("A chave 'telefone' existe no dicionário.")
else:
    print("A chave 'telefone' NÃO existe no dicionário.")

# Exercício 47 — Chaves e valores
capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}
print(f"Chaves: {list(capitais.keys())}") #print(capitais.keys())
print(f"Valores: {list(capitais.values())}") #print(capitais.values())

# Exercício 48 — Percorrendo um dicionário
produtos_48 = {"caderno": 25.0, "caneta": 4.5, "mochila": 120.0}
for item, preco in produtos_48.items(): #for itens in produtos.items()
    print(f"Produto: {item} | Preço: R$ {preco:.2f}")#print(chave) e print(valor)

# Exercício 49 — Soma dos valores
estoque = {"notebook": 5, "mouse": 20, "teclado": 12, "monitor": 4}
total_estoque = sum(estoque.values())
print(f"Total de itens no estoque: {total_estoque}")

# Exercício 50 — Frequência de palavras
palavras = ["python", "dados", "python", "lista", "dados", "python"]
frequencia = {}

for p in palavras:
    if p in frequencia:
        frequencia[p] += 1
    else:
        frequencia[p] = 1

print(frequencia)