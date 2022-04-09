# Git Is Good

## [CTFlearn Challenge](https://ctflearn.com/challenge/104)
<img src="git is good - solved.png">

## Solutions
### Step 1:
First, I downloaded the folder, ```gitIsGood```. 

### Step 2: 
As mentioned in the question, the flag was redacted when I opened the text file. However, this question is straightforward since it gave the biggest hint - ```git```. 

According to thsi [website](https://git-scm.com/docs/user-manual#repositories-and-branches), ```git show``` command shows the most recent commit on the current branch, as well as the changes made in the commit. Therefore, using this command can got me to the flag. 

<img src="git is good - 1.png">

### Flag: 
```flag{protect_your_git}```

## End Notes: 
Learned new things about ```git``` :)