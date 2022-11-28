# Write an algorithm to find the largest common prefix between elements of an array.
# example - input = ["flower", "flow", "floor"] ----> output = "flo".
# flo is the common prefix between all 3 elements of the array.
# If there is no common prefix then return empty string.


def commonPrefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for ele in strs[1:]:
            
            # first checking for out of bound condition because different words can have different length 
            if i == len(ele) or ele[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result

print(commonPrefix(["flower","flow","floor"]))
