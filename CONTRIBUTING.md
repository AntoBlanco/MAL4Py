# Contributing to MAL4Py

First of all, thank you for considering contributing to MAL4Py! It's people like you who make the open-source community such an amazing place to learn, inspire, and create.

## 🔑 How to Obtain MyAnimeList (MAL) Credentials

To run the tests locally, you will need three pieces of information: MAL_CLIENT_ID, MAL_USER, and MAL_PASS.
1. Obtain the MAL_CLIENT_ID

    Go to MyAnimeList.net and log in.

    Navigate to the API settings: Edit Profile > API (or visit https://myanimelist.net/apiconfig).

    Click on Create ID.

    Fill out the form (you can use test data; the redirect URL can be http://localhost).

    Once created, you will see the Client ID. Copy it.

2. Configure the .env File

In the root of your project, create a file named .env and paste your credentials:
```text
MAL_CLIENT_ID=your_client_id_here
MAL_USER=your_mal_username
MAL_PASS=your_mal_password
```
 ⚠️ Important: Ensure that your MAL account does not have Two-Factor Authentication (2FA) enabled for tests using unstable_login, as this automated method typically does not support the second security factor.

## 🛠️ Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/AntoBlanco/MAL4Py.git
   ```

3. Create a **virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate     # Windows
   ```

4. Install dependencies in **editable mode**:
   ```bash
   pip install -e .
   ```



## 📏 Style Guidelines

To keep the codebase clean and consistent, please follow these rules:

### 1. Code Formatting

We use **Black** as our uncompromising code formatter. Before submitting a PR, please run:

```bash
black .

```

### 2. Type Hinting (Modern Python)

This project targets **Python 3.10+**. Please use **PEP 604** syntax for type hints:

* **Correct:** `dict[str, int] | None`
* **Avoid:** `Union[Dict[str, int], None]`

### 3. Documentation

If you add a new feature or change an existing one, please update the docstrings (Google style preferred) and the `README.md` if necessary.

## 🧪 Testing

We use `pytest` for automated testing. To ensure the quality of the library, all new features and bug fixes must pass existing tests and include new ones if necessary.

### 1. Setup Environment Variables
Since the library interacts with the MyAnimeList API, you need to provide credentials for testing. **Do not hardcode these in the test files.**

Create a `.env` file in the root of the project (this file is already ignored by git):
```text
MAL_CLIENT_ID=your_client_id_here
MAL_USER=your_mal_username
MAL_PASS=your_mal_password
```

### 2. Install Development Dependencies

Make sure you have the testing tools installed:

```bash
pip install -e ".[dev]"

```

### 3. Running Tests

You can run the entire suite or specific parts of it:

| Command | Description |
| --- | --- |
| `pytest` | Runs all tests in the `tests/` folder. |
| `pytest -v` | Detailed output (shows names of tests). |
| `pytest tests/test_media.py` | Runs only media-related tests. |
| `pytest -x` | Stops execution at the first failure. |

### 4. Continuous Integration (CI)

When you open a Pull Request, GitHub Actions will automatically run the tests using our internal secrets. Make sure your code passes locally before pushing!
## 📥 Submitting a Pull Request

1. Create a new branch for your feature or bugfix: `git checkout -b feature/my-cool-feature`.
2. Commit your changes with clear messages.
3. Push to your fork and **open a Pull Request** against the `main` branch.

---
*Note: This project is maintained by AntoBlanco. Please be patient with reviews!*

---