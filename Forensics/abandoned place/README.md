# abandoned place

## [CTFlearn Challenge](https://ctflearn.com/challenge/1000)
<img src="abandoned place - solved.png">

## Solutions
### Step 1:
Same as before, I downloaded the image and rename it as ```abandoned place - task.jpg```. 

<img src="abandoned place - task.jpg">

What a nice picture :)

### Step 2: 
The hint given in the question is that ```the flag is outside of the pic``` and ```dimensions```. Thus, we should pay more attention to the dimension of the image. 

First, I tried ```exiftool``` to see if I can extract any related information. Apparently, ```exiftool``` didn't work in this case. 

### Step 3: 
Based on the first hint given, I knew that I may have to modify the dimension in order to get the flag.

As the flag is hidden somewhere outside the picture, we have to increase the dimension. The fastest and easiest way to do this is to modify the dimension twice: 
- alter the length to the original width
- alter the width to the original length

### Step 4: 
Before modifying the image, I first made two copies of the original image, 
```abandoned place2.jpg``` and ```abandoned place3.jpg``` respectively. 

### Step 5: 
Upon my research on the dimension of a ```jpg``` file, I discovered that the hex values of the dimension are stored 4 places after ```ffc0``` , which is the Start of Frame of a ```jpg``` file. 

Thus, we can modify the dimension through hex editors. This time round, instead of using ```HxD```, I thought using ```hexedit``` in the command prompt would be more straightforward.  

<img src="abandoned place - 1.png">

### Step 4: 
Once I located ```ffc0``` in the hex dump, I was able to find the width (```0384```) and the length (```07e0```) of the image.

<img src="abandoned place - 2.png">
<img src="abandoned place - 3.png">

### Step 5: 
I modified the dimension according to the 1st point stated in ```Step 3```. 

<img src="abandoned place - 4.png">

### Step 6: 
I modified the dimension according to the 2nd point stated in ```Step 3```. 

<img src="abandoned place - 5.png">
<img src="abandoned place - 6.png">

### Step 7: 
When I opened the modified```abandoned place2.jpg```, I could immediately capture the flag!

<img src="abandoned place2.jpg">

### Flag: 
```urban_exploration```

## End Notes
This was my last forensic challenge but I definitely loved it so much!!! Other than what learned from the previous challenges, it requires new and deeper forensic knowledge such as modification of dimension. Never regret attempting this challenge!

