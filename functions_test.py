import functions as f


# get_json tests
##  should pass and return json
def test_get_json():
    assert f.get_json(url="https://jsonplaceholder.typicode.com/posts")

##  should fail
def test_get_json():
    assert f.get_json(url="https://jsonplaceholder.typicode.com/")

##  should fail
def test_get_json():
    assert f.get_json(url="https://test")

# time_sleep tests
##  should pass immediately
def test_time_sleep():
    assert f.time_sleep(seconds=-1) == None

##  should fail
def test_time_sleep():
    assert f.time_sleep(seconds='a') == None

##  should pass after 5 seconds
def test_time_sleep():
    assert f.time_sleep(seconds=5) == None

#   create_folder tests
##  should create a folder with name
def test_create_folder():
    assert f.create_folder(folder_name="folder_name")

##  should fail since folder with no name cant exist
def test_create_folder():
    assert f.create_folder(folder_name="")

##  should create a folder with 1 as name
### passes but does not create a folder, odd.
def test_create_folder():
    assert f.create_folder(folder_name=1)

### this one works, so folder names cannot be int, i wonder what else cannot be a folder name
def test_create_folder():
    assert f.create_folder(folder_name='1')

#   write_to_json tests
##  should create a folder data and store json file with data in it
def test_write_to_json():
    assert f.write_to_json(data_select="test", data=[{"test_data": 1}])

## should repeat 3 times 
# def test_write_to_json_repeated():
#     assert f.write_to_json_repeated(data_select="test", data={"test_data": 1}, wait_time=20, repeat=3) == None

#   get_all_data tests
##  Should create a folder named all_data, and store data from 6 endpoints to that folder
def test_get_all_data():
    assert f.get_all_data(threading=False)

##  Should reapeat 3 times    
# def test_get_all_data():
#     assert f.get_all_data(threading=True, wait_time=20, repeat=3)

##  Should reapeat forever
# def test_get_all_data():
#     assert f.get_all_data(threading=True, wait_time=20, repeat=-1)


