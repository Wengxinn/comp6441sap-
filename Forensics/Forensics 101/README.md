# Forensics 101

## [CTFlearn Challenge](https://ctflearn.com/challenge/96)
<img src="forensics 101 - solved.png">

## Solutions
### Step 1:
First, I downloaded the file and renamed it as ```forensic 101 - task.png```. 

<img src="forensics 101 - task.jpg">

### Step 2:
I started examining the image using ```exiftool``` but unfortunately there was no flag in the metadata shown so I tried using ```strings``` command. 

<img src="forensics 101 - 1.png">

### Step 3: 
Scrolling through the output gave me the flag!

<img src="forensics 101 - 2.png">

### Flag: 
 ```flag{wow!_data_is_cool}```

## End Notes
YAY! I was so excited for solving my first ever CTF challenge. This challenge is pretty easy but it actually prepared me for solving further digital forensic challenges - always starts with ```exiftool``` and ```strings```.