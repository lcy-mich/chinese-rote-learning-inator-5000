from string import punctuation, ascii_letters, digits
from re import escape, sub

sift = r'[{}]'.format(escape(punctuation + ascii_letters + digits + '∞⁺∫⁻＝＋「」\n \t•…—，。！？、；：‘’“”《》（）［］【】'))

with open("input.txt","r", encoding="utf-8") as file:
    text = sub(sift, "", file.read())

dictionary = dict()

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

with open("extracted_chars.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join([item[0] for item in sorted_items]))


#bro like after extracting make sure to double check that the characters
#are all properly filtered cus there are some wonky ass characters that get
#used. at least from the webnovel site i got the input texts from
