#!/usr/bin/env python
# coding: utf-8

# In[340]:


"""
Readme:
Para la realización de estos ejercicios:
Copiamos todo el texto del pdf y se lo pegamos al chat de Gemini.
Pedimos a Gemini que nos pase los textos a comentarios de python , para poder pegarlo en un Jupyter Notbook con el que iremos creando el código que se nos pide
Si la IA no nos pone todo en comentario, podemos poner nosotros todos das las líneas a comentario usando el atajo de teclado en Jupyter Notebook Ctrl+/
Creamos un entorno en anaconda con Python 3.14.0 para este proyecto y dentro de él instalamos Jupyter Notbook
Pegamos el resultado de Gemini en un Jupyter Notbook y dividimos cada pregunta en celdas separadas seleccionando con el cursor el comienzo de una nueva pregunta y aplicando la combinación de teclas CTRL+Shift+-
Para convertir el archivo de estos ejercicios, que se han heco en Jupyter notebook, realizamos el proceso que vemos en el vídeo:
https://www.youtube.com/watch?v=zJf2lII3nmA
Donde, resumiendo, realizamos lo siguiente:
    En la carpeta donde tengo el archivo ipynb, abro el cmd
    Escribo:
        pip install nbconvert 
    Luego:
        jupyter nbconvert --to script Katas_Python_ThePower_v2.ipynb
    Acabando con el nombre del archivo a convertir



"""
 
# =================================================================
# PROYECTO LÓGICA: Katas de Python
# =================================================================


# In[362]:


# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencia_por_letra(texto):
    """
    Esta función cuenta las veces que se encuentra una letra dentro de un texto.
    Parametros posicionales:
    texto --- str, cadena de texto con la que contaremos las repeticiones por letra  
    """
    frecuencia={}
    for letra in texto.lower():
        if "a"<=letra<="z":
            frecuencia[letra]=frecuencia.get(letra,0)+1
    return frecuencia
frecuencia_por_letra("texto")


# In[363]:


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista = [1,2,3,4,5,6,7,8,9]
resultado = map(lambda n : n * 2, lista)
resultado_lista = list(resultado)

print(resultado_lista)



# In[364]:


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def busqueda(lista_de_palabras,palabra_objetivo):
    """
    Esta función busca si una palabra está contenida dentro de otras palabras de una lista
    parametros posicionales:
    lista_de_palabras -- list(str), lista de palabras
    palabra_objetivo -- str, palabra o cadena de texto a buscar dentro de las cadenas de texto de lista_de_palabras 
    """
    lista_coincidentes=[]
    for a in lista_de_palabras:
        if palabra_objetivo in a:
            lista_coincidentes=lista_coincidentes+[a]
    return lista_coincidentes

resultado = busqueda(["girasol", "luna", "solo"],"sol")
print(resultado)


# In[365]:


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def fdiferencia(lista1, lista2):
    """
    Esta función multiplica cada elemento de una lista por otro elemento de otra lista que esté en la misma posiciñon
    parametros posicionales
    lista1 -- list(int), lista de elementos numéricos
    lista2 -- list(int), lista de elementos numéricos
    """
    diferencia = list(map(lambda x,y: x-y, lista1, lista2))
    return diferencia
resultado = fdiferencia([10,20,30,40], [5,6,7,8])
print(resultado)
# Sobreentiendo que se quiere decir que es entre dos listas de igual longitud


# In[3]:


# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.
def fmedia(lista_num,nota_aprobado=5):
    """
    Esta función calcula si la nota media de una lista es mayor o igual a una nora definida de aprobado
    Parametros posicionales:
    lista_num -- list(float), lista de numeros con las notas del alumno.
    nota_aprobado -- float, nota de corte con la que el alumno se considera aprobado
    """
    media = sum(lista_num) / len(lista_num)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

notas_del_alumno = [5,7]
nota_aprobado = 6
resultado = fmedia(notas_del_alumno,nota_aprobado)
print(resultado)    


# In[6]:


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def fFactorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fFactorial(n - 1)
resultado = fFactorial(4)
print(resultado)


# In[7]:


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tupla_a_str(tupla):
    """
    función que convierte una lista de tuplas a una lista de strings usando la función map()
    parametros posicionales:
    tupla --- tuple, tupla a convertir en lista
    """
    return list(map(str, tupla))
Tupla = (1,"hola")
resultado = tupla_a_str(Tupla)
print(resultado)


# In[382]:


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
def fDivision():
    entrada_num1 = input("Introduce el numero a dividir (dividendo): ")
    entrada_num2 = input("Introduce el divisor: ")
    try:
        entrada_num1_float = float(entrada_num1)
        entrada_num2_float = float(entrada_num2)
        resultado=entrada_num1_float/entrada_num2_float
        print(f"El resultado de la división {entrada_num1} / {entrada_num2} es: {resultado}")
    except ZeroDivisionError: # Para el error de división por cero
        print("ERROR: división por cero")
    except ValueError as ve: # Para error al intentar pasar los valores ingresados al float (lo que está entes del try) 
        print(f"Error por un valor introducido no numérico: {ve}")
    except Exception as e: # Para cualquier otra excepción
        print(f"Ha ocurrido un error inesperado: {e}")
fDivision()


# def fDivision():
#     entrada_num1 = input("Introduce el numero a dividir (dividendo): ")
#     entrada_num2 = input("Introduce el divisor: ")
#     num1=float(entrada_num1)
#     num2=float(entrada_num2)
#     if num2 == 0 or not isinstance(num1,(int,float)) or not isinstance(num2,(int,float)):
#         div = float(num1)/float(num2)
#         print(div)
#     else:
#         print("ERROR: divisón por cero o no se ha introducido un número")
# fDivision()
    


# In[384]:


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

# Otra forma que hice primero antes de probar la definitiva fue:
# def fExclusionLista(lista_mascotas_introducidas):
#     set_lista_mascotas_introducidas = set(lista_mascotas_introducidas)
#     set_mascotas_prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}
#     set_mascotas_permitidas = set_lista_mascotas_introducidas - set_mascotas_prohibidas
#     lista_mascotas_permitidas = list(set_mascotas_permitidas)
#     return lista_mascotas_permitidas
# fExclusionLista(["gato", "perro", "Cocodrilo"])

def fExclusionLista(lista_mascotas_introducidas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    mascotas_prohibidas_lower = [m.lower() for m in mascotas_prohibidas]
    return list(filter(lambda mascota_introducida: mascota_introducida.lower() not in mascotas_prohibidas_lower,lista_mascotas_introducidas))
lista_de_mascotas = ["Gato", "Perro", "Cocodrilo"]
fExclusionLista(lista_de_mascotas)


# In[20]:


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
def fPromedio(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)


# In[406]:


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
def pedir_edad():
    while True:
        try:
            edad_solicitada = input("Por favor, introduzca su edad:")
         
            edad = int(edad_solicitada)
            if not (0<=edad<=120):
                print("La edad debe de ser entre 0 y 120 años.")
            else:
                print(f"La edad introducida es correcta: {edad}")
                break
        except ValueError as ve:
            print(f"Valor introducido no numérico: {ve}")
pedir_edad() 
# podemos probar:
# a
# -1
# 121
# 20


# In[407]:


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def introducir_frase():
    frase_introducida =input("Introduzca una frase con la que quiera que le calcule la longitud de cada palabra:")
    lista_frase = frase_introducida.split()
    lista_longitudes = list(map(len,lista_frase))
    print(f"Las longitudes de cada palabra introducida son: {lista_longitudes}")
introducir_frase()


# In[408]:


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def generador_lista_de_tuplas(lista):
    elementos_no_repetidos = set(a.lower() for a in lista if isinstance(a,str) and a.isalpha())
    return list(map(lambda b: (b.upper(), b), elementos_no_repetidos))

generador_lista_de_tuplas(["A","b","A","a",1,"2","D"])


# In[24]:


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def filtro_palabras(lista_palabras, letra_inicial):
    letra = letra_inicial.lower()
    return list(filter(lambda a: a.lower().startswith(letra), lista_palabras))
filtro_palabras(["Ave","león","anaconda"],"a")


# In[411]:


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda x: x + 3
def aplicar_lambda_sumar_tres(lista_numeros):
    return list(map(sumar_tres, lista_numeros))
print("La lista con los numeros +3:", aplicar_lambda_sumar_tres([1,2,3,4,5,6,7,8,9]))

# # Otra opción hubiera sido:
# def lista_numeros():
#     lista_pedida=input("Introduce la lista de numeros separados por comas (ejemplo: 1,2,3):")
#     lista_pedida_convertida = lista_pedida.split(",")
#     return list(map(lambda a: int(a.strip(",")) + 3,lista_pedida_convertida))
# lista_numeros()


# In[421]:


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
def filtro_palabras_cortas(texto,longitud):
    """
    Función que filtra una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
    Parámetros posicionales:
        texto --- str, cadena de texto 
        longitud --- int, número entero, que define la longitud mínima de cada palabra a mostrar
    """
    texto_split=texto.split()
    return list(filter(lambda x: len(x)>longitud,texto_split))
    
filtro_palabras_cortas("Hola Mundo",4)
# Podemos probar también con 1 para que salgan las dos palabras del texto o 20 para comprobar que no sale ninguna


# In[423]:


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce # Importo la librería para poder usar la funcioón reduce
def lista_de_digitos(lista_digitos):
    """
    Función que toma una lista de dígitos y devuelva el número que componen esos dígitos.
    Parámetro posicional:
    lista_digitos --- list, lista idealmente con un dígito en cada elemento de la misma, aunque cada elemento acepta números de más de un dígito.
    """
    return reduce(lambda a,b: a*10+b,lista_digitos)
lista_de_digitos([5,7,2])

# # Sin función, directamente con lambda, lo hubiera hecho así:
# from functools import reduce
# lista_digitos=([5,7,2])
# reduce(lambda a,b: a*10+b,lista_digitos)


# In[37]:


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()
def fitrar_por_nota(lista_estudiantes):
    return list(filter(lambda a: a["calificacion"]>=90, lista_estudiantes))
lista_estudiantes_2 = [{"nombre": "Ana", "edad":20, "calificacion": 95}, {"nombre": "Luis", "edad":22, "calificacion": 85}]
fitrar_por_nota(lista_estudiantes_2)


# In[425]:


# 19. Crea una función lambda que filtre los números impares de una lista dada.
def filtro_pares(lista):
    return list(filter(lambda a: a%2!=0,lista))
lista_2=[1,2,3,4,5,6,7,8,9,10]
filtro_pares(lista_2)


# In[426]:


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()
def filtro_int(lista):
    return list(filter(lambda a: isinstance(a,int),lista))
lista_2=[1,"2",3,"Hola",4.5]
filtro_int(lista_2)


# In[427]:


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
calculadora_cubo = lambda a: a**3
calculadora_cubo(3)


# In[428]:


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce # Importo la librería para poder usar la funcioón reduce
reduce(lambda x, y: x * y, [1, 2, 3, 4])


# In[429]:


# 23. Concatena una lista de palabras.Usa la función reduce() .
from functools import reduce # Importo la librería para poder usar la funcioón reduce
reduce(lambda x, y: x + " " + y,["Hola","Mundo","Que","Tal"])


# In[430]:


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce # Importo la librería para poder usar la funcioón reduce
reduce(lambda x, y: x - y, [10, 2, 3, 4])


# In[431]:


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contador_caracteres(cadena_de_texto):
    return len(cadena_de_texto)
contador_caracteres("Hola Mundo")
# Otra forma mas simple sería:
# contador_caracteres = lambda a: len(a)
# contador_caracteres("Hola Mundo")


# In[432]:


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
calculadora_resto = lambda a,b: a%b
calculadora_resto(27,14)


# In[433]:


# 27. Crea una función que calcule el promedio de una lista de números.
def calculadora_promedio(lista):
    return sum(lista)/len(lista)
lista_2=[9,10,11]
calculadora_promedio(lista_2)


# In[434]:


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
lista = [50, 10, 30, 10, 20, 20]
vistos = set()
for indice,elemento in enumerate(lista):
    if elemento in vistos:
        print(f"El primer elemento de la lista repetido es: {elemento}")
        break
    vistos.add(elemento)

# Si quiero que me diga todos los repetidos simplemente quito el break


# In[29]:


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.
def enmascarador(variable):
    variable_string = str(variable)
    return "#" * (len(variable_string) - 4) + variable_string[-4:]
enmascarador("Cadena a enmascarar")


# In[436]:


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.
palabra_1 = "Saco"
palabra_2 = "cosa"
def comprobador_anagrama(palabra_1,palabra_2):
    if sorted(palabra_1.lower()) == sorted(palabra_2.lower()):
        print("Son anagramas")
    else:
        print("No son anagramas")
comprobador_anagrama("Saco","cosa")


# In[439]:


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
def buscanombres():
    try:
        nombres_input = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = [nombre.strip().lower() for nombre in nombres_input.split(',')]
        nombre_buscar = input("Introduce el nombre que deseas buscar: ").strip().lower()
        if nombre_buscar in lista_nombres:
            print(f"Éxito! El nombre '{nombre_buscar.capitalize()}' fue encontrado en la lista.")
        else:
            print(f"El nombre '{nombre_buscar.capitalize()}' no se encuentra en la lista.")
    except Exception as e:
        print("Error inesperado: ",e)
buscanombres()
# probar por ejemplo Ana,Maria,luis
    


# In[34]:


# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.
def buscar_puesto(nombre_completo, lista_empleados):
    nombre_normalizado = nombre_completo.strip().lower()
    for empleado in lista_empleados:
        if empleado["nombre"].strip().lower() == nombre_normalizado:
            return empleado["puesto"]
    return f"La persona '{nombre_completo}' no trabaja aquí."
print("Resultado para Alberto Núñez Feijóo:", buscar_puesto("Alberto Núñez Feijóo", empleados))
print("Resultado para Pedro Sanchez:", buscar_puesto("Pedro Sanchez", empleados))


# In[448]:


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_1=[1,2,3]
lista_2=[2,3,4]
list(map(lambda x,y: x+y, lista_1,lista_2))


# In[449]:


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
class Arbol:
    def __init__(self):
        # Inicializo el arbol y las ramas
        self.longitud_tronco=0
        self.longitud_ramas=[]
    def crecer_tronco(self):
        self.longitud_tronco+=1
    def nueva_rama(self):
        self.longitud_ramas.append(1)
    def crecer_ramas(self):
        self.longitud_ramas=[longitud_rama+1 for longitud_rama in self.longitud_ramas] 
    def quitar_rama(self,posicion):
        self.longitud_ramas.pop(posicion) 
    def info_arbol(self):
        return {
            "longitud tronco": self.longitud_tronco,
            "longitud ramas": self.longitud_ramas
        }

mi_arbol=Arbol()
print("La información de mi árbol es: ", mi_arbol.info_arbol())
mi_arbol.crecer_tronco()
print(f"La información inicial de mi árbol después de 'crecer_tronco' es: {mi_arbol.info_arbol()}")
mi_arbol.nueva_rama()
print(f"La información de mi árbol después de 'nueva_rama' es: {mi_arbol.info_arbol()}")
mi_arbol.nueva_rama()
print(f"La información de mi árbol después de 'nueva_rama' es: {mi_arbol.info_arbol()}")
mi_arbol.crecer_ramas()
print(f"La información de mi árbol después de 'crecer_ramas' es: {mi_arbol.info_arbol()}")
mi_arbol.nueva_rama()
print(f"La información de mi árbol después de 'nueva_rama' es: {mi_arbol.info_arbol()}")
mi_arbol.crecer_ramas()
print(f"La información de mi árbol después de 'crecer_ramas' es: {mi_arbol.info_arbol()}")
mi_arbol.nueva_rama()
print(f"La información de mi árbol después de 'nueva_rama' es: {mi_arbol.info_arbol()}")
mi_arbol.quitar_rama(2)
print(f"La información de mi árbol después de 'quitar_rama' en la posición indicada es: {mi_arbol.info_arbol()}")
mi_arbol.info_arbol()
print(f"La información de mi árbol después de 'info_arbol' es: {mi_arbol.info_arbol()}")


# In[36]:


# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
class SinCuentaCorrienteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass
class UsuarioBanco:
    def __init__(self, nombre, saldo_inicial, tiene_cuenta_corriente):
        self.nombre =nombre
        self.saldo =saldo_inicial
        self.tiene_cuenta_corriente=tiene_cuenta_corriente
    def _verificar_cuenta(self):
        if not self.tiene_cuenta_corriente:
            raise SinCuentaCorrienteError(f"{self.nombre} no tiene cuenta corriente para esta operación.")
    def retirar_dinero(self, cantidad):
        try:
            self._verificar_cuenta()
            if cantidad<=0: return print(f"Error: Cantidad a retirar debe ser positiva para {self.nombre}.")
            if self.saldo<cantidad:
                raise SaldoInsuficienteError(f"Saldo insuficiente de {self.nombre}. Saldo: {self.saldo}")
            self.saldo-=cantidad
            print(f"Retiro exitoso. {self.nombre} ha retirado {cantidad}. Nuevo saldo: {self.saldo}")
        except (SinCuentaCorrienteError, SaldoInsuficienteError) as e:
            print(f"Error al retirar: {e}")
    def transferir_dinero(self, otro_usuario, cantidad):
        try:
            self._verificar_cuenta() 
            if cantidad<=0: return print(f"Error: Cantidad a transferir debe ser positiva.")
            otro_usuario._verificar_cuenta() # EL origen debe tener cuenta
            if otro_usuario.saldo<cantidad:
                raise SaldoInsuficienteError(f"Saldo insuficiente en la cuenta de {otro_usuario.nombre}. Saldo: {otro_usuario.saldo}")
            otro_usuario.saldo-=cantidad
            self.saldo+=cantidad
            print(f"Transferencia de {cantidad} de {otro_usuario.nombre} a {self.nombre} exitosa.")
            print(f"   Saldo {otro_usuario.nombre}: {otro_usuario.saldo} | Saldo {self.nombre}: {self.saldo}")
        except (SinCuentaCorrienteError, SaldoInsuficienteError) as e:
            print(f"Error al transferir: {e}")
    def agregar_dinero(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            print(f"Depósito de {cantidad} a {self.nombre}. Nuevo saldo: {self.saldo}")

alicia = UsuarioBanco("Alicia", 100, True)
manu = UsuarioBanco("Manu", 50, True)
manu.agregar_dinero(20)
alicia.transferir_dinero(manu, 30)
alicia.retirar_dinero(50)


# In[453]:


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
import re #Importamos el módulo de Expresiones Regulares (Regular Expressions), que se aplicará en la función eliminar_palabra
def contar_palabras(texto):
    palabras=texto.lower().replace('.', '').replace(',', '').split()
    frecuencias={}
    for palabra in palabras:
        frecuencias[palabra]=frecuencias.get(palabra, 0) + 1
    return frecuencias
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)
def eliminar_palabra(texto, palabra_eliminar):
    return re.sub(r'\b'+re.escape(palabra_eliminar)+r'\b', '', texto).replace("  ", " ").strip()
def procesar_texto(texto,opcion,*args):
    if opcion=="contar":
        return contar_palabras(texto)
    elif opcion=="reemplazar":
        if len(args)!=2: return "Error: 'reemplazar' requiere palabra_original y palabra_nueva."
        return reemplazar_palabras(texto,args[0],args[1])
    elif opcion=="eliminar":
        if len(args)!=1: return "Error: 'eliminar' requiere la palabra a eliminar."
        return eliminar_palabra(texto, args[0])
    else:
        return "Error: Opción no válida."

texto_ejemplo = "El perro es un animal, y el perro es amigable."
print("Contar:", procesar_texto(texto_ejemplo, "contar"))
print("Reemplazar:", procesar_texto(texto_ejemplo, "reemplazar", "perro", "can"))
print("Eliminar:", procesar_texto(texto_ejemplo, "eliminar", "animal"))


# In[454]:


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia():
    hora=input("Indica la hora del día (número entero entre 0 y 23): ")
    try:
        hora_int=int(hora)
        if 0<=hora_int<=14:
            print(f"Las {hora_int} es una hora de mañana") 
        elif 15<=hora_int<=20:
            print(f"Las {hora_int} es una hora de tarde") 
        elif 21<=hora_int<=23:
            print(f"Las {hora_int} es una hora de noche") 
        else:
            print("El número introducido no está entre 0 y 23")
    except ValueError:
        print("No se ha introducido un número entre 0 y 23")
momento_del_dia()


# In[456]:


# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son: 0 - 69 insuficiente, 70 - 79 bien, 80 - 89 muy bien, 90 - 100 excelente
def calificacion():
    calificacion_numerica=input("Introduce la calificación numeria del alumno (número entero del 0 al 100): ")
    try:
        calificacion_numerica_int=int(calificacion_numerica)
        if 0<=calificacion_numerica_int<=69: print("Insuficiente") 
        elif 70<=calificacion_numerica_int<=79: print("Bien")
        elif 80<=calificacion_numerica_int<=89:  print("Muy bien")
        elif 90<=calificacion_numerica_int<=100:  print("Excelente")  
        elif 0>calificacion_numerica_int or calificacion_numerica_int>100:  print("Número fuera del rango de 0 a 100")
    except ValueError:
            print("La calificación no es un número entero entre 0 y 100")
calificacion()


# In[457]:


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math # PAra luego poder tener el número pi con math.pi
def calcular_area(figura, datos):
    figura=figura.lower()
    if figura=="rectangulo":
        if len(datos)!=2: return "Error: Rectángulo requiere (base, altura)."
        base, altura=datos
        return base*altura
    elif figura=="circulo":
        if len(datos)!=1: return "Error: Círculo requiere (radio)."
        radio=datos[0]
        return math.pi*(radio**2)
    elif figura == "triangulo":
        if len(datos)!=2: return "Error: Triángulo requiere (base, altura)."
        base, altura=datos
        return (base*altura)/2
    else:
        return f"Error: Figura '{figura}' no reconocida."
print("40. Área Rectángulo (5, 10):", calcular_area("rectangulo", (5, 10)))


# In[471]:


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.
precio_articulo=input("Ingrese el precio del artículo: ")
try:
    precio_articulo_float=float(precio_articulo)
    si_descuento=input("¿Tiene descuento?('Si/No'): ")
    if si_descuento.lower().strip()=="si":
        importe_descuento=input("Ingrese el importe del descuento (sólo el número positivo, sin moneda): ")
        try:
            importe_descuento_float=float(importe_descuento)
            if importe_descuento_float<=0:
                print("Descuento menor o igual a cero")
            else:
                precio_articulo_float-=importe_descuento_float
                print("El precio final del artículo sería :", precio_articulo_float)            
        except:
            print("Dato de descuento no numérico")
    else:
        print("El precio final del artículo sería :", precio_articulo_float)
except:
    print("Dato no numérico")

    

