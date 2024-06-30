import tkinter as tk
from tkinter import messagebox
from decoder import RsaDecoder


def calculate_rsa():
    try:
        n = int(entry_n.get())
        e = int(entry_e.get())
    except ValueError:
        return messagebox.showerror("Invalid input", "n and e must be integers")

    rsa = RsaDecoder(n, e)

    try:
        p = rsa.get_p()
        q = rsa.get_q()
        phi = rsa.get_phi()
        d = rsa.get_d()
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
        return

    if p and q:
        result_p.set(f"p: {p}")
        result_q.set(f"q: {q}")
        result_phi.set(f"phi: {phi}")
        result_d.set(f"d: {d}")
    else:
        messagebox.showerror("Error", "No prime factors found for n")


# Create the main window
root = tk.Tk()
root.title("RSA Decoder")
root.geometry("400x300")

# Create and place the widgets
tk.Label(root, text="Enter n:").grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Label(root, text="Enter e:").grid(row=1, column=0)
entry_e = tk.Entry(root)
entry_e.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate_rsa).grid(row=2, column=0, columnspan=2)

result_p = tk.StringVar()
result_q = tk.StringVar()
result_phi = tk.StringVar()
result_d = tk.StringVar()

tk.Label(root, textvariable=result_p).grid(row=3, column=0, columnspan=2)
tk.Label(root, textvariable=result_q).grid(row=4, column=0, columnspan=2)
tk.Label(root, textvariable=result_phi).grid(row=5, column=0, columnspan=2)
tk.Label(root, textvariable=result_d).grid(row=6, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
