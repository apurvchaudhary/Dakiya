from tkinter import messagebox

INFO_MESSAGE = {
    "405": "405 wrong http method",
    "404": "404 url was not found",
    "allowed_method": "\n\nAllowed method : {allowed}"
}


class ResponseProcessor:

    @staticmethod
    def show_error_box(title, error):
        messagebox.showerror(title, error)

    @staticmethod
    def show_info_box(title, info):
        messagebox.showinfo(title, info)

    def process_response(self, _response):
        status_code = _response.status_code
        if status_code == 200:
            return _response.text
        elif status_code == 405:
            return self.show_info_box(
                title=INFO_MESSAGE["405"],
                info=_response.text + INFO_MESSAGE["allowed_method"].format(
                    allowed=_response.headers["Allow"])
            )
        elif status_code == 404:
            return self.show_error_box(title=INFO_MESSAGE["404"], error=_response.text)
