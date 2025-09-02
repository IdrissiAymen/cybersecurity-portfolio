### The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions 

<img width="631" height="44" alt="OTW12" src="https://github.com/user-attachments/assets/0faab61c-3a03-4266-ba1d-01cc471312fb" />

#### Use tr to apply ROT13 decoding
ROT13 works by shifting letters A–Z and a–z by 13 characters.
The tr command can do this translation

### cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

A-Za-z → matches uppercase + lowercase letters.

N-ZA-Mn-za-m → shifts them by 13 positions.
