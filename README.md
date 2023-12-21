# Overview
This is a simple blog post app with basic functions:
- Authentication

![logIn](https://github.com/NhiCao/finance-blog-django/assets/27496909/21cbc48b-e613-41cc-92f1-a892e05d5a89)

- Display a list of posts

![home](https://github.com/NhiCao/finance-blog-django/assets/27496909/0093182b-36f5-476a-b6ae-1b6b367a2737)

- Display details of a post

![postDetail](https://github.com/NhiCao/finance-blog-django/assets/27496909/801d33f1-b826-4632-9e6c-15750a3f61b3)

- Create a new post

![postCreate](https://github.com/NhiCao/finance-blog-django/assets/27496909/e2ad0130-4052-483d-b5b2-b7869079dffb)

- Edit a post

![postEdit](https://github.com/NhiCao/finance-blog-django/assets/27496909/efac23a2-8deb-435c-8f79-df6ae0e586e5)

- Delete a post

![postDelete](https://github.com/NhiCao/finance-blog-django/assets/27496909/27770abf-f224-4318-b58f-2ab0869b1174)

# Setting the system up:
- Clone the repository to your local machine
```
git clone https://github.com/NhiCao/finance-blog-django.git
```
- Move to the project directory
```
cd finance-blog-django
```
- Create a virtual environment
```
virtualenv venv
```
- Activate the virtual environment
```
venv\Scripts\activate
```
- Install Django in the virtual environment
```
pip install Django
```
- Migrate data
```
python manage.py migrate
```
- Create a user
```
python manage.py createsuperuser
```
- Start the server
```
python manage.py runserver
```
- Open your browser and go to http://localhost:8000/home/. Log in using the user you created above and start by creating a new post.
