# hyperionBlog

Project Name: Django Blog App

Description:
The Django Blog App is a web application built using Django and Python. It provides users with a platform to create, publish, and manage blog posts easily. With features such as user authentication, rich text editor for writing posts, and commenting system, the app offers a seamless experience for both bloggers and readers.

Table of Contents:
Installation
Usage
Credits

Installation:
To set up the Django Blog App on your local machine, follow these steps:

Clone the repository:

bash
git clone https://github.com/bruh2114/hyperionBlog.git
Navigate to the project directory:

bash
cd django-blog-app

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
bash
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Perform database migrations:
python manage.py migrate

Create a superuser (admin account):
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the blog app in your web browser at http://localhost:8000/blog.

Usage:
Creating a Blog Post:
Log in to the admin dashboard using the credentials of the superuser created during installation.
Navigate to the "Posts" section and click on "Add Post."
Fill in the title, content, and any other relevant information.
Click on "Save" to publish the post.

Viewing and Commenting on Posts:
Users can view published blog posts on the home page.
To comment on a post, users can click on the post title to view the full post and comment using the comment form provided.

Managing Users and Content:
Administrators can manage users, posts, and comments through the Django admin interface.
They can edit or delete existing posts, approve or delete comments, and manage user accounts.

Credits:
This project was developed by Aobakwe Sithole and is licensed under the HyperionDev license. Special thanks to the Django community for their contributions and support. If you have any questions or suggestions, please feel free to contact me at bakkies2116@gmail.com.
