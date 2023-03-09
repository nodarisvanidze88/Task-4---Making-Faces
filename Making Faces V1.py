                                # convert text to emoji
text = input()                                              # get user's Text

emos= {                                                     # create emoji dictionary
    ":)" : "😀",
    ":(" : "😞",
    ":|" : "🤨"
     }

def textToEmoji(st, em):                                    # function replace  in text something from dictionary
    splitedString = st.split()                                 # split the text and get item's list
    counter = 0                                                # create initial counter value for "For" loop
    for i in splitedString:                                    # run loop for check each list element
        if i in em:                                            # creat conditional logic if item is in dictionary
            splitedString[counter] = em[i]                     # if true replace item from dictionary value
        counter += 1                                           # increace counter value by 1
    result = " ".join(splitedString)                           # convert list to text
    return result                                              # get result

print(textToEmoji(text, emos))                              # run function and finaly get the result
