# Blank Page

## [CTFlearn Challenge](https://ctflearn.com/challenge/959)
<img src="blank page - solved.png">

## Solutions
### Step 1:
I downloaded the text file and renamed it as ```blank page - task.txt```. 

### Step 2: 
I used ```exiftool``` first but there was not hint about the flag. It should be noted that ```strings``` command wouldn't work in this case since it is a blank text file. 

### Step 3: 
I tried to examine the file through hex dumps instead. This time I used ```xxd``` command to obtain the hex dump of the file. 

<img src="blank page - 1.png">

### Step 4: 
The hex dump seems interesting because it contains the combination of dots and blanks only. 

We may guess it is a morse code at first glance but morse code consists of dots and dashes. 

Another possibility is binary representation. This makes senses because binary containts only 2 values, 0 and 1. Therefore, I wrote a simple python script ```blank page - script.py``` that converts the file into binary code, where ```space = 0``` and ```dots = 1```. 

```
file = open("blank page - task.txt", "r").read()
output = ""
for c in file:
	# Space
	if ord(c) == 32:
		output += "0"
	# Dots
	else:
		output += "1"
print(output)
```

### Step 5: 
I stored the output of the python program into a text file called ```blank page - bin.txt```. 

<img src="blank page - 3.png">
<img src="blank page - 4.png">

### Step 6: 
At this stage, all we have to do is to decode the binary code. In doing this, I used [CyberChef](https://gchq.github.io/CyberChef). 

<img src="blank page - 5.png">

### Flag: 
```CTFlearn{If_y0u_r3/\d_thi5_you_pa553d}```

## End Note: 
Another interesting challenge that is new to me! I would never realise a blank page file could contain any hidden message if I didn't attempt this.  