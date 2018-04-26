import csv
import json
import requests

# Add github repos to the team

# todo replace with your stuff
repos_file = 'repos.csv'
token = 'Bearer TOKEN'
team_id = 'TEAM_ID'
owner = 'OWNER'

headers = {'Accept': 'application/vnd.github.hellcat-preview+json', 'Authorization': token}
payload = {'permission': 'admin'}
base_url = 'https://api.github.com/teams/{}/repos/{}/{}'

log_file = open('log.txt', 'w')


def write_to_log(s):
    s = str(s)
    print(s)
    log_file.write(s + '\n')


with open(repos_file, 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):

        if i == 0:  # skip csv header
            continue

        repo_name = row[0]
        action = row[3]
        move = action == 'move'

        if move:
            url = base_url.format(team_id, owner, repo_name)
            write_to_log('\nTransferring: {}'.format(repo_name))

            r = requests.put(url, headers=headers, data=json.dumps(payload))
            write_to_log(r.status_code)
            if 200 <= r.status_code < 300:
                write_to_log('Success')
            else:
                write_to_log('Error:')
                write_to_log(r.content.decode('utf-8'))

log_file.close()
