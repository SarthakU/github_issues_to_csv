import sys

# try import request
# install it if not already installed 
try:
    import requests
except ImportError:
    print('Requests not installed!')
    permission = input('Do you want me to try install it? (Y/N): ')
    if permission.strip().lower() == "y":
        from setuptools.command.easy_install import main as install
        install(['requests'])
    print('\n Requests intalled! \n Rerun the script.')
    sys.exit()
    
import csv
import json

def print_gap(num):
    for i in range(num): 
        print('')

def print_pattern():
    print('-' * 10)

def gen_api_url(filename):
    api_url = "https://api.github.com/repos/"
    with open(filename, "r") as file:
        file_data = json.load(file)      

    try:
        repo = file_data["repo_link"]
    except KeyError:
        print_gap(1)
        # print("Repo not stored.")
        repo = input("Enter Repo link: ")
        print_gap(1)

        # TODO: Add ability to store repo link
        # input("Do you want me to store repo? (Y/N): ")

    if len(repo.split('/')[-2:]) == 1:
        print('Invalid Url')
        return 'invalid'
    else:
        api_url += '/'.join(repo.split('/')[-2:])
        return api_url

## TODO: Add params. Only supports access_token now
def add_params_to_url(api_url, filename):
    with open(filename, "r") as file:
        file_data = json.load(file)   

    try:
        access_token = file_data["access_token"]
    except KeyError:
        print_pattern()
        # print("Access token not stored.")
        print("Access token required for private github repos, if public press enter(return), enter token otherwise.")
        print("Help on creating token - https://help.github.com/articles/creating-an-access-token-for-command-line-use/")
        print_pattern()
        print_gap(1)
        access_token = input("Enter Access Token: ")
        print_gap(1)

        # TODO: Add ability to store access_token
        # input("Do you want me to store access token? (Y/N): ")


    api_url += '/issues?state=open' + '&access_token=' + access_token

    return api_url
        
        
def main():
    api_url = add_params_to_url(gen_api_url('data.txt'), 'data.txt')

    req = requests.get(api_url)
    data = req.json()

    output = open('output.txt', 'w+')
    keys = data[0].keys()
    output.write(" ".join(keys))



    fields = ['number', 'title', 'html_url']

    other = ['assignee', 'creater']

    with open("data.csv", "w") as file:
        csv_file = csv.writer(file)
        cols = fields + other
        csv_file.writerow(cols)
        for item in data:
            row = [item[i] for i in fields]
            try:
                row += [item['assignee']['login']]
            except:
                row += [' ']
            row += [item['user']['login']]
            csv_file.writerow(row)

if __name__ == "__main__":
    main()
