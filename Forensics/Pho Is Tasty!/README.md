# Pho Is Tasty!

## [CTFlearn Challenge](https://ctflearn.com/challenge/971)
<img src="pho is tasty - solved.png">

## Solutions
### Step 1:
After I have downloaded the image, I renamed it as ```pho is tasty - task.jpg```.

<img src="pho is tasty - task.jpg">

### Step 2: 
I started with ```exiftool``` and ```strings``` but neither of them gave me any information about the flag. 

### Step 3: 
After I have done some lookups, I thought I could get some hints about the flag through a ```hex editor```. In this case, I used a commonly-used hex editor for Windows - ```HxD```. 

<img src="pho is tasty - 1.png">

Hooray! Got the flag immediately!

### Flag: 
```CTFlearn{I_Love_Pho!!!}```

## End Notes
This was my first time encountering challenge that requires hex editors. I got to learn about another useful tool to solve forensic-related challenges. 
