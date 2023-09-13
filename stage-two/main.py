"""Test the api endpoint"""
import requests

# This script runs the entire lifecycle of a data,
# at the end of running this script, there would be
# no stored data in the database
new_data = {'name': 'Hello World'}
updated_data = {'name': 'HNG Track'}
deployed_url = 'https://stage-one-9fjg.onrender.com'
local_url = 'http://127.0.0.1:5000'
post_response = requests.post(f'{deployed_url}/api', data=new_data)
print(f'Post Request: {post_response.text}')
print(f'Post Request: {post_response.status_code}')
if post_response.status_code == 200:
    get_response = requests.get(f'{deployed_url}/api/{post_response.text}')
    print(f'Get Request: {get_response.json()}')
    put_response = requests.put(f'{deployed_url}/api/{post_response.text}', data=updated_data)
    print(f'Put Request: {put_response.text}')
    delete_response = requests.delete(f'{deployed_url}/api/{post_response.text}')
    print(f'Delete Request: {delete_response.text}')
