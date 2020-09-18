# Store_Python_Api

This is a simple example of Python Flask's usage as a simple "Task Manager".
The Database Management System is MongoDB. 
The python-MongoDB connector is PyMongo.

### Installation

First, you should [install MongoDB for DataBase](https://docs.mongodb.com/manual/installation/) and [Add JSON Viewer Chrome Extension for Best View of JSON Data on Browser](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)

then install all dependencies by running the following command:

```
$ sudo pip install -r requirements.txt
```

It will install Flask, Flask-WTF, and PyMongo.

### Usage

To run the program, first you should make sure MongoDB is running, start it using:

```
$ sudo service mongod start
```

then, run the program:

```
$ python app.py
```

Open your browser and go to `http://127.0.0.1:5000/Get_Movies` to see the running program.

