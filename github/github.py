import os, requests, json, random
from collections import OrderedDict
from urllib import urlencode
from random import randint


def get_code_freq(user_login):

    user_repos_uri = "https://api.github.com/users/" + user_login + "/repos"
    auth_tokens = OrderedDict( [("client_id", "8407206023ef2e6fc73c"), ("client_secret", "4cc24e1534c4a0d2f1b1cee42ef3e943d9b224f1") ])


    try:
        repos = json.loads(requests.get(user_repos_uri, params=urlencode(auth_tokens)).text)
        print repos
        for index, repo in enumerate(repos):
            repo_uri = repo['full_name']
            commit_activity_uri = "https://api.github.com/repos" + "/" + repo_uri + "/stats/commit_activity"
            print
            print repo_uri
            print commit_activity_uri
            print
            commit_activity = requests.get(commit_activity_uri, params=urlencode(auth_tokens)).text
            print commit_activity


    except requests.ConnectionError:
       return "Connection Error"


print get_code_freq("rubydog")





