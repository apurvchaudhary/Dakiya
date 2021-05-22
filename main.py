import tkinter as tk
import tkinter.scrolledtext as scroll_text
from tkinter import END

import requests


class Dakiya:
    """
    class to create gui of dakiya for http method processing
    """

    def __init__(self):
        # main tk object initialization
        self.main_window = tk.Tk()
        self.main_window.title("Dakiya © 2021 by Apurv Chaudhary")
        self.main_window.attributes("-zoomed", True)
        self.main_window.iconify()
        self.main_window.configure(bg='#99738E')

        # url entry field
        self.label1 = tk.Label(text="URL : ", bg='#242582', fg='white')
        self.label1.grid(row=1, sticky="w", padx=10, pady=5)
        self.entry_field1 = tk.Entry(width=80, bg='#F64C72', fg='white')
        self.entry_field1.grid(row=2, sticky="w", padx=10, pady=5)

        # option dropdown
        self.var = tk.StringVar(self.main_window)
        self.var.set("type")
        self.option = tk.OptionMenu(self.main_window, self.var, "post", "get")
        self.option.config(bg='#553D67', fg='white')
        self.option.grid(row=5, stick="W", padx=10, pady=10)

        # submit button
        self.button1 = tk.Button(text="Send", command=self.pre_call_check)
        self.button1.config(bg='#553D67', fg='white')
        self.button1.grid(row=7, sticky="W", padx=10, pady=10)

        # output
        self.output_label = tk.Label(text="Response : ", bg='#242582', fg='white')
        self.output_label.grid(row=9, sticky="w", padx=10, pady=5)
        self.text = scroll_text.ScrolledText(self.main_window, height=40, width=200, fg="blue")
        self.text['font'] = ('Helvetica', '12')
        self.text.grid(row=10, sticky="W", padx=15, pady=5)

        self.main_window.mainloop()

    def show_output(self, output):
        """
        method to show output in label in gui
        :param output: response
        :return: text output
        """
        self.text.delete("1.0", END)
        self.text.insert(END, output)

    def pre_call_check(self):
        """
        method call on send
        :return: method
        """
        if self.var.get() == "get":
            _response = self.get_method(self.entry_field1.get())
            return self.show_output(_response)

    @staticmethod
    def get_method(url):
        """
        when user submit get request, calling get_method
        :return: get response
        """
        _response = requests.get(str(url))
        if _response.status_code == 200:
            return _response.text
        return "Some error"


Dakiya()
