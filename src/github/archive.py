import json
import requests

# Archive github repos marked with a specific topic

# TODO owner organisation
owner = 'OWNER'

# TODO replace target topic to archive if necessary
archive_topic = 'archive'

# TODO put your API token here
token = 'Bearer TOKEN'

headers = {'Accept': 'application/vnd.github.mercy-preview+json', 'Authorization': token}
repos_url = 'https://api.github.com/orgs/{}/repos?page={}'
archive_url = 'https://api.github.com/repos/{}/{}'

log_file = 'log.txt'
log = open(log_file, 'w')


def write_to_log(s):
    s = str(s)
    print(s)
    log.write(s + '\n')


page = 0
repos_to_archive = []

write_to_log('Searching repos marked with topic: {}'.format(archive_topic))

while True:
    write_to_log('Page {}'.format(page))
    repo_data = requests.get(repos_url.format(owner, page), headers=headers).json()
    page += 1

    if not repo_data:
        break

    for repo in repo_data:
        if 'topics' in repo:
            topics = repo['topics']
            if archive_topic in topics:
                repos_to_archive.append(repo['name'])

write_to_log('\nFound repos to archive:')
for repo in repos_to_archive:
    write_to_log(repo)

write_to_log('\nArchiving repos:')

for repo in repos_to_archive:
    write_to_log(repo)
    payload = {'name': repo, 'archived': True}
    r = requests.patch(archive_url.format(owner, repo), headers=headers, data=json.dumps(payload))
    write_to_log(r.status_code)
    if 200 <= r.status_code < 300:
        write_to_log('Success')
    else:
        write_to_log('Error:')
        write_to_log(r.content.decode('utf-8'))

log.close()
