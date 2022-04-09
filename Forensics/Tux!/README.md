# Tux!

## [CTFlearn Challenge](https://ctflearn.com/challenge/973)
<img src="tux - solved.png">

## Solutions
### Step 1:
I first downloaded the given image and renamed it as ```tux - task.jpg```. 

<img src="tux - task.jpg">

### Step 2: 
As usual, I first examined the image using ```exiftool```. 

<img src="tux - 1.png">

By looking at the Comment of the image, it seems that the flag had been encoded as a Base64 string. 

<img src="tux - 2.png">

### Step 3: 
In order to validate my thoughts, I tried to decode the string. Surprisingly, what I got was not the flag but a password. This indicates that I need to open some files using this password to capture the flag. 

<img src="tux - 3.png">

### Step 4: 
This leads me to the thoughts that there're probably some hidden files inside the image. I used [CyberChef - Extract Files](https://gchq.github.io/CyberChef) to extract the hidden files. 

<img src="tux - 4.png">

### Step 5: 
2 of the files are zip files that means we have to unzip both of them to see which file contains the flag. (Ignore the image file since it is the original image). 

It was found ```extracted_at_0x1570``` was the correct file because the other file couldn't be unzipped successfully. 

I was able to find the flag in ```flag``` file. 

<img src="tux - 5.png">

### Flag: 
```CTFlearn{Linux_Is_Awesome}```

## End Notes
This challenge requires knowledge I have learned from previous solved challenges (Base64, hidden files, etc.). I was lucky to encounter related challenges (easier ones) before this. 