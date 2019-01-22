# A simple Python server for learning Heroku

## Organization 

- `index.html` contains the html page that will be displayed when you visit the app 
- `script.js` contains the JavaScript that will be loaded onto this html page
-  The directory `server` contains the files that will be used to serve this code
  - `server.py` runs the server
  - `save_data.py` contains helper functions for saving data 

## Instructions 

1. First, try out the server "locally": that means, from your own computer, to check that everything is working. 
  - Run the server with the following command: `python3 server/server.py`. You should get an error telling you that some files are not downloaded! Make a virtual environment inside this folder and download the files you need using pip. Learn how to make a virtual environment here: https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
  - You should see output like: `Starting httpd on port 8000...`
  - Go to the following url: `localhost:8000`
  - Play around with the web page! Try submitting your name to the "database". Right now, the "database" is just a folder that stores files. If everything is working, after you submit your name, you should see a new file in the folder `server/data`. Open it and make sure that your name was stored! 
  - In additional to showing the file `index.html`, Our website also keeps a simple counter of the number of people that visit the path `/counter`. Go to `localhost:8000/counter`. Refresh the page a few times and see what happens. 
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
5. One more thing: in order for your server to run properly on Heroku, it needs to use the correct port. Heroku tells Python what port to use by setting an environment variable called `PORT`. Make the necessary changes in `server/server.py` so that it uses the correct port. You can test this locally by setting your own environment variable `PORT` on your local machine that is NOT 8000 and check if your server defaults to that port. 
6. Your app should be working! Congrats, you're live on the Internet! Celebrate your new web app by changing the file `index.html` so that your page says "Welcome to My Name's webpage!" instead of "Welcome to my webpage!". Commit your change and push the new version to Heroku. 
7. Let's set up a real MongoDB database in the cloud, instead of just using the filesystem. Make an account on [mLab](https://mlab.com/), which provides some amount of free storage in the cloud. Create a database with a collection called `data`. 
8. In order for your app to use your mLab database, you will have to change the variable `SAVE_METHOD` in `server/server.py`. You will also have to set an environment variable named `MONGO_URI` which you can use to access your database. See the function `save_mongo` in `server/save_data.py` to see how this is used. For more help setting up your database properly, see the [mLab documentation on connecting](https://docs.mlab.com/connecting/) and the [pymongo documentation](https://api.mongodb.com/python/current/). You will also need to [set an environment variable in Heroku](https://devcenter.heroku.com/articles/config-vars). (Note: why are we putting the url in an environment variable instead of writing it inside our Python file? If you're not sure, ask!)
9. Test your app on Heroku and make sure that when you submit a new piece of data, you can see it in your mLab database. 
10. You've now got a web app set up with a working database...albeit a very sim ple one! Do something cool with your web page! You might...
- Make it prettier: Change `index.html` to have more content or to make it prettier. You might want to take a look at the HTML/JavaScript library [Semantic UI](https://semantic-ui.com/), which is already contained in your code. 
- Make it more interactive: Change `script.js` to add more cool features to your web page. [JQuery](https://jquery.com/) is already included in your app. 
- Add a new page to your web app
- Add a new endpoint to your web app. An endpoint is a url that does not have a UI associated, but that you can use to communicate with your server. The urls `/counter` and `/data` are endpoints your app currently supports: the first increments and returns a counter, and the second stores data in your mLab database. 
- Do anything else you think might be cool! 

## Github crash course

Using Heroku will require you to use git to push code to Heroku's servers. Git is known as a version control system. It lets you keep track of different versions of a code base. [Github](https://github.com/) is the online version of git. It's kind of like Google Drive or Dropbox for code--it lets people share and collaborate on code bases. Git and Github are very commonly used when programming--it is good to learn how to use them! 

### 4 Github words you should know

- **Repository (repo)**: a code base that is managed by git. This is a repo! A "remote repo" is a repo or a version of a repo that is stored online (probably on Github), not on your computer. The remote version of this repo is located at https://github.com/a-newman/simple-heroku-server. 
- **Commit**: A version of your code. "Making a commit" or "committing" means saving a version of your code. 
- **Pushing (to push)**: Uploading some code or some new changes (commits) to a remote repo (probably on Github). Similarly, **pulling (to pull)** is when you download new changes from a remote repo. 
- **Branch**: Sometimes, repos can contain different versions of the same code base at the same time (for instance, if two people are working on different parts of the project at the same time). Different parallel versions of a project are known as branches. Publishing your code on Heroku requires pushing to a branch called `heroku`. The main branch of a project is called `master`. 

### 7 Github commands you should know

- `git status`: Gives you a summary of the current status of your repo. Files shown are ones that have been changed or added since your last commit. Files in green will be part of your next commit; files in red will not. (see `commit` and `add` below).
- `git diff`: shows you the changes that you have made since your last commit. 
- `git add .`: when run from the root directory of your repo, prepares to commit all files that you have changed since your last commit. After this, all files in `git status` should be green.
- `git commit -m "<message>"`: creates a new commit with message `<message>`.
- `git push origin master`: Pushes (uploads) your code to github.
- `git pull origin master`: Pulls (downloads) any changes from Github.
- `git log`: Shows you a list of your most recent commits (versions)

A common workflow for me is: 
`git status`: Check what files I've changed
`git diff`: Check what changes I've made
`git add .`: Prepare to commit my changes
`git commit -m "summary of my changes"`: Commit my change
`git status`: make sure that I have no unchanged files and that I committed everything
`git push origin master`: push my own changes
