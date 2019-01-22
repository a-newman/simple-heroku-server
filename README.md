# A simple Python server for learning Heroku

## Organization 

- `index.html` contains the html page that will be displayed when you visit the app 
- `script.js` contains the JavaScript that will be loaded onto this html page
-  The directory `server` contains the files that will be used to serve this code
  - `server.py` runs the server
  - `save_data.py` contains helper functions for saving data 

## Instructions 

1. First, try out the server "locally": that means, from your own computer, to check that everything is working. 
  a. Run the server with the following command: `python3 server/server.py`. You should get an error telling you that some files are not downloaded! Make a virtual environment inside this folder and download the files you need using pip. Learn how to make a virtual environment here: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
  b. You should see output like: `Starting httpd on port 8000...`
  c. Go to the following url: `localhost:8000`
  d. Play around with the web page! Try submitting your name to the "database". Right now, the "database" is just a folder that stores files. If everything is working, after you submit your name, you should see a new file in the folder `server/data`. Open it and make sure that your name was stored! 
  e. In additional to showing the file `index.html`, Our website also keeps a simple counter of the number of people that visit the path `/counter`. Go to `localhost:8000/counter`. Refresh the page a few times and see what happens. 
2. Get a little familiar with the files `server.py` and `save_file.py` in the `server` file.
3. Let's get started with Heroku! Go online and make an account. You should NOT need a credit card for this. 
https://www.heroku.com/
4. Create a Heroku app! Check out these instructions. 
`https://devcenter.heroku.com/articles/git#creating-a-heroku-remote`
You should get an error when you try to run your app! You are still missing two
important files. 
First, something called a `Procfile` that tells Heroku how to run your app. 
https://devcenter.heroku.com/articles/procfile
Second, a `requirements.txt` file that tells Heroku what Python libraries you need to run your app. 
https://devcenter.heroku.com/articles/python-pip

Read the documentation and try to get your app working! I will be around to answer questions and help you along, so if you get stuck, let me know! 
