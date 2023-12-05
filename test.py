import os

path = "static/styles/audios/songs"
files = os.listdir(path)

for file in files:
    print(file)