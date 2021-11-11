from functiontesting import languageuse
from functiontesting import print_ratelimit
from functiontesting import language_count
from functiontesting import commit_file_extensions_by_year
from functiontesting import extension_list
from functiontesting import add_file
from functiontesting import find_users

#print(languageuse('marshallct', 'github-api'))
#print_ratelimit()

"""a_reaps = commit_file_names('marshallct', 'github-api')
l_counts = [('Markdown', language_count('.md',  a_reaps))
            , ('C', language_count('.c', a_reaps) + 
            language_count('.h', a_reaps))] """  
#create line 8-15 into function, give name + repo, etc
#ensures lines 9-12 gives back repository count
#get list with only extenstions, delete duplicate
print(extension_list('Python', '.py', 'marshallct'))
#create github account, invite to repo, make mods, see if data structure gives back >1 user