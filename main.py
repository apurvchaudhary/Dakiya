import tkinter as tk
import tkinter.scrolledtext as scroll_text
from tkinter import END

import requests

from constants import ERRORS, METHOD_LIST
from response_processor import ResponseProcessor


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
        self.button1 = tk.Button(text="Send", command=self.pre_check)
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

    def pre_check(self):
        """
        check before calling request
        :return: errors or method_check()
        """
        _method = self.var.get()
        _url = self.entry_field1.get()
        if not _url:
            return ResponseProcessor.show_error_box(title="Empty url", error=ERRORS["INVALID_URL"])
        if _method not in METHOD_LIST:
            return ResponseProcessor.show_error_box(title="http method type not found",
                                                    error=ERRORS["METHOD_NOT_SUPPLIED"])
        return self.method_check(_method, _url)

    def method_check(self, _method, _url):
        """
        method call on send
        :return: show_output()
        """

        if _method == "get":
            _response = self.get_method(_url)
            return self.show_output(_response)
        elif _method == "post":
            _response = self.post_method(_url)
            return self.show_output(_response)

    @staticmethod
    def get_method(url):
        response_processor = ResponseProcessor()
        try:
            _response = requests.get(str(url))
        except Exception as e:
            return ResponseProcessor.show_error_box(title="error in get request", error=e)
        else:
            return response_processor.process_response(_response=_response)

    @staticmethod
    def post_method(url):
        response_processor = ResponseProcessor()
        try:
            _response = requests.post(str(url))
        except Exception as e:
            return ResponseProcessor.show_error_box(title="error in post request", error=e)
        else:
            return response_processor.process_response(_response=_response)


Dakiya()
