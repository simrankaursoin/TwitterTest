import requests
import json
# username of github account being accessed
username = "simrankaursoin"
user = requests.get('https://api.github.com/users/' + username)
userItem = json.loads(user.text)
print(userItem["public_repos"], "public repos")

#repoItem is an object that contains data about all created git repositories
repos = requests.get(userItem["repos_url"])
repoItem = json.loads(repos.text)
print("List of python repo names:")
for repo in repoItem:
    languages = requests.get(repo["languages_url"])
    languageItem = json.loads(languages.text)
    if "Python" in languageItem:
        print(repo["name"])