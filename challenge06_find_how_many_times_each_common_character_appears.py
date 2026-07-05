text1 = "banana"
text2 = "bandana"

freq1 = {}
freq2 = {}
common = {}

for ch in text1:
        freq1[ch] = freq1.get(ch,0) + 1
        
for ch in text2:
        freq2[ch] = freq2.get(ch,0) + 1
        

for ch in freq2:
        if ch in freq1:
            common[ch] = min(freq1[ch], freq2[ch])
            

if common:
       print("Common characters:", common)
else:
       print("No common characters found.")

