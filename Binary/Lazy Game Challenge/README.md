# Lazy Game Challenge

## [CTFlearn Challenge](https://ctflearn.com/challenge/691)
<img src="lazy game challenge - solved.png">

## Solutions
### Step 1:
First, I connected the server through the command line specified in the question - ```nc thekidofarcrania.com 10001```. 

<img src="lazy game challenge - i.png">

### Step 2:
I randomly placed a bet and input different numbers between 0 to 9. 
I won a JACKPOT, apparently. But the flag was nowhere to be found. 

<img src="lazy game challenge - 1.png">

### Step 3: 
I realised that the game follows the concept of binary exploitation, which requires us to break the logic in a binary file. 

Thus, I repeated the game. I randomly placed a bet and entered numbers that are not in the range of 0 to 9. I even input some negative values. However, this still didn't lead me to the flag. In fact, it was even worse because I lost the game :(

<img src="lazy game challenge - 2.png">

### Step 4: 
I played the game again. This time round, I changed the direction to the bet I place before the game started. 

```My bet: -$1000000```

<img src="lazy game challenge - 3.png">

### Step 5: 
I understand this was totally nonsense but it actually worked! HOORAY!!!I got the flag! 

<img src="lazy game challenge - 4.png">

The logic works behind this is that if I placed a negative bet (in this case is -$1000000), the program will subtract the bet I placed from the money I owned ($500) when all my 10 guesses were incorrect. 
```Hint: 500 - (-1000000)```

Instead of minus, the program actually added $1000000 to my account. 

I am RICH RICH :)

### Flag: 
```CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}```

## End Note: 
I wish too :(