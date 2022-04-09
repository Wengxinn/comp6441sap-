# Binwalk 

## [CTFlearn Challenge](https://ctflearn.com/challenge/108)
<img src="binwalk - solved.png">

## Solutions
### Step 1:
I downloaded the image and renamed it as ```binwalk - task.jpeg```. 

<img src="binwalk - task.jpeg">

### Step 2: 
This main purpose of this challenge is to extract the hidden file inside the image. Of course, we can use ```binwalk```, but I decided to use [CyberChef - Extract Files](https://gchq.github.io/CyberChef/) instead.

<img src="binwalk - 1.png">

### Step 3: 
We can see that there are 10 files found. I tried to find the flag by opening each and every single of them. The flag is inside the last file - ```extracted_at_0x25795.png```.  

<img src="binwalk - 2.png">

### Flag: 
```ABCTF{b1nw4lk_is_us3ful}```

