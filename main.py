import json


f = open('token.json', 'r')
print json.loads(f.readline())
