# SHA-256 Password Hasher

## Overview

This Python script:

* Takes 10 user-input passwords (minimum 7 characters)
* Hashes them using SHA-256
* Saves results to `rainbow.csv`
* Adds a random PIN + salt to each hash
* Saves updated data to `rainbow2.csv`

## How to Run

1. Update file paths (`your_computer\\...`)
2. Run:

   ```
   python script.py
   ```
3. Enter 10 passwords when prompted

## Notes

* Passwords shorter than 7 characters are skipped
* This is for learning purposes, not production security
