import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
print(response_dict.keys())

print(f'Total repositories: {response_dict['total_count']}')
print(f'Complete results: {not response_dict['incomplete_results']}')

repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict['name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Repository: {repo_dict['html_url']}')
    print(f'Description: {repo_dict['description']}')

import plotly.express as px

repo_links, stars, hovertexts = [], [], []
for repo_dict in repo_dicts:

    repo_name = repo_dict['name']
    repo_url =repo_dict['html_url']
    repo_link = f"<a herf='{repo_url}'>{repo_name}</a>"   
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    hovertexts.append(repo_dict['description'])

fig = px.bar(x=repo_links, y=stars, labels={'x': 'Repository', 'y': 'Stars'}, title='Most-Starred Python Projects on GitHub', hover_name=hovertexts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()


