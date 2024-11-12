#memory model(id)
name = "python"
print(f"Address Before Changes: {id(name)}")

name += "crt"
print(f"Address After Changes: {id(name)}")