import requests
import io
from PIL import Image
import json

# model = 'runwayml/stable-diffusion-v1-5', '/SG161222/Realistic_Vision_V1.4', 'prompthero/openjourney'

def detect(n, model):
    with open('huggingface_credidentials.json') as file:
        data = json.load(file)
    API_URL = "https://api-inference.huggingface.co/models/" + model
    headers = {"Authorization": data["api_key"]}
    
    prompt = "beautiful landscape, high quality"

    for i in range(0, n):
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": prompt + " " + str(i),
        })

        # Save the image to a file
        with open("genImages\GANimage" + str(i+1) + ".jpg", "wb") as file:
            file.write(image_bytes)

        # Open the image using PIL
        image = Image.open(io.BytesIO(image_bytes))
        # image.show()
        # print("Image downloaded and displayed.")

detect(5, 'runwayml/stable-diffusion-v1-5')