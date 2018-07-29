import requests
import json
import datetime
from secure2 import USER, PASS
# secure2.py contains username and password for API auth

#now is today's date and time
now = datetime.datetime.now()

# username of github account being accessed
username = "nedbat"

#repoItem is an object that contains data about all created git repositories
repos = requests.get("/".join(["https://api.github.com/users", username, "repos"]), auth=(USER, PASS))
repoItem = json.loads(repos.text)

print('list of python repos that have had commits within this month')
for repo in repoItem:
    languages = requests.get(repo["languages_url"], auth=(USER, PASS))
    languageItem = json.loads(languages.text)
    if "Python" in languageItem:
        commits = requests.get("/".join(["https://api.github.com/repos", username, repo["name"], "commits"]), auth=(USER, PASS))
        commitsItem = json.loads(commits.text)
        for item in commitsItem:
            commit_month = item["commit"]["committer"]["date"][:7]
            current_month = str(now)[:7]
            break
        #compares most recent commit year/month to current year/month
        if commit_month == current_month:
            print(repo["name"])