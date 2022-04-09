# Taking LS

## [CTFlearn Challenge](https://ctflearn.com/challenge/103)
<img src="taking ls - solved.png">

## Solutions
### Step 1:
After I have downloaded the zip file, I unzipped it and obtained an extracted folder, ```The Flag```. 

### Step 2:
Since the hidden flag is inside this folder, we can use ```ls``` to list all the files. This gave me only 1 directory - ```The Flag.pdf```. The file requires password to be opened. 

### Step 3: 
At this point there is no other information about the password. I went back through the question to see if I could find any extra hints. The hints were quite obvious - LS and hidden. In other words, I should have used ```ls -a``` to list all the files (including the hidden files). 

<img src="taking ls - 1.png">

There we go! There's a hidden folder - ```.ThePassword```.

### Step 4: 
The password is inside the text file. 

<img src="taking ls - 2.png">

Password: ```Im The Flag```

### Step 5:
Using the password given to open the pdf file gave me the flag.

<img src="taking ls - 3.png">

### Flag:
```ABCTF{T3Rm1n4l_is_C00l}```

## End Notes
I was dumbfounded when I realised I could just manully open the ```The Flag``` folder (without using the command prompt) since it's a lot easier :) Nonetheless, this challenge reminds me to always try ```ls -a``` because I nearly forgot hidden files exist and they wouldn't be listed if ```ls``` is used. 