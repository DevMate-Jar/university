import tkinter as tk

recetas = {
    "Arroz con pollo": {"Arroz": 100, "Pollo": 50, "Agua": 350, "Pimiento": 20, "Precio": 6500, "Sal": "Al gusto"},
    "Pescado frito": {"Pescado": 150, "Harina": 30, "Aceite": 50, "Limón": 10, "Precio": 11200, "Sal": "Al gusto"},
    "Sushi": {"Arroz para sushi": 80, "Alga": 1, "Salmón": 40, "Pepino": 15, "Vinagre de arroz": 10, "Precio": 15000, "Sal": "Al gusto"},
    "Fideos con bolognesa": {"Fideos": 100, "Carne picada": 80, "Salsa de tomate": 100, "Cebolla": 30, "Aceite de oliva": 10, "Precio": 9300, "Sal": "Al gusto"}
}

def calcular_receta():
    try:
        plato = lista_platos.get()
        personas = int(entrada_personas.get())
        extra = float(entrada_porcentaje.get())
        if personas < 0 or extra < 0:
            resultado.set("No se permiten valores negativos! Intentalo de vuelta")
            return
    except:
        resultado.set("Ingresa numeros validos!")
        return

    factor = (1 + personas) * (1 + extra / 100)
    receta = recetas[plato]
    texto = f"Receta de {plato} para {1 + personas} personas (+{extra}% extra):\n\n"

    for ing, cant in receta.items():
        if ing == "Precio": 
            continue
        if isinstance(cant, (int, float)):
            texto += f"{ing}: {round(cant * factor, 2)}g\n"
        else:
            texto += f"{ing}: {cant}\n"

    texto += f"\nPrecio final estimado: ${round(receta['Precio'] * factor, 2)}"
    resultado.set(texto)

def limpiar():
    resultado.set("")

ventana = tk.Tk()
ventana.title("Calculadora de Recetas")
ventana.geometry("400x480")

tk.Label(ventana, text="Plato:").pack()
lista_platos = tk.StringVar(value=list(recetas.keys())[0])
tk.OptionMenu(ventana, lista_platos, *recetas.keys()).pack(pady=5)

tk.Label(ventana, text="Personas adicionales:").pack()
entrada_personas = tk.Entry(ventana)
entrada_personas.pack(pady=5)

tk.Label(ventana, text="Porcentaje extra (%):").pack()
entrada_porcentaje = tk.Entry(ventana)
entrada_porcentaje.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular_receta).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar).pack()

resultado = tk.StringVar(value="Selecciona un plato y completa los campos.")
tk.Label(ventana, textvariable=resultado, wraplength=360, justify="left").pack(pady=10)

ventana.mainloop()
