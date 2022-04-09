# GandalfTheWise

## [CTFlearn Challenge](https://ctflearn.com/challenge/936)
<img src="gandaif - solved.png">

## Solutions
### Step 1:
I downloaded the image file and renamed it as ```gandaif - task.jpg``` for my own conveniency to recognise the file. 

<img src="gandaif - task.jpg">

### Step 2: 
This aim of this challenge is to help beginners to discover XOR - which I didn't know before so I spent plenty of time to solve this. 

As before, I utilised ```exiftool``` as well as ```strings```. From the output, I recognised the 3 Base64 encoded strings so I tried to decode them but none of them brought me to the flag or any hints about it. 

<img src="gandaif - 1.png">

### Step 3: 
In order to solve this, we should apply XOR function. Since XOR takes in 2 arguments, based on the output strings, we would have 3 pairs of arguments. I tried all pairs until I got the right flag. 

<img src="gandaif - 2.png">

### Step 4: 
Since XOR takes in hex as arguments, I had to first convert them from Base63 to Hex. Here I used [CyberChef](https://gchq.github.io/CyberChef). 

<img src="gandaif - 3.png">
<img src="gandaif - 4.png">

### Step 5: 
Once I got the hexadecimal forms, I calculated their XOR with an [online XOR Calculator](https://xor.pw/#). 

<img src="gandaif - 5.png">

The function output another hexdump so in order to get the flag, I would need to revert it using ```xxd -r -p```.  

<img src="gandaif - 6.png">

### Flag: 
CTFlearn{Gandalf.BilboBaggins}

## End Notes:
Not an easy one in my opinion. But definitely worth the time because I was able to learn new means to solve this kind of challenges. 