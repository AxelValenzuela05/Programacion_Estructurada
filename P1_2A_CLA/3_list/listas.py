import os
#Ejemplo 1 Crear una lista e imprimir  el contenido
os.system("cls")

#1er forma
numeros=[23,100,45,56]
print(numeros)

#2da forma

for i in numeros:
    print(i)

#3era forma

for i in range(0,len(numeros)):
    print(numeros[i])























#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

os.system("cls")

palabras=["hola","casa","jupiter","sol"]

palabra_buscar=input ("Dame la plabra a buscar: ")

#1era forma
if palabra_buscar in palabras:
    print("Se encontro la palabra")
else:
    print("No encontro la palabra")

#2da forma
encontro=False
for i in palabras:
    if i ==palabra_buscar:
        encontro=True
if encontro:
    print("Se encontro la palabra")
else:
    print("no se encontro la palbara")

#3era forma
encontro=False
for i in palabras(0,len(numeros)):
    if palabras[i]==palabra_buscar:
        encontro=True
if encontro:
    print("Se encontro la palabra")
else:
    print("no se encontro la palbara")







#Ejemplo3 añadir elementos a una lista

numeros=[]
opc="si"

while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("Deseas solicitar otro numero (si/no)").lower()

print(numeros)







#Ejemplo4 Crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas

agenda =[
    ["Ivan", "123456789"],
    ["Alonso", "978837890"],
    ["Axel", "456789123"],
    ["Emiliano", "747898798"]
]
print(agenda)

for r in agenda:
    print(r)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])


valores=""
for r in range(0,3):
    for c in range(0,2):
        valores==f"{agenda[r][c]},"
    valores==f"\n"



