import random
import time
numero_secreto = random.randint(1,10)
max_tentativas = 6
print("Pensando em um número de 1 a 10...")
time.sleep(2)
tentativas = 0
while True:
    try:
        num1 = int(input("Escolha um número: "))
    except ValueError:
        print("Apenas números Inteiros Positivos")
        continue
    tentativas+=1
    if num1 == numero_secreto:
         print(f"vocẽ acertou, o número era {numero_secreto}, voce acertou em {tentativas} tentativas")
         break
    elif tentativas >= max_tentativas:
        print("muitas tentaivas")
        time.sleep(2)
        print(f"o número era {numero_secreto}")
        break
    elif num1 < numero_secreto:
        print(f"Chute mais alto \n número de tentativas: {tentativas}\n faltam: {max_tentativas - tentativas} ")
    
    else:
        print(f"Chute mais baixo \n número de tentativas: {tentativas}\n faltam: {max_tentativas - tentativas}")