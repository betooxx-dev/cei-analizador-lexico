"""Ventana principal de la aplicación"""
import tkinter as tk
from tkinter import ttk, messagebox
from gui.components import CodeEditor, ResultTable
from lexer import LexicalAnalyzer

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")
        self.root.geometry("800x600")
        
        self.lexical_analyzer = LexicalAnalyzer()
        self._setup_ui()
        
    def _setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Editor
        editor_label = ttk.Label(main_frame, text="Código fuente:")
        editor_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.editor = CodeEditor(main_frame)
        self.editor.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(button_frame, text="Analizar", command=self._analyze_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self._clear_all).pack(side=tk.LEFT, padx=5)
        
        # Tabla de resultados
        ttk.Label(main_frame, text="Resultados del análisis:").grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        
        # Frame para la tabla y scrollbars
        tabla_frame = ttk.Frame(main_frame)
        tabla_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.result_table = ResultTable(tabla_frame)
        self.result_table.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=self.result_table.yview)
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.HORIZONTAL, command=self.result_table.xview)
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        self.result_table.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Configuración de expansión
        self._setup_grid_weights(main_frame, tabla_frame)
        
    def _setup_grid_weights(self, main_frame, tabla_frame):
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def _clear_all(self):
        self.editor.clear()
        self.result_table.clear()
        
    def _analyze_code(self):
        self.result_table.clear()
        source_code = self.editor.get("1.0", tk.END)
        
        try:
            tokens = self.lexical_analyzer.analyze(source_code)
            for token_type, value, line, column in tokens:
                self.result_table.add_token(token_type, value, line, column)
        except ValueError as e:
            messagebox.showerror("Error", str(e))