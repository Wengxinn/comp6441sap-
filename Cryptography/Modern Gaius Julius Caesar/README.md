# Modern Gauis Julius Caesar

## [CTFlearn Challenge](https://ctflearn.com/challenge/885)
<img src="modern julius caesar - solved.png">

## Solutions
### Step 1:
This is definitely one of trickiest challenges! I first used Cyptii - Julius Caesar Cipher to decrypt the message but unfortunately, I couldn't get the correct flag. 

### Step 2: 
In the question, it is mentioned that ```Why should you use Alphabet when you have your keyboard?``` This seems weird at first glance but it actually gives the biggest hint - ```keyboard```. 

I looked at my keyboard for so long, trying to see if I could discover anything. And YES! I finally got it after 10 minutes. 

```Hint: Try comparing 'BUH' and 'CTF' in the keyboard.```

### Step 3: 
The plaintext characters are located at 2 positions  to the left of their corresponding ciphertext characters. 

Following the specified pattern, I was able to find the flag. 

### Flag
```CTFlearn{Cyb3r_Cae54r}```

## End Notes
I have never paid this much attention to my keyboard before encountering this challenge...