import json
import re
from slacker import Slacker

f = open('token.json', 'r')
config = json.loads(f.read())
token = config['token']
channels = config['channels']
f.close()

ts = open('timestamp.dat', 'r')
oldest_ = ts.readline()
ts.close()

slack = Slacker(token)

latest = oldest_
for channel_ in channels:
    response = slack.channels.history(channel_, oldest=oldest_, inclusive=0)
    messages = response.body['messages']
    for message in messages:
        if message['ts'] > latest:
            latest = message['ts']
        if re.search(r'(marki)|(plier)', message['text'], re.I):
            slack.reactions.add('cold_sweat', channel=channel_, timestamp=message['ts'])

ts = open('timestamp.dat', 'w')
ts.write(latest)
ts.close()
