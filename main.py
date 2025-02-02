import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import re

class AnalizadorLexicoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")
        self.root.geometry("800x600")
        
        # Definición de tokens actualizada
        self.TOKENS = [
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
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Editor de texto con soporte Unicode
        editor_label = ttk.Label(main_frame, text="Código fuente:")
        editor_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.editor = scrolledtext.ScrolledText(main_frame, width=70, height=10, font=('Consolas', 10))
        self.editor.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        
        analizar_btn = ttk.Button(button_frame, text="Analizar", command=self.analizar_codigo)
        analizar_btn.pack(side=tk.LEFT, padx=5)
        
        limpiar_btn = ttk.Button(button_frame, text="Limpiar", command=self.limpiar_editor)
        limpiar_btn.pack(side=tk.LEFT, padx=5)
        
        # Tabla de resultados
        resultados_label = ttk.Label(main_frame, text="Resultados del análisis:")
        resultados_label.grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        
        # Frame para la tabla y scrollbar horizontal
        tabla_frame = ttk.Frame(main_frame)
        tabla_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Treeview con soporte Unicode
        self.tabla = ttk.Treeview(tabla_frame, columns=("Tipo", "Valor", "Línea", "Columna"), show="headings")
        self.tabla.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar las columnas
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.heading("Valor", text="Valor")
        self.tabla.heading("Línea", text="Línea")
        self.tabla.heading("Columna", text="Columna")
        
        # Configurar el ancho de las columnas
        self.tabla.column("Tipo", width=150)
        self.tabla.column("Valor", width=300)
        self.tabla.column("Línea", width=70)
        self.tabla.column("Columna", width=70)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.HORIZONTAL, command=self.tabla.xview)
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        self.tabla.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Hacer que el frame principal sea expandible
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def limpiar_editor(self):
        self.editor.delete(1.0, tk.END)
        for item in self.tabla.get_children():
            self.tabla.delete(item)

    def analizador_lexico(self, codigo_fuente):
        tokens = []
        posicion = 0
        linea = 1
        columna = 1
        
        while posicion < len(codigo_fuente):
            match = None
            
            for tipo_token, patron in self.TOKENS:
                regex = re.compile(patron, re.UNICODE)
                match = regex.match(codigo_fuente, posicion)
                
                if match:
                    lexema = match.group(0)
                    if tipo_token != "ESPACIO":
                        tokens.append((tipo_token, lexema, linea, columna))
                    
                    if '\n' in lexema:
                        linea += lexema.count('\n')
                        columna = len(lexema) - lexema.rindex('\n') if '\n' in lexema else columna + len(lexema)
                    else:
                        columna += len(lexema)
                    
                    posicion = match.end()
                    break
            
            if not match:
                char_error = codigo_fuente[posicion]
                raise ValueError(f"Error léxico: carácter no reconocido '{char_error}' en línea {linea}, columna {columna}")
        
        return tokens

    def analizar_codigo(self):
        # Limpiar tabla anterior
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Obtener código del editor
        codigo_fuente = self.editor.get("1.0", tk.END)
        
        try:
            # Analizar el código
            tokens = self.analizador_lexico(codigo_fuente)
            
            # Mostrar resultados en la tabla
            for tipo, valor, linea, columna in tokens:
                self.tabla.insert("", tk.END, values=(tipo, valor, linea, columna))
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = AnalizadorLexicoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()