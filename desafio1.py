menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMETE_SAQUE = 3

while True:

   opcao = input(menu)

   if opcao == "1":
       valor = float(input("Informe o valor do depósito: ")) #receber valor
       if valor > 0:
          saldo += valor
          extrato += f"Deposito: R$ {valor:.2f} \n"

       else:
          print("Operação falhou! o valor informado é invalido.")


   elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMETE_SAQUE

        if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente. ")

        elif excedeu_limite:
          print("Operação Falhou! Você excedeu o limite.")

        elif excedeu_saque:
          print("Operação falhou! Você excedeu o limite de saques.")

        elif valor > 0: 
           saldo -= valor
           extrato += f"saque: R$ {valor:.2f} \n" #registrar historico
           numero_saques += 1
           
        else:
           print("Operação falhou! O numero informado é invalido")   
           

   elif opcao == "3":
    print("\n ========== EXTRATO =========")
    print("Não foram realizado movimentações." if  not extrato else extrato)
    print(f"\nsaldo: R$ {saldo:.2f}") 
    print("============================")  


   elif opcao == "0":
      break

   else:
    print("Operação invalida, por favor selecioa novamente a operação desejada.")
