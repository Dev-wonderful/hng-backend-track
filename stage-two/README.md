## SETUP
This python project was built to enable CRUD operations on a user object which only has a name attribute.
To work with this project, you need to clone this repository.

This guide is assuming that you are using the following.

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
If it fails, check your mongodb server

## Available Endpoints

```
POST    /api            => user_id (string)
GET     /api/user_id    => user dict (JSON)
PUT     /api/user_id    => success (string)
DELETE  /api/user_id    => success (string)
```

### UML Diagram

[This is a link to the UML diagram showing the structure and relationship between the api routes and the user model](https://drive.google.com/file/d/1L3-1EnbEksxkn54Ho2EapbH8adMchpld/view?usp=sharing)
