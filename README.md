

# Blog Website

This is a blog website built using Python, Django, and SQL.
![Android Chrome Icon](static/android-chrome-192x192.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction

This project is a dynamic and user-friendly blog website developed using the Django web framework. It empowers users to not only share their thoughts through blog posts but also engage with a community of like-minded individuals. In addition to standard features like creating, editing, and deleting posts, users can interact through comments, fostering a sense of collaboration and discussion.

The website prioritizes user experience with its intuitive interface and responsive design, ensuring seamless navigation on both mobile and desktop devices. Robust authentication and authorization mechanisms guarantee secure access, while a powerful search functionality enables users to quickly locate specific posts of interest.

Through this platform, we aim to provide a space where individuals can express themselves, exchange ideas, and contribute to a thriving community. Whether you're a seasoned blogger or just starting out, we welcome you to join us in this exciting journey of sharing and learning.

## Features

- User authentication and authorization (login, logout, registration, password reset)
- Create, edit, and delete blog posts
- View and comment on blog posts
- Search functionality to find specific posts
- Responsive design for mobile and desktop devices
- Admin panel for managing users, posts, and comments

## Requirements

- Python 3.x
- Django 3.x
- SQL database (e.g., SQLite, PostgreSQL)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rithikseth123/Blog-Website.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Blog-Website
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the website.

## Usage

- Visit the website and create an account or log in if you already have one.
- Create, edit, or delete blog posts from your dashboard.
- View and comment on existing blog posts.
- Use the search functionality to find specific posts.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request on the original repository.


