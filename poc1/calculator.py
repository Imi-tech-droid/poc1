import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Számológép")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Kijelző
        display_frame = tk.Frame(self.root, bg="#2c3e50")
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        display = tk.Entry(display_frame, textvariable=self.result_var,
                          font=('Arial', 24, 'bold'),
                          justify='right',
                          bd=0,
                          bg="#34495e",
                          fg="white")
        display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Gombok frame
        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Gombok elrendezése
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '0':
                    colspan = 2
                    btn = tk.Button(buttons_frame, text=btn_text,
                                  font=('Arial', 18, 'bold'),
                                  bg="#34495e",
                                  fg="white",
                                  activebackground="#1abc9c",
                                  bd=0,
                                  command=lambda x=btn_text: self.on_button_click(x))
                    btn.grid(row=i, column=j, columnspan=colspan, sticky="nsew", padx=2, pady=2)
                elif btn_text == '=':
                    btn = tk.Button(buttons_frame, text=btn_text,
                                  font=('Arial', 18, 'bold'),
                                  bg="#1abc9c",
                                  fg="white",
                                  activebackground="#16a085",
                                  bd=0,
                                  command=lambda x=btn_text: self.on_button_click(x))
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                elif btn_text in ['/', '*', '-', '+', '%']:
                    btn = tk.Button(buttons_frame, text=btn_text,
                                  font=('Arial', 18, 'bold'),
                                  bg="#e74c3c",
                                  fg="white",
                                  activebackground="#c0392b",
                                  bd=0,
                                  command=lambda x=btn_text: self.on_button_click(x))
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                elif btn_text in ['C', '⌫']:
                    btn = tk.Button(buttons_frame, text=btn_text,
                                  font=('Arial', 18, 'bold'),
                                  bg="#95a5a6",
                                  fg="white",
                                  activebackground="#7f8c8d",
                                  bd=0,
                                  command=lambda x=btn_text: self.on_button_click(x))
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                else:
                    btn = tk.Button(buttons_frame, text=btn_text,
                                  font=('Arial', 18, 'bold'),
                                  bg="#34495e",
                                  fg="white",
                                  activebackground="#1abc9c",
                                  bd=0,
                                  command=lambda x=btn_text: self.on_button_click(x))
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        # Grid súlyok beállítása
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except:
                self.result_var.set("Hiba")
                self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
