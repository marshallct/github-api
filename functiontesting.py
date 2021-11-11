
from datetime import date
import requests

#Returns the age of a given user in days
def age_of_account(user_req):
    from datetime import datetime
    import requests
    import json
    req = requests.get('https://api.github.com/users/' + user_req).json()
    dt_of_creation = datetime.strptime(req['created_at'],"%Y-%m-%dT%H:%M:%SZ")
    #assigning variable names to years, months, and days
    yearofcreate = dt_of_creation.strftime("%Y")
    monthofcreate = dt_of_creation.strftime("%m")
    dayofcreate = dt_of_creation.strftime("%d")
    yr_of_account = datetime.today().year - int(yearofcreate)
    #Finds how many months account is in age
    mth_of_account = datetime.today().month - int(monthofcreate)
    if int(monthofcreate) > datetime.today().month:
        mth_of_account = int(monthofcreate) - datetime.today().month
    #Finds how many days account is in age
    day_of_account = datetime.today().day - int(dayofcreate)
    if int(dayofcreate) > datetime.today().day:
        day_of_account = int(dayofcreate) - datetime.today().day
    #Prints account username and age
    #print("Account was created  " + str(yr_of_account) + " years ago, " + str(mth_of_account) + " months ago, and " + str(day_of_account) + " days ago.")
    days_in_mth = 0
    mth_for_days = int(monthofcreate) - 1
    if yr_of_account > 0 and mth_of_account > 0:
        for i in range(0, mth_for_days):
            if mth_for_days == 2:
                days_in_mth += 28
            elif mth_for_days == 4 or mth_for_days == 6 or mth_for_days == 9 or mth_for_days == 11:
                days_in_mth += 30
            else:
                days_in_mth += 31
    else:
        if monthofcreate == '02':
            days_in_mth = 28
        elif monthofcreate == '04' or monthofcreate == '06' or monthofcreate == '09' or monthofcreate == '11':
            days_in_mth = 30
        else:
            days_in_mth = 31
    days_in_total = day_of_account + yr_of_account * 365 + days_in_mth
    #print("Account is " + str(days_in_total) + " days old in total")
    return days_in_total

#Extracts the total remaining rate limit for a user
def print_ratelimit():
    import requests
    token = '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'
    headers = {"Authorization": "token " + token}
    login1 = requests.get("https://api.github.com/user", headers=headers)
    print('Rate limit remaining is ' + login1.headers['X-RateLimit-Remaining'])

all_files = []
#Extracts all the files committed to a given repository created by a given user
def languageuse(repo_user, repo_name):
    import requests
    import json
    from datetime import datetime
    import base64
    token = "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"
    headers = {"Authorization": "token " + token}
    login = requests.get("https://api.github.com/user", headers=headers)


    req = requests.get('https://api.github.com/repos/' + repo_user + '/' + repo_name + "/commits", headers=headers)
    dt_of_commit = datetime.strptime(req.json()[0]['commit']['committer']['date'],"%Y-%m-%dT%H:%M:%SZ")
    yr_of_block = dt_of_commit.strftime("%Y")
    mth_of_block = dt_of_commit.strftime("%m")
    day_of_block = dt_of_commit.strftime("%d")

    total_files = 0
    #finds the file name extension

    commit_list = requests.get('https://api.github.com/repos/' + repo_user + '/' + repo_name + '/commits', headers=headers).json()
    print("Grabbing files")
    for key in commit_list:
        get_url = requests.get(key['commit']['tree']['url'], headers=headers).json()
        commit1 = get_url['tree']
        for key in commit1:
            if key['type'] == 'tree':
                for i in key:
                    i = requests.get(key['url'], headers=headers).json()
                    commit3 = i['tree']
                    for key in commit3:
                        if key['type'] == 'tree':
                            commit4 = requests.get(key['url'], headers=headers).json()
                            commit5 = commit4['tree']
                            for key in commit5:
                                add_file(key['path'], all_files, total_files)
                        elif key['type'] == 'blob':
                            add_file(key['path'], all_files, total_files)
            elif key['type'] == 'blob':
                add_file(key['path'], all_files, total_files)
                total_files += 1
                if total_files % 5 == 0:
                    print("Grabbing file number " + str(total_files))

    print("All files have been grabbed")
    return language_count('as')

#Increments a value each time a file is committed. If the incremented value is a multiple of 10, a trace statement is printed
def add_file(path, all_files, total_files):
    all_files.append(path)
    total_files += 1
    if total_files % 10 == 0:
        print("Grabbing file number " + str(total_files))
    return path

#Counts the amount of files present in a list.
def language_count(filename, all_files):
    files = []
    for file in all_files:
        print('file ' + str(file))
        for filess in file:
            for filesss in filess:
                print('files ' + str(filesss))
                if filename in filesss:
                    files.append(filesss)      
    return (len(files))

#Finds file name extensions of all files made in *all* the repositories of a user.
#Sorts files into two lists, made before 5 years ago, made within 5 years. 
#Gives back the two lists, no order guaranteed.
#Returns [([(Username of person who committed file, file name extension, year of commit)]       committed before 5 years
# ,        [(Username of person who committed file, file name extension, year of commit)])]     committed within 5 years
def commit_file_extensions_by_year(username):
    from datetime import datetime
    import requests
    import json
    import base64
    token = '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'
    headers = {"Authorization": "token " + token}
    login1 = requests.get("https://api.github.com/user", headers=headers)
    #add the metadata for login1
    print('Rate limit is ' + login1.headers['X-RateLimit-Limit'])
    #add rate limit data and write to console
    current_year = date.today().year

    req = requests.get('https://api.github.com/repos/' + username + "/commits", headers=headers)
    print('Rate limit remaining is ' + req.headers['X-RateLimit-Remaining'])

    repo_list = requests.get('https://api.github.com/users/' + username + '/repos', headers=headers).json()
    all_files_pre_5 = []
    all_files_post_5 = []
    total_files = 0
    for i in repo_list:
        name_of_repo = i['contributors_url']
        #finds the file name extension
        repo_names = requests.get(name_of_repo, headers=headers).json()
        for key in repo_names:
            repos_of_user = requests.get(key['repos_url'], headers=headers).json()
            for i in repos_of_user:
                commits_url1 = i['commits_url'].replace('{/sha}', '')
                commits_url = requests.get(commits_url1, headers=headers).json()
                for key in commits_url:
                    array = []
                    user_login = key['author']['login']
                    array.append(user_login)
                    year_of_repo1 = key['commit']['committer']['date']
                    year_of_repo2 = datetime.strptime(year_of_repo1,"%Y-%m-%dT%H:%M:%SZ")
                    year_of_repo = year_of_repo2.strftime("%Y")
                    array.append(year_of_repo)
                    get_url = requests.get(key['commit']['tree']['url'], headers=headers).json()
                    commit1 = get_url['tree']
                    for key in commit1:
                        if key['type'] == 'tree':
                            p = requests.get(key['url'], headers=headers).json()
                            q = p['tree']
                            for i in q:
                                if i['type'] == 'tree':
                                    commit7 = requests.get(i['url'], headers=headers).json()
                                    commit3 = requests.get(commit7['url'], headers=headers).json()
                                    commit2 = commit3['tree']
                                    for key in commit2:
                                        if key['type'] == 'tree':
                                            commit4 = requests.get(key['url'], headers=headers).json()
                                            commit5 = commit4['tree']
                                            for key in commit5:
                                                total_files += 1
                                                add_file(key['path'], array, total_files)
                                                if total_files % 10 == 0:
                                                    print("Grabbing file number " + str(total_files))
                                elif key['type'] == 'blob':
                                    total_files += 1
                                    if total_files % 10 == 0:
                                        print("Grabbing file number " + str(total_files))
                                    add_file(key['path'], array, total_files)
                        elif key['type'] == 'blob':
                            total_files += 1    
                            if total_files % 10 == 0:
                                print("Grabbing file number " + str(total_files))
                            add_file(key['path'], array, total_files)
                    if int(year_of_repo) < int(current_year) - 5:
                        all_files_pre_5.append(array)
                    else:
                        all_files_post_5.append(array)
        print("All files have been grabbed")
    return (all_files_post_5, all_files_pre_5)


tuple_list = []
"""[(Name of the language,
  Amount of files of a given language present in all repositories of a given user 
  ([Username of person who committed the file (within the last 5 years),
    the year the file was committed(within 5 years), 
    the name of the file(within 5 years)],
    [Username of person who committed the file (before 5 years ago),
    the year the file was committed (before 5 years ago),
    the name of the file (before 5 years ago)])
   )]"""
def extension_list(language_name, extension_name, username):
    cfes = commit_file_extensions_by_year(username)
    l_counts = [(language_name,
                 language_count(extension_name, cfes),
                 set(cfes)
                 )]  
    tuple_list.append(l_counts)
    print("File numbers in repository are as follows: ")
    for i in tuple_list:
        print(i)

#Returns the usernames of all users who have made a commit to all the repositories of a user
def find_users(username, repo_name):
    token = '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'
    headers = {"Authorization": "token " + token}
    login1 = requests.get("https://api.github.com/user", headers=headers)
    #print('Rate limit is ' + login1.headers['X-RateLimit-Limit'])
    url = requests.get("https://api.github.com/repos/" + username + '/' + repo_name, headers=headers).json()
    contributor_url = requests.get(url['contributors_url'], headers=headers).json()
    for i in contributor_url:
        user_url = i['login']
        return user_url




#create line 8-15 into function, give name + repo, etc
#ensures lines 9-12 gives back repository count
#Get all usernames from people who have made a commit
#Get age of account from users
#Shows age of developers working on certain projects

#Ensure code returns data structure
#Ensure code is functional when called

#Compare language use to age of accounts
#Extract more data; username for files,
#See what data can be used for, do a console output