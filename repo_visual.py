from plotly import offline


def prepare_repos_stars_data(repositories):
    repo_links = []
    stars = []
    labels = []

    for repo in repositories:
        # Klikalne etykiety dla repozytoriów
        repo_name = repo['name']
        repo_url = repo['html_url']

        repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
        stars.append(repo['stargazers_count'])

        # Podpowiedzi
        owner = repo['owner']['login']
        description = repo['description'] or 'Brak opisu'
        labels.append(f"{owner}<br />{description}")

    return repo_links, stars, labels


def create_bar_chart(repo_links, stars, labels):
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
    return {'data': data, 'layout': my_layout}


def save_chart(fig,filename):
    offline.plot(fig, filename=filename)



