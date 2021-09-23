import requests
import json
from datetime import datetime
response = requests.get('https://api.github.com/users/marshallct')

#print(response.json()['created_at'])
#print(response.json()['login'])

user_req = input("Enter a username: ")
repo_name = input("Enter the name of the repository: ")
req = requests.get('https://api.github.com/users/' + user_req)
#print(req.json()['created_at'])

dt_of_creation = datetime.strptime(req.json()['created_at'],"%Y-%m-%dT%H:%M:%SZ")

#assigning variable names to years, months, and days
yr_of_creation = dt_of_creation.strftime("%Y")
mth_of_creation = dt_of_creation.strftime("%m")
day_of_creation = dt_of_creation.strftime("%d")

#Finds how many years the account is in age
yr_of_account = datetime.today().year - int(yr_of_creation)

#Finds how many months account is in age
mth_of_account = datetime.today().month - int(mth_of_creation)
if int(mth_of_creation) > datetime.today().month:
    mth_of_account = int(mth_of_creation) - datetime.today().month

#Finds how many days account is in age
day_of_account = datetime.today().day - int(day_of_creation)
if int(day_of_creation) > datetime.today().day:
    day_of_account = int(day_of_creation) - datetime.today().day

#Prints account username and age
print("Account username is " + req.json()['login'])
print("Account was created  " + str(yr_of_account) + " years ago, " + str(mth_of_account) + " months ago, and " + str(day_of_account) + " days ago.")


mth_days_total = 0
days_in_mth = 0

mth_for_days = int(mth_of_creation) - 1

if yr_of_account > 0 or mth_of_account > 0:
    for i in range(0, mth_for_days):
        mth_days_total += 1
        if mth_days_total == 2:
            days_in_mth += 28
        elif mth_days_total == 4 or mth_days_total == 6 or mth_days_total == 9 or mth_days_total == 11:
            days_in_mth += 30
        else:
            days_in_mth += 31


days_in_total = day_of_account + yr_of_account * 365 + days_in_mth

print("In total, account is " + str(days_in_total) + " days old.")

total_lang = requests.get('https://api.github.com/repos/' + user_req  + '/' + repo_name + '/languages').json()

print('The language used most in this repository is ' + max(total_lang))
print(max(total_lang) + ' has ' + str(total_lang[max(total_lang)]) + ' text characters.')

#Try to find account activity as a %, measure how many days since account creation has there been contributions

#Go through commits, see what changes they have made (file name extensions) to see which langauge they have used
#Change format of datetime
#Write program that takes name of developer, construct url to get account information, display certain amount of information
#Write in account name, gives back account name and age