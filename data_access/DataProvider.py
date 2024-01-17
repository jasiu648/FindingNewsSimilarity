import psycopg2
from psycopg2 import sql
import requests
from bs4 import BeautifulSoup
import PyPDF2

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
            LIMIT 100
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

class DataFromUrl():

    @staticmethod
    def get_article_text(url):
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract article text
            article_text = ""
            # Customize the CSS selectors based on the structure of the website
            paragraphs = soup.find_all('p')  # Adjust this based on the HTML structure of the article
            for paragraph in paragraphs:
                article_text += paragraph.get_text() + '\n'
            
            return article_text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None

class DataFromPdf:
    def __init__(self):
        pass

    @staticmethod
    def get_article_text(pdf_path):
        """
        Extracts text content from a PDF file.

        :param pdf_path: The path to the PDF file.
        :return: The text content of the PDF.
        """
        text_content = ""
        
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Iterate through each page and extract text
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_content += page.extract_text()

        except Exception as e:
            print(f"Error: {e}")

        return text_content

