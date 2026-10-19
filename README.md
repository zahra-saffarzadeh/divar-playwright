# Divar Playwright Automation

End-to-End test automation for [Divar](https://divar.ir) using **Playwright** + **Pytest** with the **Page Object Model (POM)** pattern.

---

## Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## Project Structure

```text
Divar-Playwright/
├── pages/              # Page Objects
├── tests/              # Test cases
├── data/               # Test data
├── reports/            # HTML reports & screenshots
├── conftest.py         # Shared fixtures
├── pytest.ini
└── requirements.txt
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run a Single Test File

```bash
pytest tests/test_search.py
```

### Run Tests in Headed Mode

```bash
pytest --headed
```

### Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Main Fixtures

| Fixture | Description |
|---|---|
| `home_with_tehran` | Opens the site and selects Tehran |
| `category_page` | Prepares the category page |
| `mobile_category` | Navigates to the mobile phones category |

### Example

```python
def test_search(home_with_tehran):
    results = home_with_tehran.search("آیفون")
    assert results.get_result_count() > 0
```

---

## Test Coverage

### Home
- Open website
- Select city

### Search
- Search results
- No-result scenarios
- Sort results
- Clear search
- Search suggestions

### Category
- Categories
- Subcategories
- Browser back navigation

### Filters
- Price filter
- Has-photo filter
- Combined filters

### Ad Detail
- Title
- Price
- Description
- Contact
- Chat
- Bookmark

### Authentication
- Login modal
- Invalid phone number
- Guest authentication behavior

### Bookmarks
- Guest bookmark behavior

### Advanced
- Network scenarios
- Screenshots
- Responsive behavior

---

## Failure Reports

When a test fails, screenshots are saved under:

```text
reports/
```

To generate an HTML test report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Notes

- Keep UI logic inside `pages/` only.
- Avoid using `time.sleep()`; use Playwright's built-in `expect` and auto-waiting capabilities.
- Store test data in `data/test_data.py`.
- Full OTP login flow is not covered in this version.