## About
### How it works?
If you decide to run the API manually, you just need to go to the main directory and execute the main file using the command `python main.py` to run the main file.
If you decide to build the container and maybe deploy the API, you just need to go to the main directory an use the command `docker build -t container_name .` and the container will be ready to deploy.

### Why didn't i extract the data from the cache of the pivot table
The only way that i know that i can extract cache from pivot tables is if the file is in the `.xlsx` format, so i decided that it would be better to get the data directly from the ANP's website, rather than manually converting the file (since using python would ruin the cached data) so i can be up to date with the most recent files. I've also included a file named `cache_extractor.py` to demonstrate a simple pivot table cache data extraction from a `.xlsx` file.

### Where can i know more about the endpoints?
There is a file called `Docs_API.md` at the main directory where you can find all the endpoints and how to use then. 

### Observation
The API was tested using postman to send the requests.