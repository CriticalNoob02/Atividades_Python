## Biblioteca para algumas funções matemáticas
import math

## Declarando as variaveis;
Confirmação = 1
Menu = ""
print("")
## Mensagem de Boas-Vindas;
print("Bem vindo ao App foda de Exercicios, onde estão todas as 15 atividades que foram lançadas para criar!")

## Laço de repetição do Menu;
while Confirmação == 1:
    Confirmação = ""
    
    ## Menu de Navegação;
    print("Você esta no menu de Navegação, digite o número referente ao exercicio que deseja ter acesso.")
    print("")
    print("Link dos exercicios: https://wiki.python.org.br/EstruturaSequencial")
    print("")
    print("1 - Alo Mundo;")
    print("2 - Mostrar o Número;")
    print("3 - Soma;")
    print("4 - Média Bimestral;")
    print("5 - m/cm;")
    print("6 - Descubra a Área do Circulo;")
    print("7 - Descubra a Área do Quadrado;")
    print("8 - Salário do Mês;")
    print("9 - Conversor de Celsio / Fahrenheit;")
    print("10 - Conversor de Fahrenheit / Celsio;")
    print("11 - Analisador de números;")
    print("12 - Peso Ideal;")
    print("13 - Peso Ideal 2;")
    print("14 - Controle de Pesca do João;")
    print("15 - O ataque do Leão;")
    print("16 - Hora da pintada;")
    print("17 - Hora da pintada (só que mais complexo)  ;")
    print("18 - Analisador de download;")

    Menu = int(input("Digite aqui: "))
    
    ## Atividades;
    if(Menu == 1):
        Menu = ""
        print("")
        print("Alô Mundo!")
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))

    elif(Menu == 2):
        Menu = ""
        print("")

        num1 = int(input("Digite um Número: "))

        ## Respostas;
        print("O número digitado foi:",num1,"!")
        num1 = ""
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))

    elif(Menu == 3):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao somador de números!")

        ##Laço para repetir a operação;
        while Confirmação2 == 1:
            Confirmação2 = ""
            num1 = int(input("Digite um Número: "))
            num2 = int(input("Digite outro Número: "))
            soma = num1 + num2

            ## Respostas;
            print("A soma dos números digitados é:",soma)

            ## Zerando as variaveis;
            num1 = ""
            num2 = ""
            soma = ""

            print("")
            Confirmação2 = (int(input("Deseja fazer a operação novamente ? (Sim = 1 / Não = 2)")))
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 4):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao gerador de médias, digite suas notas com um '.' no lugar de uma ','!")

        ##Laço para repetir a operação;
        while Confirmação2 == 1:
            num1 = float(input("Digite sua primeira nota: "))
            num2 = float(input("Digite sua segunda nota: "))
            num3 = float(input("Digite sua terceira nota: "))
            num4 = float(input("Digite sua quarta nota: "))
            media = ((num1+num2+num3+num4)/4)

            ## Respostas;
            print("Baseado nas notas inseridas, a sua média bimestral é:",media)

            ## Zerando as variaveis;
            num1 = ""
            num2 = ""
            num3 = ""
            num4 = ""
            media = ""

            print("")
            Confirmação2 = (int(input("Deseja criar a média bimestral novamente ? (Sim = 1 / Não = 2)")))
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 5):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Conversor de Comprimento, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            decisão = int(input("Qual a conversão que você deseja? (M para CM = 1 / CM para M = 2)"))

            ## Escolha 1 (Metros para Centimetros);
            if(decisão == 1):
                num1 = float(input("Digite o valor em Metros: "))
                conversão = num1*100

                ## Respostas;
                print(num1,"metros é equivalente a ",conversão,"centimetros!")

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""

            ## Escolha 2 (Centimetros para Metros);
            elif(decisão == 2):
                num1 = float(input("Digite o valor em Centimetros: "))
                conversão = num1/100
                print(num1,"centimetros é equivalente a ",conversão,"metros!")

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""
            
            ## Comando de Erro;
            else:
                print("o Comando digitado é invalido, favor inserir um valo valido!")
            
            print("")
            Confirmação2 = (int(input("Deseja converter novamente ? (Sim = 1 / Não = 2)")))
        print("")    
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 6):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao analisador de raio, digite os valores com um '.' no lugar de uma ','!")

        ## Laço de repetição da operação;
        while Confirmação2 == 1:
            num1 = float(input("Digite o valor raio do circulo: "))
            conversão = (3.14*(num1**2))

            ## Respostas;
            print("A área de um circulo com um raio de",num1,"é igual a:",conversão)

            ## Zerando as variaveis;
            num1 = ""
            conversão = ""

            Confirmação2 = (int(input("Deseja converter novamente ? (Sim = 1 / Não = 2)")))
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 7):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao analisador de Àrea do Quadrado, digite os valores com um '.' no lugar de uma ','!")

        ## Laço de repetição da operação;
        while Confirmação2 == 1:
            num1 = float(input("Digite o valor dos lados do quadrado: "))
            conversão = num1**2
            
            ## Respostas;
            print("")
            print("A área de um quadrado com lados =",num1,"é igual a:",conversão)
            print("o dobro dsesta área é",conversão*2)

            ## Zerando as variaveis;
            num1 = ""
            conversão = ""
            
            print("")
            Confirmação2 = (int(input("Deseja converter novamente ? (Sim = 1 / Não = 2)")))
        print("")
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 8):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao SS (Seu Salário), digite os valores com um '.' no lugar de uma ','!")
        
        ## Laço de repetição da Operação;
        while Confirmação2 == 1:
            num1 = float(input("Digite o valor do seu salário por hora: "))
            num2 = float(input("Agora Digite a quantidade de Horas trabalhadas no mês: "))
            conversão = num1*num2   

            ## Respostas;
            print("")
            print("O Valor do seu sálario do mês é:",conversão,"!!")

            ## Zerando as variaveis;
            num1 = ""
            num2 = ""
            conversão = ""

            print("")
            Confirmação2 = (int(input("Deseja Conferir seu Salário novamente ? (Sim = 1 / Não = 2)")))
        print("")        
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 9 or Menu == 10):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Conversor de Temperatura, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            decisão = int(input("Qual a conversão que você deseja? (ºF para ºC = 1 / ºC para ºF = 2)"))

            ## Escolha 1 (Celsius para Fahrenheit);
            if(decisão == 1):
                num1 = float(input("Digite o valor em Fahrenheit: "))
                conversão = ((num1 - 32)*5/9)

                ## Respostas;
                print(num1,"ºF é equivalente a ",conversão,"ºC!")

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""
            
            ## Escolha 2 (Fahrenheit para Celsius);
            elif(decisão == 2):
                num1 = float(input("Digite o valor em Celsius: "))
                conversão = ((num1 * 9/5)+ 32)

                ## Respostas;
                print(num1,"ºC é equivalente a ",conversão,"ºF!")

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""
            
            ## Comando de Erro;
            else:
                print("o Comando digitado é invalido, favor inserir um valo valido!")
            
            print("")
            Confirmação2 = (int(input("Deseja converter novamente ? (Sim = 1 / Não = 2)")))
        print("")    
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))  
 
    elif(Menu == 11):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Jogo dos números, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            num1 = int(input("Digite um número pertencente a classe 'Inteiro': "))
            num2 = int(input("Digite outro número pertencente a classe 'Inteiro': "))
            num3 = float(input("Agora digite um número pertencente a classe 'Real': "))
            operação1 = ((num1*2)*(num2/2))
            operação2 = ((num1*3)+num3)
            operação3 = num3**3

            ## Respostas;
            print("")
            print("O produto do dobro do primeiro número com metade do segundo número é igual a:",operação1)
            print("a soma do triplo do primeiro número com o terceiro número é igual a:",operação2)
            print("o terceiro número elevado ao cubo:",operação3)

            print("")
            Confirmação2 = (int(input("Deseja jogar novamente ? (Sim = 1 / Não = 2)")))
        print("")            
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 12 or Menu == 13):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Teste de Peso, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            decisão = int(input("Digite o número correspondente ao seu sexo? (M = 1 / F = 2) "))

            ## Escolha 1 (Metros para Centimetros);
            if(decisão == 1):
                num1 = float(input("Qual sua altura? "))
                conversão = ((72.7*num1)-58)

                ## Respostas;
                print("O peso ideal para um Homem com uma altura de",num1,"é igual a:",conversão)

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""
            
            ## Escolha 2 (Centimetros para Metros);
            elif(decisão == 2):
                num1 = float(input("Qual sua altura? "))
                conversão = ((62.1*num1)-44.7)

                ## Respostas;
                print("O peso ideal para uma Mulher com uma altura de",num1,"é igual a:",conversão)

                ## Zerando as variaveis
                num1 = ""
                conversão = ""
                decisão = ""
            
            ## Comando de Erro;
            else:
                print("o Comando digitado é invalido, favor inserir um valo valido!")
            
            print("")
            Confirmação2 = (int(input("Deseja converter novamente ? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))      

    elif(Menu == 14):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Controle de Pesca do João, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            peso = float(input("Insira o peso do peixe pescado: "))
            
            ## Operação da Multa;
            if(peso > 50):
                excesso = peso-50
                multa = excesso*4.0
                print("Seu Peixe passou",excesso,"Kg do peso máximo permitido no local, e você receberá uma multa de",multa)

            else:
                print("Seu peixe não passou do peso máximo permitido no local!")    


            print("")
            Confirmação2 = (int(input("Deseja conferir outro peixe? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    elif(Menu == 15):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Ataque do Leão, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            num1 = float(input("Digite o valor que recebe de salário por hora: "))
            num2 = float(input("Digite aqui a quantidade de Horas trabalhadas neste mês: "))
            
            ## Operações;
            salário = num1*num2
            ir = (salário*11/100)
            inss = (salário*8/100)
            sindicato = (salário*5/100)

            ## Respostas;
            print("")
            print("Seu salário Bruto é: R$",salário)
            print("Você paga R$",ir,"de Importo de Renda!")
            print("Você paga R$",inss,"de INSS!")
            print("Você paga R$",sindicato,"para o Sindicato!")
            print("Seu salário liquido é: R$",(salário-ir-inss-sindicato))

            print("")
            Confirmação2 = (int(input("Deseja conferir outro peixe? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))  

    elif(Menu == 16):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo a Hora da Pintada, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            metros = (float(input("Digite o valor (em metros quadrados) da área a ser pintada: ")))
            litros = (math.ceil(metros / 3 )) ## Método de Arredondamento da Biblioteca
            latasTinta =(math.ceil(litros / 18)) ## Método de Arredondamento da Biblioteca
            custo = (float(latasTinta * 80))

            ## Respostas;
            print("")
            print("Será nescessário utilizar",litros,"Litros de tinta para pintar",metros,"m².")
            print("Você precisa pode levar",latasTinta,"latas de tinta, e isso vai lhe custar",custo)


            print("")
            Confirmação2 = (int(input("Deseja conferir outro peixe? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))  

    elif(Menu == 17):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Ataque do Leão, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")
            metros = (float(input("Digite o valor (em metros quadrados) da área a ser pintada: ")))
            litros = (math.ceil(metros / 6 )) ## Método de Arredondamento da Biblioteca
            latasTinta =(math.ceil(litros / 18)) ## Método de Arredondamento da Biblioteca
            galaoTinta = (math.ceil(litros / 3.6))
            custoLata = (latasTinta * 80)
            custoGalao = (galaoTinta * 25)

            
            print("")
            Confirmação2 = (int(input("Deseja conferir outro peixe? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))  

    elif(Menu == 18):
        Menu = ""
        Confirmação2 = 1
        print("")
        print("Bem-Vindo ao Ataque do Leão, digite os valores com um '.' no lugar de uma ','!")

        while Confirmação2 == 1:
            print("")

            print("")
            Confirmação2 = (int(input("Deseja conferir outro peixe? (Sim = 1 / Não = 2)")))
        print("") 
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    

    else:
        Menu = ""
        print("O Comando Digitado não foi encontrado!")
        Confirmação = int(input("Deseja Voltar ao menu de exercicios ?(Sim = 1 / Não = 2)"))    


## Mensagem de Fechamento do App
print("")                                                                            
print("")                                                                            
print("")                                                                            
print("                                      ▓▓▓▓▓▓  ▓▓▓▓▓▓                                ")
print("                                      ▓▓  ░░▓▓▓▓  ▓▓▓▓▓▓                            ")
print("                                ▓▓▓▓▓▓▓▓░░  ░░▓▓░░░░▓▓▓▓  ▓▓                        ")
print("                              ▒▒▓▓░░  ▓▓░░░░░░░░░░░░▓▓░░░░▓▓                        ")
print("                                  ▒▒░░  ░░░░░░░░░░░░░░░░▓▓▓▓▒▒                      ")
print("                                  ▓▓░░░░░░░░░░░░░░░░░░░░▓▓░░▓▓                      ")
print("                ██████████    ▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓                      ")
print("            ██████      ██████    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒▒▒▒▒▓▓▓▓                      ")
print("          ████              ████████▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒  ▒▒▓▓                        ")
print("        ████                  ██████░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        ")
print("                          ██████████░░  ░░░░░░██░░░░░░████                          ")
print("                    ██████████    ██░░░░░░░░░░▒▒░░░░░░▒▒██                          ")
print("              ██████████          ██░░░░░░░░░░░░░░░░░░░░██                          ")
print("        ██████████                  ████░░░░░░░░░░░░░░░░██                          ")
print("      ██████                          ████░░░░░░▒▒▒▒░░██                            ")
print("    ████                              ██▓▓██░░░░░░░░██                              ")
print("  ████                          ████████▓▓▓▓████████                                ")
print("  ██                          ████▓▓▓▓▓▓████████▓▓██████                            ")
print("  ██                        ████▓▓▓▓▓▓▓▓▓▓██████▓▓██▓▓▓▓██                          ")
print("                          ▓▓████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▓▓                        ")
print("                        ████████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓██                        ")
print("                      ██▓▓▓▓▓▓▓▓████████████████▓▓██████▓▓██                        ")
print("                      ██▓▓██▓▓▓▓████▒▒░░░░  ░░░░▓▓██▒▒██▓▓██                        ")
print("                    ██▓▓▓▓██████████▒▒  ░░░░    ▓▓██▒▒██▓▓████                      ")
print("                    ██▓▓▓▓▓▓████  ██▒▒░░    ░░░░▓▓██▒▒▒▒██████                      ")
print("                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░      ▓▓██▒▒▒▒██▓▓██                      ")
print("                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░░░░░░░░░▓▓██▒▒██▓▓██                      ")
print("                ██▓▓▓▓████▓▓██    ████▒▒░░    ░░░░▓▓██▒▒██▓▓▓▓██                    ")
print("                ██▓▓██░░░░██        ████████▓▓▓▓▓▓▓▓████████▓▓▓▓████                ")
print("                  ██░░░░████        ████████████████████████▓▓████░░████            ")
print("                ██░░░░░░░░██        ██▒▒░░░░░░░░░░░░░░░░████▓▓██░░░░░░░░██          ")
print("                ██░░░░░░░░░░██      ██░░    ░░░░░░░░░░░░░░░░████░░░░░░░░██          ")
print("                ██░░░░░░░░░░██      ██▒▒░░░░    ░░░░██░░░░░░████░░░░░░██            ")
print("                ██░░░░░░░░██      ██▒▒  ▒▒▒▒▒▒░░░░░░██░░░░░░░░████████              ")
print("                  ████████        ██████    ▒▒▒▒████░░████░░░░██                    ")
print("                                  ██    ████▒▒██  ████▒▒▒▒▒▒▒▒░░██                  ")
print("                                ██░░░░░░  ▒▒▒▒██    ██▒▒▒▒▒▒▒▒░░░░██                ")
print("                                ██░░░░░░▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                ")
print("                              ██░░░░░░▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                ")
print("                            ██░░░░░░░░▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              ")
print("                            ██░░░░░░▒▒▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              ")
print("                          ██░░░░░░▒▒▒▒▒▒██              ██▒▒▒▒▒▒░░░░██              ")
print("                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              ")
print("                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              ")
print("                          ██░░▒▒▒▒▒▒██                    ████████████              ")
print("                        ████████████                        ████████                ")
print("                        ██▓▓▓▓████                          ██▓▓▓▓██                ")
print("                      ████████████                        ██▓▓██████████            ")
print("                    ██▓▓▓▓▓▓▓▓██                          ██▓▓▓▓▓▓▓▓▓▓▓▓████        ")
print("                  ██▓▓▓▓▓▓▓▓▓▓██                          ██████▓▓▓▓▓▓░░░░░░██      ")
print("                ██▓▓░░░░░░░░████                                ██████████████      ")
print("                ██████████████                                                      ")
print("")
print("Muito Obrigado por usar meu APP!")