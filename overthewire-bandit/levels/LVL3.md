<img width="819" height="575" alt="overthewire2" src="https://github.com/user-attachments/assets/8efa2503-b88c-46be-846f-acbf71204246" />

### Bandit Level 2 → Level 3

In this level, the password was stored in a file named `--spaces in this filename--` inside the home directory. The challenge came from the filename starting with `--`, which most commands interpret as an option rather than a file. Normally, running `cat "--spaces in this filename--"` would fail because `cat` thinks it is being given a flag. To solve this, we explicitly referenced the file in the current directory using `./`, and escaped the spaces with backslashes:  
```bash
cat ./--spaces\ in\ this\ filename--

This worked because ./ tells the shell to treat it as a path instead of an option, and the \ ensures spaces are handled correctly. An alternative method would be cat -- --spaces\ in\ this\ filename--, where -- signals the end of options. The output was the password for the next level:

MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

Key Point: When filenames begin with - or --, commands often misinterpret them as options. Using ./filename or -- filename ensures the command treats them as files.

