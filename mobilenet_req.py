import requests

# TODO: Change this to your image path
image_path = "./dog.png"


url = "http://127.0.0.1:8000"

while True:
    files = {"image": open(image_path, "rb")}

    response = requests.post(url, files=files)
    print(response.text)
