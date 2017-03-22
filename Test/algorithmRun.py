import cvas

client = cvas.client("C7ehCe6XNK+GmTp/2Ld6TvZkG8T71FLtKWyTwiH+shE=", "http://cvas.azurewebsites.net")

algorithm = client.algorithm("hello-world")
result = algorithm.run(["Hello", "Darkness", "My", "Old", "Friend"], 0)

print("Result: " + result.status)
print("StdOut: " + result.std_out)
print("StdErr:" + result.std_err)
print("Duration: " + str(result.duration) + " ms")
