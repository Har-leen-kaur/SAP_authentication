import requests
import getpass

response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

# user variables
username = input('Enter the email you registered with: ') 
password =  getpass.getpass('Enter the password: ')
base_url = 'https://editor.signavio.com'  # target system url

#provide if user is member in multiple workspaces:
workspace_ID = 'f640921aa59b4e47820c1c5125990bc0' 