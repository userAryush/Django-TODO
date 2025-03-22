#First project using Django

This project uses the basics operation of django framework. It mainly focuses on CRUD(Create,Read,Update,Delete) operation.

# Django To-Do App

A simple To-Do application built using Django. This app allows users to view, create, edit, and delete tasks.

---

## Features  

-  Create new tasks with a name, task description, status, and deadline  
-  Edit existing tasks  
-  Delete individual tasks or all tasks at once  
-  Uses Django’s ORM for database management  
-  Clean and structured code with proper comments  

---

## 🛠️ Technologies Used  

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default Django database)  

---

## 📂 Project Structure
    📁 todo_app/
    ├── 📄 models.py # Database models
    ├── 📄 views.py # Logic and request handling
    ├── 📄 urls.py # URL routing
    ├── 📄 templates/ # HTML files 

->> Clone repository

```bash
git clone https://github.com/userAryush/Django-TODO.git
```

->> Create a Virtual environment using

```bash
python -m venv env
```

->> Activate Virtual environment using

-> For Windows

```bash
env\Scripts\activate
```

-> For Mac/Linux

```bash
source env\bin\activate
```

->> Install all requirements using

```bash
pip install -r requirements.txt
```

->> Initialize models using

```bash
python manage.py makemigrations
python manage.py migrate
```


->> Start Web App using

```bash
python manage.py runserver
```

Now, open http://127.0.0.1:8000/home/ in your browser to access the application. 🚀

![Image](https://github.com/user-attachments/assets/12399611-2407-4015-b78e-c02432d26782)
