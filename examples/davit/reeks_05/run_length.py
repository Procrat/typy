'''
Created on Feb 17, 2015

@author: david
'''
def rle(text):
    char = ""
    single = ""
    result = ""
    for i in text:
        if char == "":
            count = 1
            char = i
        elif char == i:
            if single != "":
                result+= "1" + single + "1"
                single = ""
            elif count == 8:
                result += "9"+char
                char = ""
            count += 1
        elif count == 1:
            if char == "1":
                char = "11"
            single += char
            char = i
        else:
            result += str(count) + char
            char = i
            count = 1
    if single != "":        
        return result + "1" + single + "1"
    if count == 1:
        if char == "1":
            char = "111"
        char += "1"
    if char == "":
        count = ""
    return result + str(count) + char
print(rle("B"))
print(rle('PPPPPPPPP'))
print(rle('AAAAAABCCCC'))
print(rle('JJJJ5555IIIIIIIIIIIIIIIIUUUUUUJJJJJJJJJJJ33333333DD0000IIBBBBBBBBBBBBBQQ777777777777444444444444444SSSSSSSS'))