import cvas
import sys

client = cvas.client("8bttfegqwfX5Do6rgHIF4t/5Eco7uYm8MoSrpn6p6S8=", "localhost:5000")

with open("C:\\Users\\adamj\\OneDrive\\Study\\DP\\AlgorithmAssets\\car1.jpg", 'rb') as readFile:
    file = client.upload_data(readFile.read(), "image/jpeg", ".jpg")

if file is None:
    print("Error with uploading file from data")
    sys.exit(1)

print(file.object_id)

algorithm = client.algorithm("license-plate-recognition")
result = algorithm.run([{ "c" : "eu", "n": 1}, file])

while result.status == "notFinished":
    result.get()

print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr:" + result.std_err)
print("Duration: " + str(result.duration) + " ms")