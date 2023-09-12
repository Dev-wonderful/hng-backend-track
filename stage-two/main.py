"""Test the api endpoint"""
import requests

new_data = {'name': 'Samuel'}
updated_data = {'name': 'Bola'}
post_response = requests.post('http://localhost:5000/api', data=new_data)
print(f'Post Request: {post_response.status_code}')
get_response = requests.get('http://localhost:5000/api?name=Samuel')
print(f'Get Request: {get_response.status_code}')
patch_response = requests.patch('http://localhost:5000/api', data=updated_data)
print(f'Patch Request: {patch_response.status_code}')
