import json
file= open("data/candidate_profile.json")
profile= json.load(file)
print(profile ["english"])
