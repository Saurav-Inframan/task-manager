# Task Manager

A simple task manager web app built with Flask and SQLite.

## Features

- Add a task
- View all tasks
- Mark a task as completed (or undo)
- Delete a task
- Clean HTML/CSS frontend

## Tech Stack

- Python 3
- Flask
- SQLite
- HTML/CSS

## Project Structure

```text
task-manager/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Setup & Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/task-manager.git
   cd task-manager
   ```

2. **Create and activate a virtual environment**

   Windows (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser at **http://127.0.0.1:5000**

The SQLite database (`tasks.db`) is created automatically the first time the app runs.

## Pushing to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/task-manager.git
git branch -M main
git push -u origin main
```

## License

Free to use for learning and personal projects.
