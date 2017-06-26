import cvas

client = cvas.client(
    "siOqZKBcJ50GYwAnJYCvh0nAFXUBCg1z7tgPBP/2ib0=", 
    "http://localhost:5000")


algorithms = [i.code_name for i in client.all_algorithms()]
for alg in algorithms:
    print(alg)