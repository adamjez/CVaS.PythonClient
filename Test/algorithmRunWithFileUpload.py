import cvas
import time

client = cvas.client(
    "fpfGmGL99O+3bM1BpV8vSQLeHxxocf+IeLMcKHFwfXU=", 
    "http://localhost:5000")

file = client.upload_file("grayscale.jpg")

algorithm = client.algorithm("colorization")
result = algorithm.run([file])

while result.status == "notFinished":
    time.sleep(1)
    result.get()

print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr: " +  result.std_err)
print("Duration: " + str(result.duration) + " ms")

if result.status == "success":
    result.file.download("colorized.jpg")