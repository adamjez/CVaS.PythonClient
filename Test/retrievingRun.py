import cvas

client = cvas.client("C7ehCe6XNK+GmTp/2Ld6TvZkG8T71FLtKWyTwiH+shE=", "http://cvas.azurewebsites.net")

run = client.run(3)
print(run.std_out)