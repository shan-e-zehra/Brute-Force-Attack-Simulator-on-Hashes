import tkinter as tk
from tkinter import messagebox
from hash_utils import generate_hash
from dictionary_attack import dictionary_attack
from brute_force import brute_force_attack

def run_attack():
    password = entry_password.get()
    algorithm = algo_var.get()
    attack = attack_var.get()
    use_salt = salt_var.get()

    if password == "":
        messagebox.showerror("Error", "Password required")
        return

    salt = "X9@!" if use_salt else ""
    hashed = generate_hash(password, algorithm, salt)

    result_label.config(text="Stored Hash:\n" + hashed)

    if attack == "Dictionary":
        result, t = dictionary_attack(hashed, algorithm, salt)
    else:
        result, t = brute_force_attack(hashed, algorithm, salt)

    if result:
        output_label.config(
            text=f"Password Cracked!\nPassword: {result}\nTime: {round(t,2)} sec",
            fg="green"
        )
    else:
        output_label.config(
            text="Password NOT cracked\n(Strong or Salted Password)",
            fg="red"
        )

# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("Brute Force Attack Simulator")
root.geometry("520x420")
root.resizable(False, False)

tk.Label(root, text="Brute Force Attack Simulator on Hashes",
         font=("Arial", 14, "bold")).pack(pady=10)

# Password
tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

# Hash Algorithm
tk.Label(root, text="Select Hash Algorithm:").pack()
algo_var = tk.StringVar(value="md5")
tk.Radiobutton(root, text="MD5 (Weak)", variable=algo_var, value="md5").pack()
tk.Radiobutton(root, text="SHA-256 (Strong)", variable=algo_var, value="sha256").pack()

# Attack Type
tk.Label(root, text="Select Attack Type:").pack(pady=5)
attack_var = tk.StringVar(value="Dictionary")
tk.Radiobutton(root, text="Dictionary Attack", variable=attack_var, value="Dictionary").pack()
tk.Radiobutton(root, text="Brute Force Attack", variable=attack_var, value="Brute").pack()

# Salt Option
salt_var = tk.BooleanVar()
tk.Checkbutton(root, text="Use Salt", variable=salt_var).pack(pady=5)

# Button
tk.Button(root, text="Start Attack", command=run_attack,
          bg="black", fg="white", width=20).pack(pady=10)

# Result
result_label = tk.Label(root, text="", wraplength=480)
result_label.pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 11))
output_label.pack(pady=10)

root.mainloop()
