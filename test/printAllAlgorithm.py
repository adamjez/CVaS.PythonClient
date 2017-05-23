import cvas

client = cvas.client(
    "fpfGmGL99O+3bM1BpV8vSQLeHxxocf+IeLMcKHFwfXU=", 
    "http://localhost:5000")


algorithms = [i.code_name for i in client.all_algorithms()]
print(algorithms)