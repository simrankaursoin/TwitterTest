import requests
import json
import datetime
import csv
from secure2 import USER, PASS
# secure2.py contains username and password for API auth

# now is today's date and time
now = datetime.datetime.now()

# username of github account being accessed
username = "nedbat"

# repoItem is an object that contains data about all created git repositories
repos = requests.get("/".join(["https://api.github.com/users",
                     username, "repos"]), auth=(USER, PASS))
repoItem = json.loads(repos.text)

# make csv file
with open('repo_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name of Python Repo", "Last Commit Date"])
    for repo in repoItem:
        languages = requests.get(repo["languages_url"], auth=(USER, PASS))
        # languageItem contains a full list of all languages used in repo
        languageItem = json.loads(languages.text)
        # sorts out repos that contain Python
        if "Python" in languageItem:
            commits = requests.get("/".join(["https://api.github.com/repos",
                                   username, repo["name"], "commits"]),
                                   auth=(USER, PASS))
            commitsItem = json.loads(commits.text)
            # for each repo's commit history
            #    isolate the date of the most recent commit
            for item in commitsItem:
                commit_month = item["commit"]["committer"]["date"][:7]
                break
            # compares most recent commit year/month to current year/month
            current_month = str(now)[:7]
            last_month = current_month[:6] + str(int(current_month[6:])-1)
            if commit_month == current_month or commit_month == last_month:
                writer.writerow([repo["name"],
                                item["commit"]["committer"]["date"]])
