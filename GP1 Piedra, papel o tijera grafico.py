import random
import tkinter as tk

Choices = ["piedra", "papel", "tijera"]

# función que ejecuta el juego
def jugar(player):

    oponente = random.choice(Choices)

    if player == oponente:
        resultado = "Es un empate!"

    elif (player == "piedra" and oponente == "tijera") or \
         (player == "papel" and oponente == "piedra") or \
         (player == "tijera" and oponente == "papel"):

        resultado = "¡Tú ganas!"

    else:
        resultado = "El oponente gana!"

    resultado_label.config(
        text=f"Tú escogiste: {player}\nEl oponente escogió: {oponente}\n{resultado}"
    )


# crear ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("300x200")

# texto superior
label = tk.Label(ventana, text="Vamos a jugar")
label.pack(pady=10)

# botones
boton_piedra = tk.Button(ventana, text="Piedra", command=lambda: jugar("piedra"))
boton_papel = tk.Button(ventana, text="Papel", command=lambda: jugar("papel"))
boton_tijera = tk.Button(ventana, text="Tijera", command=lambda: jugar("tijera"))

boton_piedra.pack()
boton_papel.pack()
boton_tijera.pack()

# etiqueta donde aparece el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=10)

# iniciar interfaz
ventana.mainloop()