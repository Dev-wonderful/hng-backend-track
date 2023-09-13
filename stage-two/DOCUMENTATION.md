## FORMATS
In this documentation, I am making use of python requests module for examples
#### POST
The POST request needs a name to be passed in the request body, the value returned is the `user_id` to be used in subsequent HTTP methods, concerning this user
```
.
.
>>> post_response = requests.get(f'{BASE_URL}/api', data={'name':'Hello World' })
>>> post_response
>>> 65774884994994040484848
```