import os
import shutil

os.makedirs("texts", exist_ok = True)

for file in os.listdir("."):
    if file.endswith(".txt"):
        shutil.move(file, "texts/" + file)

print("all . txt files moved to 'texts' folder.")