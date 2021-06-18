from datetime import datetime


def obter_limite(salario, idade):
      return int(salario * (idade / 1000)) + 100


def verificar_produto():
      nome_produto = str(input('\nDigite o nome do produtinho que você se interessou: '))
      preco_produto = float(input('Qual é o preço do produtinho? '))

      primeiro_nome = str(nome_completo.split()[0])
      caracteres_nome_completo = int(len(nome_completo))
      caracteres_primeiro_nome = int(len(primeiro_nome))
      print(primeiro_nome, caracteres_nome_completo, caracteres_primeiro_nome)

      if caracteres_nome_completo < preco_produto < idade_usuario:

            # Desconto em % e considerando o nome do cliente, conforme comentado na aula online
            desconto = float(preco_produto * (caracteres_primeiro_nome / 100))
            percentual_desconto = caracteres_primeiro_nome

            # Desconto máximo de 15%, para evitar que o cliente receba desconto ilimitado, caso insira o nome
            # e sobrenome sem espaços e ano de nascimento muito antigo
            if percentual_desconto > 15:
                  desconto = float(0.15 * preco_produto)
                  percentual_desconto = 15

            novo_preco_produto = float(preco_produto - desconto)

            print('\nParabéns! Você ganhou o desconto de', percentual_desconto, '%,', 'no valor de R$ %.2f' % desconto)
            print('O valor do produtinho com o desconto é: R$ %.2f' % novo_preco_produto, '.')

            return novo_preco_produto

      return preco_produto


# Validação de limite disponível para o cliente continuar comprando
def limite_disponivel():
      if limite_de_gasto >= (limite_de_gasto - valor_total_compra):
            limite_disponivel = limite_de_gasto - valor_total_compra

            print('Seu limite disponível é: R$ %.2f ' %limite_disponivel)
            print('Valor atual da compra é: R$ %.2f ' %valor_total_compra)

            return True

      else:
            print('Limite indisponível para compra.')
            print('Seu limite disponível é: R$ %.2f ' %limite_de_gasto)
            print('Valor total da compra é: R$ %.2f ' %valor_total_compra)

            return False

# Saudação e informações do cliente
print('\n\tSeja bem-vindo (a) à Loja Incriveland! \n\tAqui quem fala é Everlyn Borges de Oliveira.')
print('\nVamos fazer uma rápida análise de crédito para você começar a comprar conosco. '
      '\nPara isso, vou precisar de algumas informações, ok?!')

nome_completo = str(input('\nQual é o seu nome completo? '))

hoje = datetime.now()
ano_atual = int(hoje.strftime('%Y'))
ano_nascimento = int(input('Em que ano você nasceu? '))

if ano_nascimento > ano_atual:
      print('O ano de nascimento não pode ser superior ao ano atual. Por favor, preencha o ano novamente.')
      exit()

idade_usuario = int(ano_atual - ano_nascimento)

cargo_empresa = str(input('\nNo momento, qual cargo você ocupa na empresa em que trabalha? '))
salario_empresa = float(input('Qual é o seu salário médio mensal? '))

if salario_empresa <= 0:
      print('O salário deve ser maior que zero.')
      exit()

print('Cargo: ', cargo_empresa, ', Salário: ', salario_empresa, ', Ano de nascimento: ', ano_nascimento)
print('\nIdade: ', idade_usuario)

# Limite de crédito e quantidade de produtos
limite_de_gasto = obter_limite(salario_empresa, idade_usuario)
print('\nLimite de crédito disponível R$ %.2f ' %limite_de_gasto)

quantidade_de_produtos = int(input('\nQuantos produtinhos você quer levar? '))
valor_total_compra = 0


for produto in range(quantidade_de_produtos):
      valor_total_compra += verificar_produto()
      liberado_novo_produto = limite_disponivel()

      #Proteção para o cliente não comprar produtos além do limite de crédito
      if liberado_novo_produto == False:
            break


print('\nVerificando liberação...')

if valor_total_compra <= (0.6 * limite_de_gasto):
      print('\nLiberado!')
      print('Valor total da compra: R$ %.2f ' %valor_total_compra)
elif valor_total_compra <= (0.9 * limite_de_gasto):
      print('\nLiberado ao parcelar em até 2 vezes')
      print('Valor total da compra: R$ %.2f ' %valor_total_compra)
elif valor_total_compra <= limite_de_gasto:
      print('\nLiberado ao parcelar em 3 ou mais vezes')
      print('Valor total da compra: R$ %.2f ' %valor_total_compra)
else:
      print('\nBloqueado. Não foi dessa vez :(')