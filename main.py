#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers ={'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")
response_dict=r.json()
print(response_dict.keys())


print(f"Liczba repos: {response_dict['total_count']}")

repo_dicts=response_dict['items']

print(f"Liczba zwróconychy repos: {len(repo_dicts)}")

repo_dict=repo_dicts[0]
print(f"\nKlucze: {len(repo_dict)}")

#for key in sorted(repo_dict.keys()):
#    print(f"{key}")
i=0
for repo in repo_dicts:
    i += 1
    print(f"\n{i}")
    print(f"Nazwa: {repo_dict['name']}")
    print(f"Właściciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Repozytorium: {repo_dict['html_url']}")
    print(f"Opis: {repo_dict['description']}")
