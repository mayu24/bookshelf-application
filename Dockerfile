# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Initialize DB before start (or do in app.py)
RUN python -c "import sqlite3; sqlite3.connect('bookshelf.db').execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')"

# Run the app
CMD ["python", "app.py"]
