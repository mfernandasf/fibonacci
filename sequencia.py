# a) Progressão aritmética (diferença de 2)
seq_a = [1, 3, 5, 7]
seq_a.append(seq_a[-1] + 2)
print("a) Próximo número:", seq_a[-1])

# b) Progressão geométrica (multiplica por 2)
seq_b = [2, 4, 8, 16, 32, 64]
seq_b.append(seq_b[-1] * 2)
print("b) Próximo número:", seq_b[-1])

# c) Quadrados dos inteiros
seq_c = [0, 1, 4, 9, 16, 25, 36]
seq_c.append(len(seq_c) ** 2)
print("c) Próximo número:", seq_c[-1])

# d) Quadrados dos pares
pares = [2, 4, 6, 8]
seq_d = [n ** 2 for n in pares]
seq_d.append((pares[-1] + 2) ** 2)
print("d) Próximo número:", seq_d[-1])

# e) Fibonacci
fib = [1, 1, 2, 3, 5, 8]
fib.append(fib[-1] + fib[-2])
print("e) Próximo número:", fib[-1])

# f) Alternando entre grandes e pequenas adições
seq_f = [2, 10, 12, 16, 17, 18, 19]
seq_f.append(seq_f[-1] + 1)
print("f) Próximo número:", seq_f[-1])
