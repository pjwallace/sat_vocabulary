# SAT Vocabulary Practice App

A lightweight desktop application built with Python and Tkinter for SAT vocabulary practice.  
This app functions as a simple flashcard-style tool: it displays a vocabulary word, allows the user to think through the definition, and then reveals the correct meaning on demand.

The project is intentionally minimal, stable, and easy to run. It is designed for focused vocabulary review without grading, scoring, or distractions.

The words used in this app come from the Princeton Review Top 100 SAT Words.

---

## Author
Created by Patrick Wallace, MD FACS
Educator & developer of educational tools for test preparation and medical training.

---

## Features

- Randomized vocabulary words (no immediate repeats)
- Clean, distraction-free user interface
- Reveal definition on submission (no grading)
- Tracks progress through the word list
- Automatically resets when all words have been shown
- Desktop-based (no internet connection required)

---

## Project Structure

sat-vocab-app/
│
├── sat_vocabulary.py # Main application file
├── SAT100.txt # Vocabulary source file (word + definition)
├── README.md # Project documentation
├── .gitignore # Git ignore rules
└── requirements.txt # (Optional) dependencies

## Vocabulary File Format

The vocabulary file should be a plain text file with **one word per line**, formatted as:
abate to become less intense or widespread
aberration a departure from what is normal

- The **first token** is treated as the word
- Everything after the first space is treated as the definition

---

## Requirements

- Python **3.9+** recommended
- Tkinter (included with standard Python installations)

## Installation
1. Clone the repository
    - git clone https://github.com/pjwallace/sat_vocabulary.git
    - cd sat_vocabulary

2.  Create and activate a virtual environment (optional):
    - python -m venv .venv
    - source .venv/bin/activate   # macOS/Linux
    - .venv\Scripts\activate      # Windows

3.  Run the Application
    - python sat_vocabulary.py
