
import json
data = []
with open('git_readme.json', 'r') as fp:
    data = json.load(fp)
readme = []
for ii in range(len(data)):
    tmp = data[ii]['readme']
    if "https://drive.google.com" in tmp:
        readme.append(tmp)

print(len(readme))
