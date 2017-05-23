import cvas

client = cvas.client("fpfGmGL99O+3bM1BpV8vSQLeHxxocf+IeLMcKHFwfXU=", "http://localhost:5000")

run = client.run("0ca1edcf-a535-4c5f-7048-08d4a22cf837")
print(run.std_out)