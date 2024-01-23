Task Management System
This is a simple web application for managing tasks. The application allows users to create, update, delete, and view tasks.

Setup Instructions
Prerequisites
Python 3.x
Git

Clone the Repository
git clone https://github.com/your-username/task-management.git
cd task-management

Set Up Virtual Environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows, use .venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Apply Database Migrations
python manage.py migrate

Run the Application
python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser.

Usage
1. Access the task list: http://127.0.0.1:8000/tasks/
2. Create a new task: http://127.0.0.1:8000/tasks/create/
3. View task details: http://127.0.0.1:8000/tasks/{task_id}/
4. Update a task: http://127.0.0.1:8000/tasks/{task_id}/update/

Additional Notes
Make sure to deactivate the virtual environment after using the application:
deactivate

For production deployment, configure your web server (e.g., Nginx, Apache) and use a production-ready database.

