import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import uuid

class FacturacionTiendaBarrio:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Facturación Electronica Simple")
        self.ventana.geometry("500x600")

        # Datos del comercio
        tk.Label(self.ventana, text="DATOS DEL COMERCIO").pack()
        
        tk.Label(self.ventana, text="Nombre Comercio:").pack()
        self.nombre_comercio = tk.Entry(self.ventana, width=50)
        self.nombre_comercio.pack()

        tk.Label(self.ventana, text="NIT:").pack()
        self.nit_comercio = tk.Entry(self.ventana, width=50)
        self.nit_comercio.pack()

        tk.Label(self.ventana, text="Direccion:").pack()
        self.nit_comercio = tk.Entry(self.ventana, width=50)
        self.nit_comercio.pack()

        tk.Label(self.ventana, text="Telefono:").pack()
        self.nit_comercio = tk.Entry(self.ventana, width=50)
        self.nit_comercio.pack()

        # Datos del comprador
        tk.Label(self.ventana, text="DATOS DEL COMPRADOR").pack()
        
        tk.Label(self.ventana, text="Nombre Comprador:").pack()
        self.nombre_comprador = tk.Entry(self.ventana, width=50)
        self.nombre_comprador.pack()

        tk.Label(self.ventana, text="Número Documento:").pack()
        self.documento_comprador = tk.Entry(self.ventana, width=50)
        self.documento_comprador.pack()

        tk.Label(self.ventana, text="Numero Telefonico:").pack()
        self.documento_comprador = tk.Entry(self.ventana, width=50)
        self.documento_comprador.pack()

        # Detalles de compra
        tk.Label(self.ventana, text="DETALLES DE COMPRA").pack()
        
        tk.Label(self.ventana, text="Producto:").pack()
        self.producto = tk.Entry(self.ventana, width=50)
        self.producto.pack()

        tk.Label(self.ventana, text="Precio:").pack()
        self.precio = tk.Entry(self.ventana, width=50)
        self.precio.pack()

        # Métodos de pago
        tk.Label(self.ventana, text="Método de Pago:").pack()
        self.metodo_pago = tk.StringVar()
        metodos = ["Efectivo", "Transferencia", "Datafono", "PSE"]
        for metodo in metodos:
            tk.Radiobutton(self.ventana, text=metodo, 
                           variable=self.metodo_pago, 
                           value=metodo).pack()

        # Botón generar factura
        tk.Button(self.ventana, text="Generar Factura", 
                  command=self.generar_factura).pack()

    def calcular_iva(self, producto, precio):
        # Mismo método de cálculo de IVA anterior
        productos_excluidos = [
            'arroz', 'pan', 'huevos', 'leche', 
            'frutas', 'verduras', 'medicamentos'
        ]
        
        productos_iva_reducido = [
            'libros', 'computadores', 'tabletas'
        ]
        
        if producto.lower() in productos_excluidos:
            return 0
        elif producto.lower() in productos_iva_reducido:
            return precio * 0.05
        else:
            return precio * 0.19

    def generar_factura(self):
        # Validación de campos
        if not all([
            self.nombre_comercio.get(), 
            self.nit_comercio.get(),
            self.nombre_comprador.get(),
            self.documento_comprador.get(),
            self.producto.get(),
            self.precio.get(),
            self.metodo_pago.get()
        ]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Cálculo de valores
        precio = float(self.precio.get())
        iva = self.calcular_iva(self.producto.get(), precio)
        total = precio + iva

        # Generación de factura
        factura = f"""
FACTURA ELECTRÓNICA
-------------------
Comercio: {self.nombre_comercio.get()}
NIT: {self.nit_comercio.get()}

Cliente: {self.nombre_comprador.get()}
Documento: {self.documento_comprador.get()}

Producto: {self.producto.get()}
Precio: ${precio:,.0f}
IVA: ${iva:,.0f}
TOTAL: ${total:,.0f}

Método Pago: {self.metodo_pago.get()}
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Código Único: {uuid.uuid4()}
"""
        
        messagebox.showinfo("Factura Generada", factura)

    def iniciar(self):
        self.ventana.mainloop()

# Iniciar aplicación
app = FacturacionTiendaBarrio()
app.iniciar()