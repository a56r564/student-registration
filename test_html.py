from pathlib import Path
from bs4 import BeautifulSoup


def test_html_file_exists():
    assert Path("index.html").exists(), "index.html does not exist"


def test_required_elements():
    html_file = Path("index.html")

    html = html_file.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")

    assert soup.find("html") is not None
    assert soup.find("head") is not None
    assert soup.find("body") is not None

    heading = soup.find("h1")

    assert heading is not None
    assert "Student Registration" in heading.text

    form = soup.find("form")

    assert form is not None

    assert soup.find("input", {"id": "name"}) is not None
    assert soup.find("input", {"id": "email"}) is not None
    assert soup.find("input", {"id": "roll"}) is not None

    assert soup.find("select", {"id": "course"}) is not None

    button = soup.find("button", {"type": "submit"})

    assert button is not None