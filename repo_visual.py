import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers ={'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data =[{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
 'title' : 'Projekty python z największą liczbą gwiadek',
 'xaxis': {'title':'Repositories'},
 'yaxis': {'title':'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='repo_visual.html')