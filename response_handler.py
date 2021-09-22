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

    def get_data(self, file):
        data = open(f'{self.path}/{file}', 'rb')
        return data.read()

    def get_response(self, file, status):
        data = self.get_data(file)
        return b'\r\n'.join([
                helper.get_header(status),
                helper.get_content_type(file),
                bytes("Content-Length: %s" % len(data), 'utf-8'),
                helper.get_date(),
                b"Connection: close",
                b'', data
            ])

    def build_response(self, file):
        dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f'{dt} | {file}')
        if not self.exists(file):
            status = 404
            file = "404.html"
        else:
            status = 200
        return self.get_response(file, status)
