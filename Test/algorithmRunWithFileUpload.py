import cvas

client = cvas.client("8bttfegqwfX5Do6rgHIF4t/5Eco7uYm8MoSrpn6p6S8=", "http://localhost:5000")

file = client.upload_file("lion-grayscale.jpg")

algorithm = client.algorithm("colorization")
result = algorithm.run([file])

while result.status == "notFinished":
    result.get()

print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr: " +  result.std_err)
print("Duration: " + str(result.duration) + " ms")

if result.status == "success":
    result.file.download("lion.jpg")