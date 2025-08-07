# Offensive Security Intro - TryHackMe Challenge

## Objective
Get introduced to offensive security concepts and basic reconnaissance tools used by red teamers.

## Key Concept
To be an effective red team ethical hacker, **you need to think like a hacker** — understanding how attackers explore and exploit systems.

## Command Used

gobuster -u http://fakebank.thm -w wordlist.txt dir

## Explanation of the Command

    gobuster: A tool used for brute forcing URIs (directories/files) and DNS subdomains.

    -u http://fakebank.thm: Target URL to scan.

    -w wordlist.txt: The wordlist containing common directory names to test.

    dir: Mode of operation telling gobuster to brute force directories.

 
## Results / Observations

-Found several hidden directories on the fakebank.thm web server.

-was able to transfer myself some money from a hacked account through a secure lab within the THM challenge.
