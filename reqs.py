import threading
import requests

def thread_function(url):
    print("enviando request para", url)
    response = requests.get(url)

for i in range(100):
    threading.Thread(target=thread_function, args=('http://localhost:6789/',)).start()
