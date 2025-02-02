# Analizador Léxico 🔍

## ¿Qué es el Análisis Léxico? 📚

El análisis léxico es la primera fase en el proceso de compilación de un lenguaje de programación. Su función principal es analizar el código fuente caracter por caracter para identificar y clasificar los elementos básicos del lenguaje, conocidos como "tokens".

### Tokens Reconocidos 🏷️

El analizador identifica los siguientes elementos:

- 📝 Identificadores (nombres de variables y funciones)
- 🔢 Números (enteros y decimales)
- 🔑 Palabras reservadas (if, else, int, float, string)
- ➗ Operadores (aritméticos y lógicos)
- 📏 Delimitadores (paréntesis, llaves, punto y coma)
- 💬 Cadenas de texto
- 📋 Comentarios (de una línea y multilínea)

### Proceso de Análisis ⚙️

Durante el análisis, el programa:
1. Lee el código fuente caracter por caracter
2. Identifica patrones usando expresiones regulares
3. Clasifica cada elemento encontrado
4. Registra su posición (línea y columna)
5. Detecta errores léxicos

> "Un analizador léxico es como un detector de piezas de rompecabezas: identifica cada pieza individual antes de que comience el verdadero ensamblaje del programa." 🧩