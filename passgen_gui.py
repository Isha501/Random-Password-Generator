import tkinter as tk
import random
import string

def generate_password(length: int = 10):
    # makes sure the password can contain characters other than the mandatory one uperrcase letter, one digit and one symbol 
    if length <3:
        raise ValueError("Password must be more than 3 characters long.")
    
    # 3 different variables to store the three necessary values: uppercase letter, number and symbol
    upper_case = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbols = random.choice(string.punctuation)

    # determines the number of characters needed after generating the necessary values1
    remaining = length - 3
    # contains all the letters, digits and puncuations 
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # selects random letters, digits and punctuations from the all_chars variable for "remaining" number of times
    remaining_chars = [random.choice(all_chars) for i in range(remaining)]

    # makes the final password by joining the necessary 3 characters: upper case ltter, digit, symbol 
    # and the remaining 7 characters from the <remaining_chars> variable that randomly selects the remaining characters from <all_chars> variable 
    password = upper_case + digit + symbols + ''.join(remaining_chars)
    return password

#main password variable that will store the generated password
Password = generate_password()
print(f"The Generated Password is: {Password}")

def on_generate():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)
result_label = tk.Label(root, text="Generated Password: ")
result_label.pack(pady=5)

root.mainloop()
