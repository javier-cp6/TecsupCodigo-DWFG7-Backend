# Operadores Aritméticos
edad_juan = 40
edad_maria = 34


print(edad_juan % edad_maria)

print("""5 veces la edad 
de Juan es
{}""".format(edad_juan*5))

# potencia **

# Operadores de Comparación
# > < == != >= <=
# a diferencia, de JS, en python no existe ===
print(edad_juan <= edad_maria)  # False

# Operadores lógicos
# and or not

print(edad_juan > 10 and edad_maria < 40)
print(edad_juan > 10 or edad_maria < 40)
print(not edad_juan)

edad_eduardo = 18
edad_renato = 26
edad_laura = 35

print(edad_eduardo >= 18)
print(edad_eduardo > edad_laura)
print(edad_renato < edad_laura and edad_renato > edad_eduardo)
print(edad_laura > edad_renato or edad_laura < edad_eduardo)

# Operadores de Asignación
# = += -= *= /=
# en python no funciona ++ -- +1
edad = 50
edad += 1
print(edad)
