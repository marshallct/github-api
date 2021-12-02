from apifunction import commit_file_extensions_by_year
from apifunction import add_file
from apifunction import filter_commits_by_year
from apifunction import language_count
from apifunction import extension_list


#print(languageuse('marshallct', 'github-api'))
#print_ratelimit()

#create line 8-15 into function, give name + repo, etc
#ensures lines 9-12 gives back repository count
#get list with only extenstions, delete duplicate
cfes = commit_file_extensions_by_year('marshallct')
list_of_years = ['2021', '2020']
print(extension_list('Python', '.py', cfes, list_of_years))
print(extension_list('README', '.md', cfes, list_of_years))
#create github account, invite to repo, make mods, see if data structure gives back >1 user


#INTEGRATE PIP INSTALL
#environmental variable
