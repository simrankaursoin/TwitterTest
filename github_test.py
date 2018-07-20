import requests
import json
# username of github account being accessed
username = "nedbat"

user = requests.get('https://api.github.com/users/' + username)
userItem = json.loads(user.text or user.content)
print(userItem["public_repos"], "public repos")

#repoItem is an object that contains data about all created git repositories
repos = requests.get(userItem["repos_url"])
repoItem = json.loads(repos.text)
print("List of python repo names:")
for repo in repoItem:
    # if the repo contains python, its name is printed
    if repo["language"] == "Python":
        print("\t" + repo["name"])