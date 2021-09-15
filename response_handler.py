import os


class ResposeHandler:
    def __init__(self, path):
        self.path = path
        self.supported_requests = ["js", "html", "jpeg", "jpg", "png"]

    def exists(self, filename):
        return True if os.path.isfile(f'{self.path}/{filename}') else False

    @staticmethod
    def get_ext(file):
        ext = file.split(".")[-1]
        return ext

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
        data = open(f'{self.path}/{file}', 'r')
        return data.read()

    def build_response(self, file):
        ext = self.get_ext(file)
        if not self.exists(file):
            response = 'HTTP/1.0 404 OK\r\n' \
                       'Content-Type: text/html\r\n\r\n' + \
                       self.get_text_data("404.html")
            return response.encode("utf-8")

        if ext == "jpeg":
            data = self.get_image_data(file)
            return b'\r\n'.join([
                b"HTTP/1.0 200 OK",
                b"Connection: close",
                b"Content-Type: image/jpeg",
                bytes("Content-Length: %s" % len(data), 'utf-8'),
                b'', data
            ])

        if ext == "html":
            response = 'HTTP/1.0 200 OK\r\n'\
                       'Content-Type: text/html\r\n\r\n'+\
                       self.get_text_data(file)
            return response.encode("utf-8")


