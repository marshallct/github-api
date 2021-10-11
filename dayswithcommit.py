import requests
import json
from datetime import date, datetime

date_link = requests.get('https://api.github.com/repos/marshallct/github-api/git/commits/4adf960da1ce2107d14bcaafb95daf37372b6c2b').json()
time_commit = datetime.strptime(date_link['committer']['date'],"%Y-%m-%dT%H:%M:%SZ")
print(time_commit.strftime("%d/%m/%Y"))