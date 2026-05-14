
import pyshorteners


def shorten_URL(url): 

    s = pyshorteners.Shortener()

    print(s.tinyurl.short(url))
  

  
print("Enter a URL to be shortened")

user_url = input()

shorten_URL(user_url)


print ("Exit? (e to exit) ")

exit = input()



