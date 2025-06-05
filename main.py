# João Vitor: RM 563329 - Nicolas Baradel: RM 563245 - Patrick Correa: RM 564088

import random  # Importa o módulo para gerar números aleatórios
from hospital import hospital_mais_proximo  # Importa a função de localização de hospital

chamados = []  # Lista para armazenar os chamados feitos pelo usuário

# Mensagens iniciais do sistema
print("\nApluvi Alert")
print("Conectando dados à sua Segurança!")
print("---------------------------------")
print("Você está precisando de ajuda? A Apluvi vai encaminhar o seu chamado para Defesa Civil.")

# Loop principal do menu
while True:
    # Menu de opções
    print("\n[MENU ALERT]\n")
    print("1 - Preciso de ajuda! Realizar um Chamado.")
    print("2 - Status do Chamado")
    print("3 - Histórico de Chamados.")
    print("4 - Finalizar.\n")

    menu = input("Digite o número da opção:")

    # Escolha de ação conforme a opção digitada
    match menu:
        case "1":
            print("\nIniciando Chamado...\n")

            # Coleta e validação do nome
            while True:
                nome = input("Digite o nome completo da pessoa condutora:").strip()
                if nome:
                    break
                print("O nome não pode ser vazio.")

            # Coleta e validação da idade
            while True:
                try:
                    idade = int(input("Digite a idade da pessoa condutora:"))
                    if idade > 0:
                        break
                    else:
                        print("Digite uma idade válida.")
                except ValueError:
                    print("Digite um número válido para a idade.")

            # Coleta e validação do endereço
            while True:
                endereco = input("Informe o endereço (com adicionais) do local onde a ajuda é necessária:").strip()
                if endereco:
                    break
                print("O endereço não pode ser vazio.")

            # Coleta e validação da quantidade de pessoas
            while True:
                try:
                    pessoas = int(input("Digite a quantidade estimada de pessoas no local:"))
                    if pessoas > 0:
                        break
                    else:
                        print("Deve haver pelo menos uma pessoa.")
                except ValueError:
                    print("Digite um número válido.")

            # Coleta e validação de crianças e idosos
            while True:
                try:
                    criancas = int(input("Quantidade estimada de crianças:"))
                    idosos = int(input("Quantidade estimada de idosos:"))

                    if criancas < 0 or idosos < 0:
                        print("Os números de crianças e idosos não podem ser negativos.")
                    elif criancas + idosos > pessoas:
                        print("A soma de crianças e idosos não pode ser maior do que o total de pessoas.")
                    else:
                        break

                except ValueError:
                    print("Digite números válidos.")

            # Coleta da descrição da situação
            while True:
                situacao = input("Descreva a situação avistada ou presenciada:").strip()
                if situacao:
                    break
                print("A descrição da situação não pode ser vazia.")

            # Geração aleatória de senha do chamado
            senha = random.randint(500, 1000)

            # Montagem do dicionário do chamado
            chamado = {
                "Nome": nome,
                "Idade": idade,
                "Endereço": endereco,
                "Quantidade estimada de pessoas totais": pessoas,
                "Quantidade de criancas": criancas,
                "Quantidade de idosos": idosos,
                "Descrição da situacao": situacao,
                "Senha do chamado": senha,
            }

            # Adiciona o chamado à lista de chamados
            chamados.append(chamado)

            # Confirmação de envio
            print("\n" + "-" * 50)
            print("\nO seu chamado foi encaminhado para a Defesa Civil.")
            print("Acompanhe o processo na seção 'Status do Chamado'.")

        case "2":
            # Verifica o status dos chamados
            print("\nStatus do Chamado:\n")

            if not chamados:
                print("Nenhum chamado foi encontrado.")
            else:
                for status in chamados:
                    print("Senha do chamado:", status["Senha do chamado"])
                    print("Nome:", status["Nome"])
                    print("")
                    print("Endereço:", status["Endereço"])
                    # Chama função que retorna hospital mais próximo
                    print(hospital_mais_proximo(status["Endereço"]))
                    print("\nA ajuda já está a caminho. Por favor, permaneça em um local seguro.\n")
                    print("-" * 30)

        case "3":
            # Exibe o histórico de chamados
            print("\nHistórico de Chamados:\n")

            if not chamados:
                print("Nenhum chamado registrado ainda.")
            else:
                num = 1
                for chamado in chamados:
                    print(f"CHAMADO #{num}:")
                    for info, valor in chamado.items():
                        print(f"{info}: {valor}")
                    num += 1
                    print("\n" + "-" * 30)

        case "4":
            # Encerra o sistema
            print("\nEncerrando o sistema. Obrigado por usar o Apluvi Alert!")
            break

        case _:
            # Caso a opção digitada seja inválida
            print("\nOpção inválida. Tente novamente.")
