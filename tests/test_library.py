import os
import sys
import json
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import Book
from storage import Storage


@pytest.fixture
def sample_books():
    return [
        {"id": "1", "title": "Title 1", "author": "Author 1", "year": "2001", "status": "в наличии"},
        {"id": "2", "title": "Title 2", "author": "Author 2", "year": "2002", "status": "выдана"}
    ]

@pytest.fixture
def storage(tmpdir):
    file_path = tmpdir.join("library.json")
    return Storage(str(file_path))

def test_load_books(storage, sample_books):
    with open(storage.filename, "w") as file:
        json.dump(sample_books, file)
    
    books = storage.load_books()
    
    assert len(books) == len(sample_books)
    for book, sample in zip(books, sample_books):
        assert book.id == sample["id"]
        assert book.title == sample["title"]
        assert book.author == sample["author"]
        assert book.year == sample["year"]
        assert book.status == sample["status"]

def test_save_books(storage, sample_books):
    books = [Book(**data) for data in sample_books]
    
    storage.save_books(books)
    
    with open(storage.filename, "r") as file:
        saved_books = json.load(file)
    
    assert len(saved_books) == len(sample_books)
    for saved, sample in zip(saved_books, sample_books):
        assert saved["id"] == sample["id"]
        assert saved["title"] == sample["title"]
        assert saved["author"] == sample["author"]
        assert saved["year"] == sample["year"]
        assert saved["status"] == sample["status"]

def test_load_books_file_not_found(storage):
    if os.path.exists(storage.filename):
        os.remove(storage.filename)
    
    books = storage.load_books()
    assert books == []

def test_save_books_creates_file(storage, sample_books):
    if os.path.exists(storage.filename):
        os.remove(storage.filename)
    
    books = [Book(**data) for data in sample_books]
    
    storage.save_books(books)
    
    assert os.path.exists(storage.filename)

    with open(storage.filename, "r") as file:
        saved_books = json.load(file)
    
    assert len(saved_books) == len(sample_books)
    for saved, sample in zip(saved_books, sample_books):
        assert saved["id"] == sample["id"]
        assert saved["title"] == sample["title"]
        assert saved["author"] == sample["author"]
        assert saved["year"] == sample["year"]
        assert saved["status"] == sample["status"]
