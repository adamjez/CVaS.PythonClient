import cvas
import os

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.rpartition('.')[-1] in ["jpg", "png"] ]

client = cvas.client("siOqZKBcJ50GYwAnJYCvh0nAFXUBCg1z7tgPBP/2ib0=", "http://localhost:5000")
uploadedFiles = [client.upload_file(f) for f in files]

algorithm = client.algorithm("face-detection")

for file in zip(uploadedFiles, files):
    uploadedFile, filename = file

    arguments = {"input": uploadedFile, "outputType": "image", "borderWidth": 4}
    result = algorithm.run(arguments)

    if result.std_out != "":
        print("StdOut: " + result.std_out)

    if result.status == "success":
        result.file.download("./result/" + filename)


