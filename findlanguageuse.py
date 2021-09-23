import requests
import json

test_grab = requests.get('https://api.github.com/repos/marshallct/github-api/git/trees/78f38b7a2b0e6501e8c995a309a5370e19ed0d2a')
file_name = test_grab.json()
file = file_name['tree']
file_1 = file[0]


"""repo_user = input("Please enter the username of the repo: ")
repo_name = input("Please enter the repo name: ")"""

repo_1 = requests.get("https://api.github.com/repos/marshallct/github-api/commits").json()
repo_2 = repo_1[0]
repo_3 = repo_2['commit']
repo_4 = repo_3['tree']
repo_5 = repo_4['url']
repo_6 = requests.get(repo_5).json()
repo_7 = repo_6['tree']
repo_8 = repo_7[0]
file_name = repo_8['path']
print(file_name)