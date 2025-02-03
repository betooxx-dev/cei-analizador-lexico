"""Componentes de la interfaz gráfica"""
import tkinter as tk
from tkinter import ttk, scrolledtext

class CodeEditor(scrolledtext.ScrolledText):
    def __init__(self, parent):
        super().__init__(parent, width=70, height=10, font=('Consolas', 10))
    
    def clear(self):
        self.delete(1.0, tk.END)

class ResultTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(
            parent, 
            columns=("Tipo", "Valor", "Línea", "Columna"),
            show="headings"
        )
        self._setup_columns()
        
    def _setup_columns(self):
        # Configurar las columnas
        columns = {
            "Tipo": 150,
            "Valor": 300,
            "Línea": 70,
            "Columna": 70
        }
        
        for col, width in columns.items():
            self.heading(col, text=col)
            self.column(col, width=width)
    
    def clear(self):
        for item in self.get_children():
            self.delete(item)
            
    def add_token(self, token_type, value, line, column):
        self.insert("", tk.END, values=(token_type, value, line, column))