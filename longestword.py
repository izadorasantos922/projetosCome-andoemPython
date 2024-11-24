str = "Hello my name is izadora and i have 19 years old and i like to code"
def longestword(str):
    longestword = ""
    array = str.split(" ")
    for word in array:
        if (len(word) > len(longestword)):
            longestword = word
    print(longestword)

longestword(str);
