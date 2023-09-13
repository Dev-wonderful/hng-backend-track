## FORMATS
In this documentation, I would be making use of python requests module for examples
#### POST
The POST request needs a name to be passed in the request body as a form-data, the value returned is the `user_id` to be used in subsequent HTTP methods, concerning this user
```
.
.
>>> post_response = requests.post(f'{BASE_URL}/api', data={'name':'Hello World' })
>>> post_response
>>> 6501c7feff424ec0e3c23bac
```
#### GET
The GET request needs the `user_id` of an existing user, to be passed as a path parameter. The response is JSON data of the user details requested for
```
.
.
>>> get_response = requests.get(f'{BASE_URL}/api/6501c7feff424ec0e3c23bac')
>>> get_response.json()
>>> {'id': '6501c7feff424ec0e3c23bac', 'name': 'Hello World'}
```
#### PUT
The PUT request needs a name to be passed in the request body as a form-data, and the `user_id` of the user to be updated as a path parameter.
The response is a string `success` indicating that the update was successful.
```
.
.
>>> put_response = requests.put(f'{BASE_URL}/api/6501c7feff424ec0e3c23bac', data={'name':'Stage Two' })
>>> put_response
>>> success
```
#### DELETE
The DELETE request needs the `user_id` of an existing user, to be passed as a path parameter.
The response is a string `success` indicating that the deletion was successful.
```
.
.
>>> delete_response = requests.delete(f'{BASE_URL}/api/6501c7feff424ec0e3c23bac')
>>> delete_response
>>> success
```

## Assumptions
* The POST and PUT request data would be sent as a form-data
* A PATCH request won't be needed since it's only one attribute under user

## Setting up a Development Environment

This guide is assuming you are using the following.

`Requirements`
```
Windows 10
python 3.10.1
mongodb community server (To setup a local db)
mongosh or mongodb compass (To view your db locally)

Optional
mongodb atlas cluster (For deployment)
```

If your environment meets the above requirement, you can proceed.

```
git clone https://github.com/Dev-wonderful/hng-backend-track.git
```
`cd` into the directory and install dependencies with `pip`

```
cd hng-backend-track/stage-two
pip install -r requirements.txt 
```
When Installation is done, start your mongodb server if it isn't active and run this command to start the flask server

```
python -m app
```

Open a second terminal, run the `main.py` to test that all is working fine

```
python main.py
```

## Deploying on a remote server
The process would vary based on the hosting platform but the general requirements are the build and start command.

`Sidenote:` Make sure the hosting platform is running python version 3.10.1 above to be safe

`Build Command`
```
pip install -r requirements.txt
```

`Start Command`

The start command would be to start a production level application server like gunicorn, the flask default server can only be used for development
```
gunicorn app:app
```

Set your appropriate environment variables like your mongodb connection uri in your hosting platform

