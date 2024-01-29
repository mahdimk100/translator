import tkinter as tk
from tkinter import ttk, scrolledtext
from googletrans import Translator

def translate_text():
    input_text = input_text_widget.get("1.0", tk.END)
    destination_language = destination_var.get()

    translator = Translator()
    translated_text = translator.translate(input_text, dest=destination_language).text
    
    output_text_widget.config(state=tk.NORMAL)
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.insert(tk.END, translated_text)
    output_text_widget.config(state=tk.DISABLED)

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("ترجمه کننده")

# استفاده از تم زیبا
style = ttk.Style()
style.theme_use("clam")

# ایجاد ویجت‌ها
label = ttk.Label(window, text="متن ورودی:")
label.grid(row=0, column=0, pady=10, padx=10)

input_text_widget = scrolledtext.ScrolledText(window, width=40, height=5, wrap=tk.WORD)
input_text_widget.grid(row=0, column=1, pady=10, padx=10)

label_language = ttk.Label(window, text="زبان مقصد:")
label_language.grid(row=1, column=0, pady=10, padx=10)

languages = ["en","fa", "es", "fr", "de", "zh-CN"]
destination_var = tk.StringVar()
destination_combobox = ttk.Combobox(window, textvariable=destination_var, values=languages, state="readonly")
destination_combobox.grid(row=1, column=1, pady=10, padx=10)
destination_combobox.set("en")

translate_button = ttk.Button(window, text="ترجمه", command=translate_text)
translate_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

output_label = ttk.Label(window, text="متن ترجمه شده:")
output_label.grid(row=3, column=0, pady=10, padx=10)

output_text_widget = scrolledtext.ScrolledText(window, width=40, height=5, wrap=tk.WORD, state=tk.DISABLED)
output_text_widget.grid(row=3, column=1, pady=10, padx=10)

# شروع حلقه رویداد
window.mainloop()
