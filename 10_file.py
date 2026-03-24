# tulis file
with open("contoh.txt", "w") as f:
    f.write("Halo dunia")

# baca file
with open("contoh.txt", "r") as f:
    print(f.read())
