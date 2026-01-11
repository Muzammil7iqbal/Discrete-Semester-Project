import tkinter as tk
from tkinter import messagebox

# Affine Cipher keys
a = 5
b = 8
a_inverse = 21  # Multiplicative inverse of 5 mod 26

def encrypt():
    global cipher_text
    text = entry.get().upper()
    result = ""

    for char in text:
        if char.isalpha():
            x = ord(char) - 65
            enc = (a * x + b) % 26
            result += chr(enc + 65)
        else:
            result += char

    cipher_text = result
    output_label.config(text=result)

def decrypt():
    result = ""

    for char in cipher_text:
        if char.isalpha():
            y = ord(char) - 65
            dec = (a_inverse * (y - b)) % 26
            result += chr(dec + 65)
        else:
            result += char

    output_label.config(text=result)


# GUI Window
window = tk.Tk()
window.title("Affine Cipher Encryption & Decryption")
window.geometry("400x300")

tk.Label(window, text="Enter Message:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack()

tk.Button(window, text="Encrypt", command=encrypt, width=15).pack(pady=10)
tk.Button(window, text="Decrypt", command=decrypt, width=15).pack(pady=5)

tk.Label(window, text="Result:", font=("Arial", 12)).pack(pady=10)
output_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
output_label.pack()

window.mainloop()
