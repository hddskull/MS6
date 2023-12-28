import unittest
import requests

# from document_service.app.model.document import Document

KRAKEND_URL = "http://127.0.0.1:8080"
test_user = {
    "id": "e1161271-c9d1-47b3-95d1-d879bd137a2a",
    "first_name": "Test",
    "last_name": "Test",
    "gender": "male",
    "roles": ["admin"]
}
test_doc = {
    'title': 'This is a e2e test entity',
    'body': 'This is a e2e test entity',
    'owner_id': 'e1161271-c9d1-47b3-95d1-d879bd137a2a'
}

test_doc_id = ''


def get_test_doc_id():
    r = requests.get(f"{KRAKEND_URL}/v1/user_docs")
    docs = r.json()['documents']
    for doc in docs:
        if (
                doc['title'] == 'This is a e2e test entity' and
                doc['body'] == 'This is a e2e test entity' and
                doc['owner_id'] == 'e1161271-c9d1-47b3-95d1-d879bd137a2a'
        ):
            return doc['id']
    return ''

class TestE2E(unittest.TestCase):
    # CMD: python tests/e2e.py

    def test_users_handle(self):
        r = requests.get(f"{KRAKEND_URL}/v1/users")
        self.assertEqual(r.status_code, 200)

    def test_add_doc_handle(self):
        r = requests.post(f"{KRAKEND_URL}/v1/add_doc", json=test_doc)
        self.assertEqual(r.status_code, 200)

    def test_user_docs_handle(self):
        test_dict = test_doc.copy()
        test_dict['id'] = get_test_doc_id()

        r = requests.get(f"{KRAKEND_URL}/v1/user_docs")

        doc_list = r.json()['documents']

        self.assertEqual(test_dict in doc_list, True)

    def test_user_data_by_id_handle(self):
        user_id = test_user['id']
        r = requests.get(f"{KRAKEND_URL}/v1/user_data/{user_id}")

        test_dict = test_doc.copy()
        test_dict['id'] = get_test_doc_id()

        ER = {
            'document': test_dict,
            'user': test_user
        }
        AR = r.json()
        self.assertEqual(AR, ER)

if __name__ == '__main__':
    unittest.main()
