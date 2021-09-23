import requests
import json

repo_user = input("Enter the name of the user: ")
repo_name = input("Enter the name of the repository: ")

total_lang = requests.get('https://api.github.com/repos/' + repo_user  + '/' + repo_name + '/languages').json()

print('The language used most in this repository is ' + max(total_lang))
print(max(total_lang) + ' has ' + str(total_lang[max(total_lang)]) + ' text characters.')
