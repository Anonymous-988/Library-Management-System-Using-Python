# Library Management System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [End](#end)

## Introduction

The Library Management System is a Python-based application that allows users to manage and organize a catalogue of books and journals. Users can log in, borrow and return books, search for books.

## Features

- User authentication and login system
- Book borrowing and return functionality
- Search and filtering of books
- User-friendly command-line interface

## Technologies Used

- Python 3.9.12
- MySQL Database
- XAMPP Server

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/Anonymous-988/Library-Management-System-Using-Python.git
   ```

2. Navigate to the project directory:
   ```
   cd Library-Management-System-Using-Python
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MySQL database:
   - Create a new MySQL database named `library`.
   - Import the provided SQL dump file from Assets using the following command:
     ```
     mysql -u username -p library < library.sql
     ```

5. Update the database connection settings in `DBModule.py`:
   ```python
   DB_HOST = 'localhost'
   DB_USER = 'your_db_username'
   DB_PASSWORD = 'your_db_password'
   DB_NAME = 'library'
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Follow the on-screen instructions to log in, borrow or return books/journals.

## Database Schema

The database schema consists of the following tables:

- `users`: Stores user information (uid pkey auto, username, password, fname, lname).
- `items`: Stores books/journals information (itemid pkey auto, title, author, genre, itemtype, quantity, pyear).
- `user_action`: Keeps track of borrowed/returned items (aid pkey auto, uid fkey, itemid fkey, action, review, rating).

Users and Items has a many-to-many relationship which is established using user_action relation. Users can either borrow or return items which will be logged in the user_action table and action column.

## End
Open for Suggestions.. Thank You !!
