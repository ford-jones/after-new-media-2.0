# zero-views-youtube-crawler
Welcome to the usage guide for this python youtube crawler.
This project has a seacond half, find it here: https://github.com/ford-jones/zero-views-yt-frontend
Get started by using the command line to run the following scripts.

Make sure you have a python3 release installed with:
```
python3 --version
```

If you don't, install the latest version using homebrew: 
```
brew install python3
```

# Setup your python virtual environment

1. From your working directory, make a new folder and navigate into it:
```
mkdir pyEnv && cd pyEnv
```

2. From here you can install the venv package to manage the crawlers virtual environment, with python installed you should be able to run this from your CLI:
```
python3 -m venv env
```
Now when listing the current directory you will notice a new folder has been created called env.

3. The environment needs to be activated. Do this by setting the source of the env like so:
```
source env/bin/activate
```

4. To check if that worked, you can list the python files using pip:
```
pip list
```

5. Note that the environment can be deactivated again easily by running this from the root:
```
deactivate
```

# Setup the crawler

1. Now that your environment is setup. Make sure you are in the root of the pyEnv directory and clone the GH repository:
```
git clone https://github.com/0qy/zero-views-youtube-crawler.git
```

2. Navigate into the directory and install the dependencies using pip:
```
cd zero-views-youtube-crawler
pip install -r requirements.txt
```

3. Register an account with Youtube development and request an API key, be sure to take note of it: https://developers.google.com/youtube
The free API key will give you a cap of 50 searches every 24 hours, upgrade your account for more. 

4. You will also need to make an account with mongoDB Atlas: https://www.mongodb.com/cloud/atlas/register 
Create a new database with a single user (Note the username and password). In the configuration you will be prompted to authenticate requests privately or over a network. The choice is yours but be sure that any IP you want to have access to the database is included in your IP access list under the network access tab. 

When setting up your cluster make sure to take note of the name of your database and its' collection.

5. Set up a config.env file by running:
```
touch config.env
```

6. Open the newly created config.env file with your text editor and insert the following values:
```
API_KEY=yourYoutubeApiKey

MONGODB_USR=yourClusterUserName
MONGODB_PW=yourClusterUserPassword
MONGODB_DB='yourClusterDatabaseName'
MONGODB_COLLECTION='yourDatabaseCollectionName'
```

7. The crawler comes with a shell script which is used to execute the programme. Give execution permissions with:
```
chmod +x run.sh
```

8. With all the steps completed succesfully you should be able to run the script from the CLI with:
```
./run.sh
```
The crawler will output its' results in the terminal.
