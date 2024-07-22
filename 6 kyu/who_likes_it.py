def likes(names):
# Description
  # Given an array of users who like a post on facebook, create an output statement that shows the first 3 users and any extra number of likers otherwise, return a message that no one liked the post

  
#     Getting the length of the array
    arrLen = len(names)
    
#   Bool check for no of users
    sing = arrLen < 2
    doub = arrLen < 3
    trip = arrLen < 4
    
#     Empty Array Logic
    if arrLen <= 0:
        return "no one likes this"
    elif arrLen > 0:
#         Has likes logic
        if sing == 1:
            return names[0]+" likes this"
        elif doub == 1:
            return names[0]+" and "+names[1]+" like this"
        elif trip == 1:
            return names[0]+", "+names[1]+" and "+names[2]+" like this"
        else:
            return names[0]+", "+names[1]+" and "+str(arrLen-2)+" others like this"
