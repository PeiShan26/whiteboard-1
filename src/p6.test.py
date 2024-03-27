def maximumOccurence(text):
    character = ''
    occurrence = 0
    for char in text:
        #Count the occurrence of the current character
        count = text.count(char)
        #Update the character and occurrenceif it is greater than the previous
        if count > occurrence:
            character = char
            occurrence = count
    return character, occurrence

text = input("Input: ")
character, occurrence = maximumOccurence(text)
#Display the result
print(f"Character: {character}, Occurrence: {occurrence}")