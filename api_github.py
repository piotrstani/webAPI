#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

# api_github.py
# API
#  ↓
# requests
#  ↓
# JSON
#  ↓
# repositories


import requests
import json
from typing import Any

GITHUB_API_URL = "https://api.github.com/search/repositories"
GITHUB_PARAMS = {
    "q": "language:python",
    "sort": "stars",
}
GITHUB_HEADERS = {'Accept': 'application/vnd.github.v3+json'}

# Pobierz dane z GitHuba
def get_github_response(url: str, headers: dict[str, str], params: dict[str, Any]) -> dict[str, Any]:
    try:
        http_response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )
        print(f"Kod stanu: {http_response.status_code}")
        http_response.raise_for_status()
        return http_response.json()

    except requests.Timeout:
        print("Przekroczono limit czasu połączenia z GitHub API.")
        return None

    except requests.HTTPError as exc:
        print(f"Błąd HTTP: {exc}")
        return None

    except requests.RequestException as exc:
        print(f"Błąd połączenia: {exc}")
        return None


def print_github_repos(print_response: list[dict[str, Any]]) -> None:

    print(f"Liczba repos: {print_response['total_count']}")

    repo_dicts=print_response['items']
    print(f"Liczba zwróconychy repos: {len(repo_dicts)}")
    if not repo_dicts:
        print("Brak repozytoriów.")
        return

    first_repo = repo_dicts[0]
    print(f"\nLiczba kluczy pierwszego repo: {len(first_repo)}")
    print("\nKlucze pierwszego repo:")
    for key in sorted(first_repo.keys()):
        print(f"  {key}")

    for i, repo in enumerate(repo_dicts, start=1):
        print(f"\n{i}")
        print(f"Nazwa: {repo['name']}")
        print(f"Właściciel: {repo['owner']['login']}")
        print(f"Gwiazdki: {repo['stargazers_count']}")
        print(f"Repozytorium: {repo['html_url']}")
        print(f"Opis: {repo['description']}")

# Pobierz dane z GitHuba
def get_github_repos(url: str, headers: dict[str, str], params: dict[str, Any]) -> dict[str, Any]:
    response_dict = get_github_response(
        url,
        headers,
        params
    )
    return response_dict["items"]



#

if __name__ == "__main__":
    r = get_github_response(url=GITHUB_API_URL, headers=GITHUB_HEADERS, params=GITHUB_PARAMS)
    pprint(r["items"][0])
    #print(json.dumps(r["items"][0], indent=4, ensure_ascii=False))
    #print_github_repos(r)




