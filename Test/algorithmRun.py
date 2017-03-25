import cvas

client = cvas.client("zVes/1008G1YhtKNiNa0WY5ZGubLK+DYYu0g+e1hcmQ=", "http://cvas.azurewebsites.net")

algorithm = client.algorithm("hello-world")
result = algorithm.run(["Hello", "Darkness", "My", "Old", "Friend"])

print("Id: " + result.object_id)
print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr:" + result.std_err)
print("Duration: " + str(result.duration) + " ms")
