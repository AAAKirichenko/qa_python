import pytest
from main import BooksCollector  # Импортируй класс


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector