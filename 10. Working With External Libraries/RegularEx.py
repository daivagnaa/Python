import re
text = "Dog is barking out loud on other dog"

match = re.search("loud", text)
if match:
    print("Match Found")
    print("Start index :",match.start())
    print("End index :",match.end())

matches = re.findall("Dog" , text , re.IGNORECASE)
print("Matches :",matches)

new = re.sub("Dog", "Pakistani" , text)
print(f"New Text : {new}")