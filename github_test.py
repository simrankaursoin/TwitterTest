import requests
import json
username = "nedbat"
user = requests.get('https://api.github.com/users/' + username)
userItem = json.loads(user.text or user.content)
print("username: ", userItem["login"])
print(userItem["public_repos"], "public repos")
repos = requests.get(userItem["repos_url"])
repoItem = json.loads(repos.text)
print("List of python repo names:")
for repo in repoItem:
    if repo["language"] == "Python":
        print("\t" + repo["name"])