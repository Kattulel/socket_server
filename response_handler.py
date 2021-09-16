import os
import helper
from datetime import datetime


class ResposeHandler:
    def __init__(self, path):
        self.path = path

    def exists(self, filename):
        return True if os.path.isfile(f'{self.path}/{filename}') else False

    @staticmethod
    def get_url_file(request):
        data = str(request).split("\\r\\n")
        for i in data:
            if "GET" and "HTTP" in i:
                path = i.split(" ")[1].strip("/")
                return path
        return None

    def get_image_data(self, file):
        data = open(f'{self.path}/{file}', 'rb')
        return data.read()

    def get_text_data(self, file):
        data = open(f'{self.path}/{file}', 'rb')
        return data.read()

    def get_image_respose(self, file, status):
        data = self.get_image_data(file)
        return b'\r\n'.join([
                helper.get_header(status),
                b"Connection: close",
                helper.get_content_type(file),
                bytes("Content-Length: %s" % len(data), 'utf-8'),
                b'', data
            ])

    def get_text_response(self, file, status):
        return b'\r\n'.join([
            helper.get_header(status),
            helper.get_content_type(file),
            b'\r\n', self.get_text_data(file)
        ])

    def build_response(self, file):
        dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if file != "favicon.ico" or file is not None:
            print(f'{dt} | {file}')
        if not self.exists(file):
            status = 404
            file = "404.html"
        else:
            status = 200

        if helper.get_request_type(file) == "text":
            return self.get_text_response(file, status)
        elif helper.get_request_type(file) == "image":
            return self.get_image_respose(file, status)
