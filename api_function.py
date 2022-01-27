from datetime import datetime
import requests
import json
import base64
#import env_var.json
#Finds file name extensions of all files made in *all* the repositories of a user.
#Returns [Year the file was committed, file name]
def commit_file_extensions_by_year(username):
    token = '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'
    headers = {"Authorization": "token " + token}
    login1 = requests.get("https://api.github.com/user", headers=headers)
    #add the metadata for login1
    print('Rate limit is ' + login1.headers['X-RateLimit-Limit'])
    #add rate limit data and write to console
    req = requests.get('https://api.github.com/repos/' + username + "/commits", headers=headers)
    print('Rate limit remaining is ' + req.headers['X-RateLimit-Remaining'])
    repo_list = requests.get('https://api.github.com/users/' + username + '/repos', headers=headers).json()
    all_files = []
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
                    year_of_repo1 = key['commit']['committer']['date']
                    year_of_repo2 = datetime.strptime(year_of_repo1,"%Y-%m-%dT%H:%M:%SZ")
                    year_of_repo = year_of_repo2.strftime("%Y")
                    array.append(year_of_repo)
                    get_url = requests.get(key['commit']['tree']['url'], headers=headers).json()
                    commit1 = get_url['tree']
                    for key in commit1:
                        if key['type'] == 'tree':
                            tree_check1 = requests.get(key['url'], headers=headers).json()
                            tree_check = tree_check1['tree']
                            for i in tree_check:
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
                                elif i['type'] == 'blob':
                                    total_files += 1
                                    if total_files % 10 == 0:
                                        print("Grabbing file number " + str(total_files))
                                    add_file(key['path'], array, total_files)
                        elif key['type'] == 'blob':
                            total_files += 1    
                            if total_files % 10 == 0:
                                print("Grabbing file number " + str(total_files))
                            add_file(key['path'], array, total_files)
                        all_files.append(array)

        print("All files have been grabbed")
    return [all_files]

#Increments a value each time a file is committed. If the incremented value is a multiple of 10, a trace statement is printed
def add_file(path, all_files, total_files):
    all_files.append(path)
    total_files += 1
    if total_files % 10 == 0:
        print("Grabbing file number " + str(total_files))
    return path

#Separates the return value from commit_file_by_year into separate years
#Returns ('All files committed for year [year] are [files committed in that year]')
def filter_commits_by_year(commit_list, year):
    list_of_files_sorted_by_year = []
    for through_list in commit_list:
        for sort_list in through_list:
            if year in sort_list:
                list_of_files_sorted_by_year.append([sort_list])
    return list_of_files_sorted_by_year

#Counts the files present in a list
def language_count(filename, all_files):
    files = []
    for file in all_files:
        for extension_iterate in file:
            for find_extension in extension_iterate:
                if filename in find_extension:
                    files.append(extension_iterate)     
    return (len(files))

#Finds the total files committed of in *all* repositories of a given user, in a given language, in given years.
#{'extension_list': [{'language_name' : Name of a given language,
#                     'year_file_committed' : The year the file was committed
#                     'language_count_files' : The amount of files committed in given language in given year
#                   }]}
files_year_number = {'extension_list' : []}
def extension_list(language_name, extension_name, cfes, years):
    for i in years:
        l_counts = {'language_name' : language_name,
                    'year_file_committed' : i,
                    'language_count_files' : language_count(extension_name, filter_commits_by_year(cfes, i))
        }
        files_year_number['extension_list'].append(l_counts)
    return files_year_number

"""Get d3 visualisation with json file
Generate file from backend code"""
#Decide and design visual to match data gathered, implement
#Decide what your data is actually for
"""break the limits of pi charting"""
