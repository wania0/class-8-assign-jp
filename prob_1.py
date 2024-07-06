# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content.

# Solution:

f = open ("prob_1.txt","r")
data = f.read()
data = data.replace("user", "alice")
data = data.replace("title", "Advantages of coding")
data = data.replace("here", "https://bootcamp.berkeley.edu/blog/what-is-coding-key-advantages/")
f = open ("user_email.txt","a")
f.write(data + "\n\n")
f.close()

f = open ("prob_1.txt","r")
data = f.read()
data = data.replace("user", "bob")
data = data.replace("title", "Disadvantages of coding")
data = data.replace("here", "https://bootcamp.berkeley.edu/blog/what-is-coding-key-advantages/")
f = open ("user_email.txt","a")
f.write(data + "\n\n")
f.close()

f = open ("prob_1.txt","r")
data = f.read()
data = data.replace("user", "charlie")
data = data.replace("title", "coding")
data = data.replace("here", "https://bootcamp.berkeley.edu/blog/what-is-coding-key-advantages/")
f = open ("user_email.txt","a")
f.write(data + "\n\n")
f.close()




