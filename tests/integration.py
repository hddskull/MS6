import unittest
import requests
import psycopg2
from time import sleep


def checkConnect():
    try:
        conn = psycopg2.connect(
            dbname='DocumentsDB',
            user='postgres',
            password='biba',
            host='localhost',
            port='5432'
        )
        conn.close()
        return True
    except:
        return False


class TestIntegration(unittest.TestCase):
    # CMD: python tests/integration.py

    def test_db_connection(self):
        sleep(5)
        self.assertEqual(checkConnect(), True)

    def test_document_service_connection(self):
        r = requests.get("http://127.0.0.1:8001/health")
        self.assertEqual(r.status_code, 200)

    def test_user_service_connection(self):
        r = requests.get("http://127.0.0.1:8000/health")
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()