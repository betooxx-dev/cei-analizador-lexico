"""Definición de tokens y patrones para el analizador léxico"""

TOKENS = [
    # Comentarios (deben ir primero para tener prioridad)
    ("COMENTARIO_BLOQUE", r"/\*[\s\S]*?\*/"),
    ("COMENTARIO_LINEA", r"//.*$"),
    
    # Palabras reservadas
    ("PALABRA_RESERVADA", r"\b(if|else|int|float|string|return)\b"),
    
    # Identificadores (actualizado para soportar caracteres Unicode)
    ("IDENTIFICADOR", r"[a-zA-ZáéíóúÁÉÍÓÚñÑ_][a-zA-ZáéíóúÁÉÍÓÚñÑ0-9_]*"),
    
    # Números
    ("NUMERO_REAL", r"\b\d*\.\d+\b"),
    ("NUMERO_ENTERO", r"\b\d+\b"),
    
    # Operadores
    ("OPERADOR_ARITMETICO", r"[+\-*/]"),
    ("OPERADOR_LOGICO", r"(==|!=|<=|>=|<|>|&&|\|\|)"),
    ("OPERADOR_ASIGNACION", r"="),
    
    # Delimitadores
    ("PARENTESIS_IZQ", r"\("),
    ("PARENTESIS_DER", r"\)"),
    ("LLAVE_IZQ", r"\{"),
    ("LLAVE_DER", r"\}"),
    ("COMA", r","),
    ("PUNTO_COMA", r";"),
    
    # Cadenas (actualizado para soportar diferentes tipos de comillas)
    ("CADENA", r'("([^"\\]|\\.)*"|\'([^\'\\]|\\.)*\')'),
    
    # Espacios y saltos de línea
    ("ESPACIO", r"[ \t\n\r]+"),
]