# Chalkboard

## [CTFlearn Challenge](https://ctflearn.com/challenge/972)
<img src="chalkboard - solved.png">

## Solutions
### Step 1:
I downloaded the image and renamed it as ```chalkboard - task.jpg```. 

<img src="chalkboard - task.jpg">

### Step 2: 
First, I used ```exiftool```. 

<img src="chalkboard - 1.png">

### Step 3: 
Under Comment, it is stated that the flag is of the form ```CTFlearn{I_Like_Math_x_y}``` where x and y are the solution to equations: 
 - ```3x + 5y = 31```
 - ```7x + 9y = 59```

<img src="chalkboard - 2.png">

I guess this challenge aimed to test our maths LOL... But anyways, solving this should be kinda easy. I got ```x = 2``` and ```y = 5```. 

### Flag: 
```CTFlearn{I_Like_Math_2_5}```