import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("searchengine_front/searchengine_front/chat-3d13c-firebase-adminsdk-o5qln-85aeee7308.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def store_page(url, content):
    try:
        db.collection('pages').add({'url': url, 'content': content})
    except Exception as e:
        print(f"Error adding page: {e}")

def get_all_pages():
    try:
        return [doc.to_dict() for doc in db.collection('pages').stream()]
    except Exception as e:
        print(f"Error fetching pages: {e}")
        return []

def search_pages_by_content(search_term):
    try:
        return [
            doc.to_dict() for doc in db.collection('pages').stream()
            if search_term.lower() in doc.to_dict().get('content', '').lower()
        ]
    except Exception as e:
        print(f"Error searching pages: {e}")
        return []
