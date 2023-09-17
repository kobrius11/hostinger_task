# hostinger_task

### Set up 
Program was written in WSL2 Ubuntu 22.04.2 LTS, Python 3.10.6
1. Clone repository, 
3. set up virtualenv, or venv  `python3 -m venv venv`
4. Download requirements `pip install -r requirements.txt`
5. run `python3 main.py` in console

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
i want to get comment with id=1, by specific user(id=1): `https://jsonplaceholder.typicode.com/comments/1/?userId=1`
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

### What i would have done with more time.
`Refactoring`: To improve code quality and maintainability, you could have continued refactoring the code. Focus on breaking down complex functions into smaller, more manageable ones, and adhere to coding standards and best practices.

`Testing`: Expanding test coverage is essential for ensuring the reliability and robustness of your program. You might have written more unit tests, integration tests, and possibly even added automated testing frameworks to catch bugs early in the development process.

`Web-Based Version`: If you were considering adapting the program into a web-based version using Django-REST, you could start by outlining the project requirements, designing the database schema, and creating API endpoints to interact with the application. This would involve setting up Django models, serializers, views, and URL routing.

`Abstraction`: To make the program more abstract, you could identify common patterns and functionality and encapsulate them into reusable modules or classes. This would make the code more flexible and easier to maintain in the long run.

