# Python Terminal Hangman 

A classic Hangman game built entirely in the command line. I built this to practice string manipulation, input validation, and working with Python's built-in modules.
Key Features:
* **Dynamic ASCII Art:** Uses a Python dictionary to track and render different stages of the hangman based on the user's wrong guess count.
* **Clean Terminal UI:** Utilizes the `os` and `time` modules to clear the screen and create smooth, frame-by-frame loading effects for a better user experience.
* **Smart Input Handling:** Validates user input to prevent numbers or multi-letter guessing, and uses `enumerate()` to accurately place correctly guessed letters in the hidden word.
