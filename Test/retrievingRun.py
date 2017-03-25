import cvas

client = cvas.client("zVes/1008G1YhtKNiNa0WY5ZGubLK+DYYu0g+e1hcmQ=", "http://cvas.azurewebsites.net")

run = client.run("fd15273c-6d9a-4dba-558c-08d472df7446")
print(run.std_out)