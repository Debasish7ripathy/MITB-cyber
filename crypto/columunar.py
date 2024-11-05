import math
def colTransencrypt(txt,key):

    txt=txt.replace(" ","").upper()
    keylen=len(key)
    rows=math.ceil(len(txt)/keylen)

    grid=["" for _ in range(keylen)]

    for i,char in enumerate(txt):
        grid[i%keylen]+=char


    sortedkey=sorted(list(enumerate(key)),key=lambda x:x[1])

    encryptedmsg="".join(grid[i[0]] for i in sortedkey)

    return  encryptedmsg

txt="this is dumb"
enc=colTransencrypt(txt,"HELLO")
print(enc)
