from tkinter import *
import customtkinter as ct
from decoder import RsaDecoder


rsa = RsaDecoder(239848036260463, 23)
root = ct.CTk()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

root.title("SMALL RSA CRACKER")
root.geometry('900x500')


button = ct.CTkButton(root, text="get p", command=rsa.get_q())

button.pack(pady=200)

root.mainloop()
