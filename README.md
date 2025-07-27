# 🔗 Shortener

**Shortener** is a simple web service for shortening long URLs. Built with Django and optionally runnable via Docker.

## 🚀 Getting Started (Local)

### 1. Install [`uv`](https://github.com/astral-sh/uv)

### 2. Sync dependencies

```
uv sync
```

### 3. Environment Configuration
Create a .env file in the src/ directory (based on .env.dist):

### 4. Run the server locally

```
py .\src\manage.py runserver 8100
```

### Running with Docker

### 1. Build and start the container

```
docker-compose up -d --build
```

### 2. Open the application
Visit: http://localhost:8100

## ✅ Usage
1. Open the app in your browser.
2. Paste any valid URL into the form.
3. Get a shortened link like: ```http://localhost:8100/abc123```
4. Use it to redirect to the original URL.

🧪 Running Tests (optional)
You can add a section here if your project includes tests using pytest, unittest, etc.