import cvas

client = cvas.client("C7ehCe6XNK+GmTp/2Ld6TvZkG8T71FLtKWyTwiH+shE=", "http://cvas.azurewebsites.net")

file = client.upload_file("C:\\Users\\adamj\\OneDrive\\Study\\DP\\AlgorithmAssets\\car1.jpg")
print(file.object_id)

algorithm = client.algorithm("license-plate-recognition")
result = algorithm.run([{ "c" : "eu", "n": "2"}, file])

while result.status == "notFinished":
    result.get()

print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr:" + result.std_err)
print("Duration: " + str(result.duration) + " ms")