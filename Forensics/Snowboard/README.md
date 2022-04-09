# Snowboard

## [CTFlearn Challenge](https://ctflearn.com/challenge/934)
<img src="snowboard - solved.png">

## Solutions
### Step 1:
After downloading the image, I renamed it as ```snowboard - task.jpg```. 

<img src="snowboard - task.jpg">

### Step 2: 
I utilised ```exiftool``` to check the metadata as usual but this time, the flag was not found. I proceeded to use ```strings``` command but there were too many output strings so I filtered out the strings that have more than 10 characters. 

### Step 3: 
The flag was nowhere to be found. But wait a minute! I noticed the padding suffix - ```'='```. This indicates that the flag may have been encoded as a Base64 string. I checked if there's any another similar-patterned strings using ```strings snowboard\ -\ task.jpg | grep '='```

<img src="snowboard - 1.png">

### Step 4: 
As far as I can see, there was only one string that seems to match the pattern. I tried to decode it with Base64 and got the flag!

<img src="snowboard - 2.png">

### Flag: 
```CTFlearn{SkiBanff}```

## End Notes
Through this challenge, I learned to always try decoding possible Base64 encoded strings (especially strings ends with '=') when I counldn't get the flag. 
