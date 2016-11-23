# github_issues_to_csv

### A python script to get your issues in csv format, readable in Microsoft's Excel or similar software.

## How to Use
Download or Clone the Repository and run the main.py file with [python 3](https://www.python.org/downloads/release/python-352/). Enter your repo's url (and access token in case of private repositories).
The issues will be written to a file, data.csv in the same folder.

Help for creating access_token:

https://help.github.com/articles/creating-an-access-token-for-command-line-use/

## Saving url and access token for regular use

Add your access_token and repo url to data.txt in following way.
~~~
{
    "access_token" : "6dd4afee139c08912pf212f1a09",
    "repo_link" : "https://github.com/mozilla/kuma"   
}
~~~

The access token will be saved as plain text so do not save it on a public or insecure machine.
