import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# ============================
# Cryptography Cipher Functions
# ============================


def vigenere_encrypt(plaintext, key):
    """
    Encrypt plaintext using Vigenere Cipher
    """
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            shift = ord(key[i % key_length]) - ord("A")
            cipher_char = chr(
                ((ord(letter.upper()) - ord("A") + shift) % 26) + ord("A")
            )
            ciphertext += cipher_char
        else:
            ciphertext += letter
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Vigenere Cipher
    """
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            shift = ord(key[i % key_length]) - ord("A")
            plain_char = chr(
                ((ord(letter.upper()) - ord("A") - shift + 26) % 26) + ord("A")
            )
            plaintext += plain_char
        else:
            plaintext += letter
    return plaintext


# TODO: Add Playfair and Hill cipher implementations here


# ============================
# File Upload Handler
# ============================
def upload_file():
    """
    Function to upload a .txt file and load its content into the text box.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_entry.delete(1.0, tk.END)  # Clear the text box
            text_entry.insert(
                tk.END, file.read()
            )  # Insert the file content into the text box


# ============================
# Encryption/Decryption Handler
# ============================
def process_cipher(action):
    """
    Process the cipher based on the selected mode (Encrypt or Decrypt)
    and the selected cipher type (Vigenere, Playfair, Hill).
    """
    key = key_entry.get()
    if len(key) < 12:
        messagebox.showwarning(
            "Invalid Key", "Key must be at least 12 characters long!"
        )
        return

    text = text_entry.get(1.0, tk.END).strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter or upload some text.")
        return

    cipher = cipher_choice.get()

    if action == "Encrypt":
        if cipher == "Vigenere":
            result = vigenere_encrypt(text, key)
        # TODO: Add Playfair and Hill encryption conditions here
    else:  # Decrypt
        if cipher == "Vigenere":
            result = vigenere_decrypt(text, key)
        # TODO: Add Playfair and Hill decryption conditions here

    result_entry.delete(1.0, tk.END)  # Clear previous result
    result_entry.insert(tk.END, result)  # Display new result


# ============================
# GUI Setup with Tkinter
# ============================

# Create the main window
root = tk.Tk()
root.title("Cryptography Quiz: Vigenere, Playfair, Hill Ciphers")
root.geometry("600x500")
root.configure(bg="#f0f4f8")  # Light background color

# Header Label
header_label = tk.Label(
    root, text="Cryptography Ciphers", font=("Helvetica", 16), bg="#f0f4f8", fg="#333"
)
header_label.pack(pady=10)

# Plaintext / Ciphertext Input
tk.Label(root, text="Plaintext / Ciphertext:", bg="#f0f4f8", fg="#333").pack()
text_entry = tk.Text(root, height=8, width=50, padx=10, pady=5, font=("Courier", 12))
text_entry.pack(pady=5)

# Upload File Button
upload_button = tk.Button(
    root,
    text="Upload File",
    command=upload_file,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
)
upload_button.pack(pady=5)

# Key Input
tk.Label(root, text="Key (min 12 characters):", bg="#f0f4f8", fg="#333").pack()
key_entry = tk.Entry(root, font=("Courier", 12), width=40)
key_entry.pack(pady=5)

# Cipher Choice (Radio Buttons)
cipher_choice = tk.StringVar(value="Vigenere")
tk.Label(root, text="Choose a Cipher:", bg="#f0f4f8", fg="#333").pack()

cipher_frame = tk.Frame(root, bg="#f0f4f8")
cipher_frame.pack()

tk.Radiobutton(
    cipher_frame,
    text="Vigenere Cipher",
    variable=cipher_choice,
    value="Vigenere",
    bg="#f0f4f8",
).pack(side=tk.LEFT)
tk.Radiobutton(
    cipher_frame,
    text="Playfair Cipher",
    variable=cipher_choice,
    value="Playfair",
    bg="#f0f4f8",
).pack(side=tk.LEFT)
tk.Radiobutton(
    cipher_frame, text="Hill Cipher", variable=cipher_choice, value="Hill", bg="#f0f4f8"
).pack(side=tk.LEFT)

# Encrypt / Decrypt Buttons
action_frame = tk.Frame(root, bg="#f0f4f8")
action_frame.pack(pady=10)

encrypt_button = tk.Button(
    action_frame,
    text="Encrypt",
    command=lambda: process_cipher("Encrypt"),
    bg="#2196F3",
    fg="white",
    padx=15,
    pady=5,
)
encrypt_button.pack(side=tk.LEFT, padx=10)

decrypt_button = tk.Button(
    action_frame,
    text="Decrypt",
    command=lambda: process_cipher("Decrypt"),
    bg="#FF5722",
    fg="white",
    padx=15,
    pady=5,
)
decrypt_button.pack(side=tk.LEFT, padx=10)

# Result Display
tk.Label(root, text="Result:", bg="#f0f4f8", fg="#333").pack()
result_entry = tk.Text(
    root, height=8, width=50, padx=10, pady=5, font=("Courier", 12), bg="#e8f0fe"
)
result_entry.pack(pady=5)

# Run the application
root.mainloop()
