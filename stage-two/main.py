"""Test the api endpoint"""
import requests

# This script runs the entire lifecycle of a data,
# at the end of running this script, there would be
# no stored data in the database
new_data = {'name': 'Omolade'}
updated_data = {'name': 'Toyin'}
post_response = requests.post('http://127.0.0.1:5000/api', data=new_data)
print(f'Post Request: {post_response.text}')
if post_response.status_code == 200:
    get_response = requests.get(f'http://127.0.0.1:5000/api/{post_response.text}')
    print(f'Get Request: {get_response.json()}')
    put_response = requests.put(f'http://127.0.0.1:5000/api/{post_response.text}', data=updated_data)
    print(f'Put Request: {put_response.text}')
    delete_response = requests.delete(f'http://127.0.0.1:5000/api/{post_response.text}')
    print(f'Delete Request: {delete_response.text}')
