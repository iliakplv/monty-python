import csv
import json
import requests

# Transfer github repos to new owner

# todo replace with your stuff
token = 'Bearer TOKEN'
old_owner = 'OLD_OWNER'
new_owner = 'NEW_OWNER'

headers = {'Accept': 'application/vnd.github.nightshade-preview+json', 'Authorization': token}
payload = {'new_owner': new_owner, 'team_id': []}
base_url = 'https://api.github.com/repos/{}/{}/transfer'

log_file = open('log.txt', 'w')


def write_to_log(s):
    s = str(s)
    print(s)
    log_file.write(s + '\n')


with open('repos.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):

        if i == 0:  # skip csv header
            continue

        repo_name = row[0]
        action = row[3]
        move = action == 'move'

        if move:
            url = base_url.format(old_owner, repo_name)
            write_to_log('\nTransferring: {}'.format(repo_name))

            r = requests.post(url, headers=headers, data=json.dumps(payload))
            write_to_log(r.status_code)
            if 200 <= r.status_code < 300:
                write_to_log('Success')
            else:
                write_to_log('Error:')
                write_to_log(r.content.decode('utf-8'))

log_file.close()
