# Simple Steganography 

## [CTFlearn Challenge](https://ctflearn.com/challenge/894)
<img src="simple steganography - solved.png">

## Solutions
### Step 1:
I downloaded and renamed the image file as ```simple steganography - task.jpeg```. 

<img src="simple steganography - task.jpeg">

### Step 2:
Using ```exiftool```, I was able to get information about metadata of the image. Even though there was no flag to be seen anywhere, the ```Keywords: myadmin``` caught my attention. 
<img src="simple steganography - 1.png">

### Step 3: 
Since it is stated that this is a steganography challenge, I tried using ```steghide extract -sf``` command to solve the challenge. It basically extracts the file embedded with ```steghide```.

<img src="simple steganography - 2.png">

### Step 4: 
As we can see, the program asked to enter passphrase, which means I was in the correct path. I attempted to extract the embedded file using ```myadmin```. 

<img src="simple steganography - 3.png">

Well I did it! I was able to extract the message embedded with steghide. The data was written to the text file - ```raw.txt```.

<img src="simple steganography - 4.png">

### Step 5: 
The data inside the text file isn't the flag but it looks familiar to me - I guessed it's a Base64 encoded string. I was correct because by decoding the string, I was able to capture the flag!

<img src="simple steganography - 5.png">

### Flag: 
```CTFlearn{this_is_fun}```


