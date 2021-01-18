# import sys
# sys.stdin = open("input.txt","r")
# sys.stdout = open("output.txt","w")

#A,B,C = [float(A) for A in input().split()]
A,B,C = 3.0, 4.0, 5.2

T = (1/2) * A * C
c = 3.14159 * C * C
TR = C * (A + B) / 2
S = B * B
R = A * B

print("TRIANGULO: %0.3f" %T)
print("CIRCULO: %0.3f" %c)
print("TRAPEZIO: %0.3f" %TR)
print("QUADRADO: %0.3f" %S)
print("RETANGULO: %0.3f" %R)