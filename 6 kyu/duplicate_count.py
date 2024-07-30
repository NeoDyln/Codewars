def duplicate_count(text):
# #     Logic used:
# Convert all text to either upper or lowercase
# Find out how may times each letter occurs in the text
# Extract letters where occurence occurred more than once
# Get same letters as set hence unique letters
# Get length (Count) of those unique letters and return
    text2 = text.upper()
#     Holder for no of occurrences at each index
    occs =[]
#     Holder of duplicate letters
    dups = []
    
#     Occurrences counter 1
    for letter in text2:
        count = 0
        for letter2 in text2:
            if letter == letter2:
                count += 1
        occs.append(count)
        
#         Duplicate extract
    for i in range(len(occs)):
        if occs[i] > 1:
            dups.append(text2[i])
# Obtain unique (set) letters then get length(count) of occurrences
    return len(set(dups))
