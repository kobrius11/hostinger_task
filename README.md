# hostinger_task

### Set up 
1. Clone repository, 
3. set up virtualenv, or venv 
4. Download requirements
5. run python3 main.py in console

### Overview
Basically this program uses requests library to connect to an API, and either prints response, or writes it in a json file.
Also this program is capable initializing request object with a thread, so you can get multiple responses at the same time and still use the program for something else.

`main.py` contains whole program, menu loop.
`functions.py` contains all functions, which are called in main.
`logger.py` contains logger functions.

### Usage
API = `https://jsonplaceholder.typicode.com/`

First, specify destination (what data you want to get) eg.: i want all users, so `https://jsonplaceholder.typicode.com/users`,
or maybe all posts so `https://jsonplaceholder.typicode.com/posts`.
There are 6 destinations to chose from `users, posts, comments, albums, photos, todos`.

Once destination is choosen you can specify url parameters. 
eg.: i want to get all posts by user which has id = 1: `https://jsonplaceholder.typicode.com/posts?userId=1`,
i want to get all comments, on specific post(id=1), by specific user(id=1): `https://jsonplaceholder.typicode.com/comments?postId=1?userId=1`
Program tells its user which destination takes which url parameters.

Once destination & parameters are set, user can get data, by using 3 option in the main menu, where user will be promped to enter how he wants data to be delivered 1-option creates a json file in `./data` directory, 2- option prints data to the console.

Also user can turn on `Run threading` option, and once 1-options in `get data` menu is selected, new file will appear every 90 seconds.
`Run threading` is also supported in main menu `get all data` option, which creates directory `./all_data` and stores all data from all six destinations in there. 


### Examples
url = `https://jsonplaceholder.typicode.com/posts`
params = {userId=1, albumId=4, postId=2}
data will contain all posts where userId=1 `https://jsonplaceholder.typicode.com/posts?userId=1`
since its the only parameter this endpoint will accept.


url = `https://jsonplaceholder.typicode.com/comments/1`
params = {userId=3, albumId=4, postId=2}
data will contain comment with id=1, `https://jsonplaceholder.typicode.com/comments/1?postId=2`
since comment with id=1, and postId=2 doesn't exist.

url = `https://jsonplaceholder.typicode.com/comments`
params = {userId=3, albumId=4, postId=2}
data will contain all comments where postId=2, `https://jsonplaceholder.typicode.com/comments/?postId=2`



