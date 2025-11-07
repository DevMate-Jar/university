import tkinter as tk

# DICCIONARIOS
multiplicadores = {
    "Moto": 1.5,
    "Auto": 2.0,
    "Camioneta": 3.0
}

estacionamiento = {
    "A1": {"tipo": "Auto", "patente": "ABC123", "horas": 3, "tarifa_base": 200, "pagado": False},
    "A2": {"tipo": "Moto", "patente": "XYZ789", "horas": 2, "tarifa_base": 200, "pagado": True},
    "B1": {"tipo": "Camioneta", "patente": "DEF456", "horas": 5, "tarifa_base": 200, "pagado": False},
    "B2": {"tipo": None, "patente": None, "horas": 0, "tarifa_base": 0, "pagado": False}
}

# FUNCIONES
def mostrar_estado():
    lugar = lista_lugares.get()
    datos = estacionamiento[lugar]
    texto = f"📍 Lugar: {lugar}\n"

    if datos["tipo"] is None:
        texto += "Estado: Libre\n\n"
        texto += "Podés ocupar este lugar llenando los campos abajo"
    else:
        tipo = datos["tipo"]
        patente = datos["patente"]
        horas = datos["horas"]
        tarifa = datos["tarifa_base"]
        pagado = "Sí" if datos["pagado"] else "No"
        multiplicador = multiplicadores.get(tipo, 1.0)
        total = horas * tarifa * multiplicador
        texto += f"Tipo: {tipo}\n"
        texto += f"Patente: {patente}\n"
        texto += f"Horas: {horas}\n"
        texto += f"Tarifa base: ${tarifa}\n"
        texto += f"Total: ${total}\n"
        texto += f"Pagado: {pagado}\n"
    resultado.set(texto)

def ocupar_lugar():
    lugar = lista_lugares.get()
    if estacionamiento[lugar]["tipo"] is not None:
        resultado.set("Ese lugar ya está ocupado.")
        return

    tipo = entry_tipo.get().capitalize()
    patente = entry_patente.get().upper()
    try:
        horas = int(entry_horas.get())
    except ValueError:
        resultado.set("Ingresa un número valido para las horas")
        return

    pagado = var_pagado.get()
    if tipo not in multiplicadores:
        resultado.set("Tipo invalido, solamente se permiten autos, motos y camionetas!")
        return

    estacionamiento[lugar] = {
        "tipo": tipo,
        "patente": patente,
        "horas": horas,
        "tarifa_base": 200,
        "pagado": pagado
    }

    resultado.set(f"✅ El lugar {lugar} se ha ocupado correctamente")
    mostrar_estado()

def marcar_pagado():
    lugar = lista_lugares.get()
    if estacionamiento[lugar]["tipo"] is None:
        resultado.set("Ese lugar esta libre")
        return
    estacionamiento[lugar]["pagado"] = True
    resultado.set(f"💳 El lugar {lugar} se pago correctamente")
    mostrar_estado()

def liberar_lugar():
    lugar = lista_lugares.get()
    estacionamiento[lugar] = {
        "tipo": None,
        "patente": None,
        "horas": 0,
        "tarifa_base": 0,
        "pagado": False
    }
    resultado.set(f"El lugar {lugar} ha sido liberado correctamente")
    mostrar_estado()

# INTERFAZ TKINTER
ventana = tk.Tk()
ventana.title("Sistema de Estacionamiento")
ventana.geometry("480x580")

tk.Label(ventana, text="Estacionamiento - Control de Lugares", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(ventana, text="Selecciona un lugar:").pack()
lista_lugares = tk.StringVar(ventana)
lista_lugares.set(list(estacionamiento.keys())[0])
tk.OptionMenu(ventana, lista_lugares, *estacionamiento.keys()).pack(pady=5)

tk.Button(ventana, text="Mostrar estado", command=mostrar_estado).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", font=("Arial", 10)).pack(pady=10)

frame_form = tk.LabelFrame(ventana, text="Ocupar lugar libre", padx=10, pady=10)
frame_form.pack(pady=10, fill="x", padx=10)

tk.Label(frame_form, text="Tipo (Moto/Auto/Camioneta):").grid(row=0, column=0, sticky="w")
entry_tipo = tk.Entry(frame_form)
entry_tipo.grid(row=0, column=1)

tk.Label(frame_form, text="Patente:").grid(row=1, column=0, sticky="w")
entry_patente = tk.Entry(frame_form)
entry_patente.grid(row=1, column=1)

tk.Label(frame_form, text="Horas:").grid(row=2, column=0, sticky="w")
entry_horas = tk.Entry(frame_form)
entry_horas.grid(row=2, column=1)

var_pagado = tk.BooleanVar()
tk.Checkbutton(frame_form, text="Pagado", variable=var_pagado).grid(row=3, columnspan=2)

tk.Button(frame_form, text="Ocupar lugar", command=ocupar_lugar).grid(row=4, columnspan=2, pady=5)

tk.Button(ventana, text="Marcar como pagado", command=marcar_pagado).pack(pady=5)
tk.Button(ventana, text="Liberar lugar", command=liberar_lugar).pack(pady=5)

mostrar_estado()
ventana.mainloop()
