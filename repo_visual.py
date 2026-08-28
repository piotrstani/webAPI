import requests
from plotly import offline

# Pobierz dane z GitHuba
def get_github_repos():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    response = requests.get(url, headers=headers, timeout=10)
    print(f"Kod stanu: {response.status_code}")
    response.raise_for_status()

    return response.json()['items']

# Przetwórz dane i zwizualizuj dane
def github_repos_stars(repositories):
    repo_links, stars, labels = [], [], []
    for repo_dict in repositories:
        # Klikalne etykiety dla repozytoriów
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        # Podpowiedzi
        owner = repo_dict['owner']['login']
        description = repo_dict['description'] or 'Brak opisu'
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
            'text': 'Projekty Python z największą liczbą gwiazdek',
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

repos = get_github_repos()
github_repos_stars(repos)
