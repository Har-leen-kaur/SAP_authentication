import requests
from conf import *
from authentication.authenticate import authenticate

# user variables
# ID of the diagram revision you want to retrieve the revision list for
diagram_ID = '96d76985bd6e4d9c9f4d3096c2afd3ce'

revision_url = base_url + '/p/model/' + diagram_ID + '/revisions'
auth_data = authenticate()

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json',
           'x-signavio-id':  auth_data['auth_token']}

get_revisions_request = requests.get(revision_url,
                                     cookies=cookies,
                                     headers=headers)

print(get_revisions_request.text)

with open('diag.json', 'w') as f:
    f.write(get_revisions_request.text)
    f.close()