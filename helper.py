from datetime import datetime


def get_header(status):
    return {
        200: b"HTTP/1.0 200 OK",
        404: b"HTTP/1.0 404 OK"
    }.get(status)


def get_content_type(file):
    ext = file.split(".")[-1]
    return {
        "jpg": b"Content-Type: image/jpg",
        "jpeg": b"Content-Type: image/jpeg",
        "png": b"Content-Type: image/png",
        "html": b"Content-Type: text/html; charset=utf-8",
        "js": b"Content-Type: text/javascript; charset=utf-8"
    }.get(ext)


def get_request_type(file):
    ext = file.split(".")[-1]
    if ext in ["jpg", "jpeg", "png"]:
        return "image"
    else:
        return "text"


def dt():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")