<<<<<<< HEAD
# OSINT Username Checker 🔎

A small Python project that checks whether a username can be found on public websites.

I made this project to practice Python, HTTP requests, error handling and working with external websites.

## How it works

You enter a username, and the program checks the selected websites.

For example:

```text
Enter username: J4m80

GitHub: FOUND
URL: https://github.com/J4m80
```

If the profile doesn't exist:

```text
GitHub: NOT FOUND
```

The project currently starts with GitHub, but I plan to add more platforms in the future.

## What I learned

While making this project, I'm practicing:

* Python modules and functions
* HTTP requests
* HTTP status codes
* Error handling
* Working with external websites
* Returning and processing structured data
* Organizing a Python project

## Tech

* Python 3
* Requests

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd osint-checker
```

Install the required library:

```bash
pip install -r requirements.txt
```

Then run the program:

```bash
python main.py
```

## Project structure

```text
osint-checker/
│
├── main.py
├── checker.py
├── requirements.txt
├── .gitignore
└── README.md
```

`main.py` handles user input and displays the results.

`checker.py` contains the username checking logic.

`requirements.txt` contains the external Python libraries used by the project.

## Plans for the project

This project is still a work in progress. I plan to add:

* [x] GitHub checker
* [x] GitLab checker
* [x] Instagram checker
* [x] TikTok checker
* [ ] Export results to JSON
* [ ] Better terminal interface
* [ ] Simple GUI

## Disclaimer

This project is made for educational purposes and works with publicly available information.

Finding the same username on different websites does **not** mean that the accounts belong to the same person.

## License

MIT
=======
# osint-checker
Python-based OSINT username checker that searches for profiles across multiple websites.
>>>>>>> 454496ec812453cfc810d30223ea2f83221bacaa
