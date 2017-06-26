import cvas
import os
import json
from PIL import Image

filename = "grayscale-black-and-white.jpg"

client = cvas.client("siOqZKBcJ50GYwAnJYCvh0nAFXUBCg1z7tgPBP/2ib0=", "http://localhost:5000")
uploadedFile = client.upload_file(filename)

algorithm = client.algorithm("face-detection")


arguments = {"input": uploadedFile, "outputType": "text"}
result = algorithm.run(arguments)

if result.status == "success":
    print("Success, cropping...")
    faces = json.loads(result.std_out)
    original = Image.open(filename)

    for index, face in enumerate(faces):
        print(face)
        cropped = original.crop((face['x'], face['y'], face['x'] + face['width'], face['y'] + face['height']))
        cropped.save('./result/' + str(index) + filename)




