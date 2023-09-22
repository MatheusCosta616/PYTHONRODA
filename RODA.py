# RM98831 Henrique de Brito Costa

# RM99482 Pedro Zilves Hissa Quaresma Romão

# RM551157 Matheus José

# RM99279 João Paulo Fonseca Zamperlini

import csv
import random

with open('d:/roda.txt', 'w') as f:
    opcoes_roda = ['50', '100', '150', '200', '250', '300', '350', '500', '550', '600', '650', '700', '750', '800', '850', '900', '950', '1000', 'Aposta Tudo']
    f.write(','.join(opcoes_roda))

palavras = ['COMPUTADOR', 'PROGRAMAR', 'MICROSOFT']
with open('d:/palavras.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(palavras)

jogadores = [input(f"Nome do jogador {i + 1}: ") for i in range(3)]
pontuacoes = [0, 0, 0]
rodada = 0

print("Dica: Ferramentas de um Desenvolvedor de Software")


letras_adivinhadas = [set() for _ in palavras]
letras_mencionadas = set()

while True:
    jogador_atual = rodada % 3
    print(f"É a vez de {jogadores[jogador_atual]}, rodar a roda!")
    input("Pressione enter para rodar a roda...")

    valor_roda = random.choice(opcoes_roda)
    print(f"A roda parou em: {valor_roda}")

    while True:
        escolha = input("Escolha uma letra ou digite uma palavra: ").upper()
        if len(escolha) == 1:
            letra = escolha
            if letra in letras_mencionadas:
                print("Entrada inválida ou letra já mencionada, tente novamente.")
            else:
                letras_mencionadas.add(letra)
                total_letras = sum(palavra.count(letra) for palavra in palavras)
                if total_letras > 0:
                    if valor_roda == 'Aposta Tudo':
                        pontuacoes[jogador_atual] *= 2
                        print(f"Boa escolha! Você dobrou seus pontos.")
                    else:
                        pontuacoes[jogador_atual] += total_letras * int(valor_roda)
                        print(f"Boa escolha! Você ganhou {total_letras * int(valor_roda)} pontos.")

                    for i in range(len(palavras)):
                        if letra in palavras[i]:
                            letras_adivinhadas[i].add(letra)
                else:
                    if valor_roda == 'Aposta Tudo':
                        print("Que pena! Você perdeu todos os seus pontos.")
                        pontuacoes[jogador_atual] = 0
                    else:
                        print("Que pena! Não há essa letra nas palavras.")
                break
        elif len(escolha) > 1:
            palpite = escolha
            if palpite in palavras:
                print(f"Parabéns {jogadores[jogador_atual]}, você acertou a palavra {palpite}!")
                for i in range(len(palavras)):
                    if palavras[i] == palpite:
                        pontos = len(palavras[i]) - len(letras_adivinhadas[i])
                        pontuacoes[jogador_atual] += pontos * int(valor_roda)
                        letras_adivinhadas[i].update(palpite)
                break
            else:
                print(f"Palpite errado! Você digitou {palpite}.")
                break
        else:
            print("Entrada inválida. Por favor, digite uma letra ou uma palavra completa.")

    for i in range(len(palavras)):
        palavra_mostrada = ' '.join([letra if letra in letras_adivinhadas[i] else '_' for letra in palavras[i]])
        print(f"Palavra {i + 1}: {palavra_mostrada}")

    for i in range(len(jogadores)):
        print(f"Pontuação de {jogadores[i]}: {pontuacoes[i]}")

    letras_restantes = sum(len(palavras[i]) - len(letras_adivinhadas[i]) for i in range(len(palavras)))
    if letras_restantes == 0:
        print("Todas as palavras foram adivinhadas! Fim de jogo.")
        break

    rodada += 1
