El contenido del archivo `Katas_Python_ThePower_v2.py` es una colección de 41 ejercicios de lógica y programación en Python, que abarcan conceptos fundamentales como funciones, lambdas, estructuras de datos (listas, diccionarios, tuplas), recursividad, manejo de excepciones (`try...except`), programación funcional (`map`, `filter`, `reduce`), programación orientada a objetos (clases `Arbol` y `UsuarioBanco`), y lógica de control de flujo (`if/elif/else`).

## 📄 README para Katas_Python_ThePower_v2.py

### 🐍 Proyecto Lógica: Katas de Python

Este repositorio contiene la resolución de una serie de 41 ejercicios de programación en Python ("Katas") que buscan reforzar conceptos esenciales de la lógica de programación y el uso de estructuras de datos y funciones específicas de Python.

-----

### 📝 Contenido del Archivo

El archivo `Katas_Python_ThePower_v2.py` es el resultado de la conversión de un **Jupyter Notebook** (`.ipynb`) a un script Python (`.py`), manteniendo la estructura original con comentarios para cada ejercicio.

Cada ejercicio (o "Kata") resuelve un problema de lógica y sintaxis específico, incluyendo:

  * **Manipulación de Cadenas y Listas:** Frecuencia de letras, filtrado de palabras por longitud o letra inicial, anagramas, etc. (Katas 1, 3, 12, 14, 16, 25, 29, 30).
  * **Funciones Anónimas (`lambda`) y Funcional:** Uso intensivo de `map()`, `filter()`, y `reduce()` para operaciones con listas y tuplas (Katas 2, 4, 7, 9, 13, 15, 17, 19, 20, 22, 23, 24, 26, 33).
  * **Manejo de Excepciones:** Implementación de `try/except` para manejar errores comunes como la división por cero, `ValueError` (entrada no numérica) y listas vacías (Katas 8, 10, 11).
  * **Estructuras de Control de Flujo:** Cálculos de promedios, factoriales, clasificaciones y lógica condicional (Katas 5, 6, 27, 38, 39, 41).
  * **Programación Orientada a Objetos (POO):** Creación de clases con atributos y métodos para simular objetos como un `Arbol` y un `UsuarioBanco` (Katas 34, 36).
  * **Funciones con Múltiples Opciones:** Implementación de una función maestra (`procesar_texto`) que delega tareas a sub-funciones (Kata 37).

-----

### 🚀 Estructura del Código

El script está organizado en celdas numeradas (indicadas por comentarios como `# In[362]:`) que corresponden a cada ejercicio.

1.  **Definición del Problema:** Cada celda comienza con el enunciado del ejercicio como comentario.
2.  **Implementación:** Se define la función o se escribe el código necesario para resolver el problema.
3.  **Prueba/Ejecución:** Se incluye una llamada a la función o una impresión del resultado para verificar su correcto funcionamiento.

-----

### 💡 Observaciones sobre la Implementación

  * **Kata 4:** Asume que las listas de entrada tienen la misma longitud para calcular la diferencia de valores correspondientes.
  * **Kata 6 (Factorial):** La implementación actual utiliza un bucle (`for`) en lugar de la **recursividad** explícitamente solicitada. Una implementación recursiva sería más adecuada para seguir la consigna.
  * **Kata 8 y 11 (Excepciones):** Se utilizan bloques `try...except` anidados o múltiples para manejar `ValueError` y `ZeroDivisionError` de forma específica.
  * **Katas 34 y 36 (POO):** Las clases `Arbol` y `UsuarioBanco` implementan los atributos y métodos solicitados para simular su comportamiento. En la clase `UsuarioBanco` se definieron errores personalizados (`SinCuentaCorrienteError`, `SaldoInsuficienteError`) para un manejo de excepciones más robusto.

-----

### 🛠️ Proceso de Generación y Conversión

El archivo fue inicialmente desarrollado en un entorno **Jupyter Notebook** y luego convertido a un script de Python usando la herramienta `nbconvert`, tal como se detalla en los comentarios iniciales del archivo:

```bash
pip install nbconvert 
jupyter nbconvert --to script Katas_Python_ThePower_v2.ipynb
```

