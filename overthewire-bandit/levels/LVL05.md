<img width="793" height="565" alt="Screenshot_1" src="https://github.com/user-attachments/assets/bd27fed9-4ece-46a0-b723-c0ddae9c6ed8" />
# Bandit Level 4 → Level 5

### Level Goal
The password for the next level is stored in the only **human-readable file** inside the `inhere` directory.

---

### Steps

1. **List files inside `inhere`:**
   ```bash
   ls inhere

    This shows multiple files with similar names (-file00, -file01, …, -file09).

    We don’t know which one has the password, so we need to check their types.

    Check file types with file:

file inhere/*

    The file command examines each file and tells us what kind of data it contains.

    Output shows that most files are data or binary, but one of them is ASCII text.

### Example output (shortened):

inhere/-file00: data
inhere/-file01: data
inhere/-file07: ASCII text
inhere/-file08: data
...

    The ASCII text one is the human-readable file (password is inside here).

Read the content of the human-readable file:

### cat inhere/-file07

    This displays the password stored inside.

    In our case, the password is:

        4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

### Why it Worked

    ls showed us the candidate files.

    file helped distinguish binary/unreadable data from readable ASCII text.

    cat printed the contents of the text file, revealing the password.

### Final Password

4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
