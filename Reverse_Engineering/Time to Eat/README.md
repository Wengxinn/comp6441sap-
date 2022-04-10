# Time to Eat

## [CTFlearn Challenge](https://ctflearn.com/challenge/743)
<img src="time to eat - solved.png">

## Solutions
### Step 1: 
I first downloaded the python file and renamed it as ```time to eat - task.py```. I was confused when opened the file (the name of the variables killed me). 

### Step 2: 
The program asks for user input (flag) and displays some output indicating if the flag is correct. 

To solve this challenge, we would apply reverse engineering to reverse the functions. 

I wrote the corresponding reverse script in a python file - ```time to eat - script.py```, 

### Step 3: 
```
def Eat(eat):
    if eAT(eat) == 9:
        if EATEATEATEATEATEAT(eat[:EATEATEAT]) and\
            EATEATEATEATEATEAT(eat[eAT(eat)-EATEATEAT+1:]):
                eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    EaT("absolutely EATEN!!! CTFlearn{",flag,"}")
```
From the function above, I knew that ```eat``` should have length of 9. 

### Step 4: 
Since ```eAT(eat) = 9```, 
```
EATEATEAT = 3
EATEATEATEAT = 4
EATEATEATEATEAT = 2
```

### Step 5: 
According to this part in ```Eat(eat)```: 
```
eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))
if eateat == "E10a23t9090t9ae0140":
    flag = "eaten_" + eat
    EaT("absolutely EATEN!!! CTFlearn{",flag,"}")

```
the flag would be correct if the returned value of ```EAt(eaT(eat), Ate(aTE(aten(eat))))```, which is also called (```eateat```), equals to ```E10a23t9090t9ae0140```. 

### Step 6: 
```eateat``` can be broken down into 2 strings: 
- ```eaT(eat)```
- ```Ate(aTE(aten(eat)))```

### Step 7: 
```eaT(eat)```: 
1. ```Eating(eat[:3]) + eat[::-1]```
2. ```str(int(eat[:3])*3) + eat[::-1]```

### Step 8: 
```Ate(aTE(aten(eat)))```
1. ```Ate(aTE(eat[::-1]))```
2. ```Ate(eat[::-1])```
3. ```"Eat" + str(len(eat[::-1])) + eat[::-1][:3]```
4. ```Eat9 + eat[::-1][:3]```

### Step 9: 
Now we can proceed to reverse ```EAt(eat, eats)```.
Since the function takes in 2 strings and output another string, so in order to reverse it, I wrote a function called ```reverse_eat(eat)``` that takes in a string and outputs 2 other strings. 
```
def reverse_eat(eat):
    """
    Reverse function EAt to find the two strings - eat, eats, given eAt
    """
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = "E10a23t9090t9ae0140"
    # From original
    # Ate(aTE(aten(eat)))
    # Ate(eat[::-1]) = Eat9 + eat[::-1][:3] = Eat9 + 3 characters
    eats = "Eat9___"

    while eat1 < len(eat) and eat2 < len(eats):
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            # previously modified + current (from eAt) + remaining unknowns
            eats = eats[:eat2] + eAt[eateat] + eats[eat2+1:]
            eat2 += 1
        else:
            # previously modified + current (from eAt) + remaining unknowns
            eat = eat[:eat1] + eAt[eateat] + eat[eat1+1:]
            eat1 += 1
        eateat += 1

    return eat, eats
```

### Step 10: 
For the first string ```eaT(eat)```, there will be 2 possible choices: 3 
Note that there will be two possible choices for the first string - ```eaT(eat)```: 3-digit or 4-digit numbers as the result of ```str(int(eat[:3])*3)```. 

Hence I decided to passed in 2 possible patterns as arguments. 
```
# 4 digits
eat, eats = reverse_eat("----_________")
# Check eat and eats - eat[4:7] and eats[-3:] are both starts of original eat
if eat[4:7] == eats[-3:]:
    print(str(int(eat[:4]) // 3) + eat[4:len(eat)-4+1][::-1])

# 3 digits 
eat, eats = reverse_eat("---_________")
# Check eat and eats - eat[3:6] and eats[-3:] are both starts of original eat
if eat[3:6] == eats[-3:]:
    print(str(int(eat[:3]) // 3) + eat[3:len(eat)-3+1][::-1])
```

### Step 11: 
By running the python program, I got the flag!
<img src="time to eat - 1.png">

### Flag: 
```341eat009```

## End Notes
Time to EATTTT! I am hungry :P