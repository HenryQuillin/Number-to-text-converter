# Num to text converter
number = (input('Enter numbers: '))
dic = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for e in number:
    output += dic.get(e) + " "
print(output)
