import os

# API params
PATH_LAST_PROCESSED = "./data/last_processed.json"
API_KEY = "8baf43d621934e4298eb9132ff8f4cd5"
#API_KEY = os.getenv("NEWS_API")
MAX_LIMIT = 100
MAX_OFFSET = 10000

# We have three parameters in the URL:
# 1. MAX_LIMIT: the maximum number of records to be returned by the API
# 2. date_de_publication: the date from which we want to get the data
# 3. offset: the index of the first result
URL_API = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
URL_API = URL_API.format(API_KEY)
#URL_API = URL_API.format(MAX_LIMIT, "{}", "{}")

# POSTGRES PARAMS
user_name = os.getenv("POSTGRES_DOCKER_USER", "localhost")
POSTGRES_URL = f"jdbc:postgresql://{user_name}:5432/postgres"
POSTGRES_PROPERTIES = {
    "user": "postgres",
    "password": os.getenv("POSTGRES_PASSWORD"),
    "driver": "org.postgresql.Driver",
}

NEW_COLUMNS = [
    
]

COLUMNS_TO_NORMALIZE = [
   
]

COLUMNS_TO_KEEP = [
    "publishedAt",
    "source",
    "author",
    "title",
    "description",
    "url",
    "urlToImage",
    "content"
]

DB_FIELDS = COLUMNS_TO_KEEP + COLUMNS_TO_NORMALIZE + NEW_COLUMNS