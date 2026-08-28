import requests
#from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers ={'Accept': 'application/vnd.github.v3+json'}
response = requests.get(url, headers=headers, timeout=10)
print(f"Kod stanu: {response.status_code}")
response.raise_for_status()

response_dict = response.json()
repo_dicts = response_dict['items']


def github_repos_stars(repositories):
    repo_links, stars, labels = [], [], []
    for repo_dict in repositories:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        # Podpowiedzi
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # Wizualizacja
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width': 1.5, 'color': 'rgb(60,100,150)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': {
            'text': 'Projekty python z największą liczbą gwiadek',
            'font': {'size': 28},
        },
        'xaxis': {
            'title': {
                'text': 'Repositories',
                'font': {'size': 24}
            },
            'tickfont': {'size': 14},
        },

        'yaxis': {'title': {
            'text': 'Stars',
            'font': {'size': 24},
        },
            'tickfont': {'size': 14}, },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='repo_visual.html')

github_repos_stars(repo_dicts)
