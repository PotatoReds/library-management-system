# Library Management System
## Description

A Python-based library management system built using object-oriented programming (OOP).
The system allows users to manage books and members, issue and return books, and store data persistently using JSON.

## Features
Add, remove, and update books
Add, remove, and update members
Issue and return books
Search books and members
Track member borrowing history
Persistent storage using JSON files
Command-line interface (CLI)
Unit testing using unittest
Technologies Used
Python 3
Object-Oriented Programming (OOP)
JSON (for data storage)
unittest (for testing)
How to Run

## Run the program:

python3 main.py

## Run tests:

python3 -m unittest tests/test_library.py
Project Structure
library-management-system/
│
├── src/
│   ├── book.py
│   ├── member.py
│   └── library.py
│
├── tests/
│   └── test_library.py
│
├── main.py
├── playground.py
├── books.json
├── members.json
└── README.md

## OOP Concepts Used
Classes and Objects
Encapsulation
Polymorphism (display_info methods)
Modular design

## Notes
Data is saved in books.json and members.json
The system loads saved data automatically on startup

## Author

Jonathan S. Jacobsen