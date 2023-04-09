import tkinter as tk

import time

sample_text = "Umut candan ava gitti"

root = tk.Tk()

root.title("Typing Speed Test")

def start_test():

    start_button.config(state="disabled")

    text_label.config(text=sample_text)

    typing_entry.config(state="normal")

    typing_entry.focus()

    start_time = time.time()

    def check_text():

        typed_text = typing_entry.get()

        if typed_text == sample_text:

            end_time = time.time()

            elapsed_time = end_time - start_time

            words_per_minute = int(len(sample_text.split()) / (elapsed_time / 60))

            result = f"You typed at {words_per_minute} words per minute!"

            tk.messagebox.showinfo(title="Typing Speed Test", message=result)

            typing_entry.delete(0, tk.END)

            typing_entry.config(state="disabled")

            start_button.config(state="normal")

        else:

            root.after(100, check_text)

    check_text()

text_label = tk.Label(root, wraplength=400, font=("Arial", 12))

text_label.pack(padx=10, pady=10)

typing_entry = tk.Entry(root, font=("Arial", 12), state="disabled")

typing_entry.pack(padx=10, pady=10)

start_button = tk.Button(root, text="Start", font=("Arial", 12), command=start_test)

start_button.pack(padx=10, pady=10)

root.mainloop()