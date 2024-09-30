def fibonacci(n):
    if n <= 0:
        print("Por favor, insira um número positivo.")
    elif n == 1:
        print("Sequência de Fibonacci até", n, "termo:")
        print(0)
    else:
        print("Sequência de Fibonacci até", n, "termos:")
        a, b = 0, 1
        print(a, b, end=" ")
        
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c 
        print()

num_termos = int(input("Quantos termos da sequência de Fibonacci você quer? "))
fibonacci(num_termos)
