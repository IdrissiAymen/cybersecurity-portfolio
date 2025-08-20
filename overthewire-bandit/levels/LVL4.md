<img width="816" height="584" alt="overthewire3" src="https://github.com/user-attachments/assets/c3960893-fb4f-4e0e-ba6b-083a23e62ffb" />

### Bandit Level 3 → Level 4

In this level, the goal was to find the password hidden somewhere inside the `inhere` directory. After navigating into the folder, a normal `ls` command did not reveal anything useful. However, using the `-a` option with `ls` (`ls -a`) displayed hidden files as well. Among the results, a suspicious file named `...Hiding-From-You` appeared.  

To view its contents, we used `cat` on the file:  
```bash
cat inhere/...Hiding-From-You

2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

