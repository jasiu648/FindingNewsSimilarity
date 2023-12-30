import psycopg2
from psycopg2 import sql

class DataProvider():
    
    def __init__(self):
        db_params = {
            "database": "nlpdatabase",
            "user": "postgres",
            "password": "6487",
            "host": "localhost",
            "port": "5432",
        }

        conn = psycopg2.connect(**db_params)

        self.cursor = conn.cursor()

    def get_articles(self, language = 'PL', max_count = 100):
        
        query = sql.SQL("""
            SELECT
                tr.body,
                ta.body,
                ml.similarity
            FROM
                matching_list ml
            JOIN releases re ON ml.id_releases = re.id 
            JOIN articles ar ON ml.id_articles = ar.id
            JOIN texts ta ON ta.id = ar.id_texts
            JOIN texts tr ON tr.id = re.id_texts
            WHERE ar.language = {}
            LIMIT 101
        """).format(sql.Literal(language))

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows

class DataInput():
    def __init__(self):

        db_params = {
            "database": "nlp_english",
            "user": "postgres",
            "password": "6487",
            "host": "localhost",
            "port": "5432",
        }

        conn = psycopg2.connect(**db_params)

        self.cursor = conn.cursor()

    def add_article(self, body = "", category = ""):

        query = "INSERT INTO articles (body, category) VALUES (%s, %s)"
        self.cursor.execute(query, (body, category))

    def add_copy(self, body = "", original_id =""):

        query = "INSERT INTO copies (main_id, body) VALUES (%s, %s)"
        self.cursor.execute(query, (original_id, body))
