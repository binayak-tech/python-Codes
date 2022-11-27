def reverse(string):
    # Method 1
    #  return string[::-1]

    # Method 2
    if len(string) <= 1:
      return string
    return string[len(string)-1] + reverse(string[0:len(string)-1])

print(reverse("Binayak"))