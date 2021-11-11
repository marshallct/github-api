from datetime import datetime
import requests
import json
import base64


username = 'marshallct'
token = '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'
login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))
headers = {"Authorization": "token " + token}
login1 = requests.get("https://api.github.com/user", headers=headers)
#add the metadata for login1
print('Rate limit is ' + login1.headers['X-RateLimit-Limit'])
#add rate limit data and write to console


repo_user = input("Please enter the username of the repo: ")
repo_name = input("Please enter the repo name: ")
repo_year = input("Please enter the year of block: ")
repo_month = input("Please enter the month of block: ")
repo_day = input("Please enter the day of block: ")

req = requests.get('https://api.github.com/repos/' + repo_user + '/' + repo_name + "/commits", headers=headers)
print('Rate limit remaining is ' + req.headers['X-RateLimit-Remaining'])
dt_of_commit = datetime.strptime(req.json()[0]['commit']['committer']['date'],"%Y-%m-%dT%H:%M:%SZ")
yr_of_block = dt_of_commit.strftime("%Y")
mth_of_block = dt_of_commit.strftime("%m")
day_of_block = dt_of_commit.strftime("%d")

repo_list = requests.get('https://api.github.com/users/' + repo_user + '/repos').json()
for i in repo_list:
    name_of_repo = i['commits_url']

totalfiles = 0
#finds the file name extension
all_files = []
repo_names1 = name_of_repo.replace('{/sha}', "")
repo_names = requests.get(repo_names1, headers=headers).json()
print(name_of_repo)
print(repo_names)
"""commit_list = requests.get(str(name_of_repo) + '/commits').json()"""
if yr_of_block == repo_year or repo_year == '0' and mth_of_block == repo_month or repo_month == '0' and day_of_block == repo_day or repo_day == '0':
    print("Grabbing files")
    for key in repo_names:
        get_url = requests.get(key['commit']['tree']['url']).json()
        commit1 = get_url['tree']
        for key in commit1:
            if key['type'] == 'tree':
                for i in key:
                    i = requests.get(key['url']).json()
                    commit3 = i['tree']
                    for key in commit3:
                        print(key)
                        if key['type'] == 'tree':
                            commit4 = requests.get(key['url']).json()
                            commit5 = commit4['tree']
                            for key in commit5:
                                all_files.append(key['path'])
                                totalfiles += 1
                                if totalfiles % 10 == 0:
                                    print("Grabbing file number" + str(totalfiles))
                                else:
                                    break
                        elif key['type'] == 'blob':
                            all_files.append(key['path'])
                        else:
                            break
            elif key['type'] == 'blob':
                all_files.append(key['path'])
                totalfiles += 1
                if totalfiles % 5 == 0:
                    print("Grabbing file " + str(totalfiles))
            else:
                break
    print("All files have been grabbed")

def languagecounter(filename):
    files = []
    for file in all_files:
        if filename in file:
            files.append(file)
    return len(files)
    
#counts number of files
print("Counting total number of files")
py_files = []
for files in all_files:
    if '.py' in files:
        py_files.append(files)
if len(py_files) > 0:
    print('Python has been committed ' + str(len(py_files)) + ' times.')
jav_files = []
for files in all_files:
    if '.java' in files:
        jav_files.append(files)
if len(jav_files) > 0:
    print('Java has been committed ' + str(len(jav_files)) + ' times.')
ymd_files = []
for files in all_files:
    if '.ymd' in files:
        ymd_files.append(files)
if len(ymd_files) > 0:
    print(' has been committed ' + str(len(ymd_files)) + ' times.')
c_files = []
for files in all_files:
    if '.h' in files:
        c_files.append(files)
if len(c_files) > 0:
    print('C has been committed ' + str(len(c_files)) + ' times.')
hs_files = []
for files in all_files:
    if '.hs' in files:
        hs_files.append(files)
if len(hs_files) > 0:
    print('Haskell has been committed ' + str(len(hs_files)) + ' times.')
cs_files = []
for files in all_files:
    if '.cs' in files:
        cs_files.append(files)
if len(cs_files) > 0:
    print('C# has been committed ' + str(len(cs_files)) + ' times.')
cpp_files = []
for files in all_files:
    if '.cpp' in files:
        cpp_files.append(files)
if len(cpp_files) > 0:
    print('C++ has been committed ' + str(len(cpp_files)) + ' times.')
js_files = []
for files in all_files:
    if '.js' in files:
        js_files.append(files)
if len(js_files) > 0:
    print('JavaScript has been committed ' + str(len(js_files)) + ' times.')
php_files = []
for files in all_files:
    if '.php' in files:
        php_files.append(files)
if len(php_files) > 0:
    print('PHP has been committed ' + str(len(php_files)) + ' times.')
rb_files = []
for files in all_files:
    if '.rb' in files:
        rb_files.append(files)
if len(rb_files) > 0:
    print('Ruby has been committed ' + str(len(rb_files)) + ' times.')
r_files = []
for files in all_files:
    if '.r' in files:
        r_files.append(files)
if len(r_files) > 0:
    print('R has been committed ' + str(len(r_files)) + ' times.')


