def railfence(txt,depth):
    txt=txt.replace(" ","").upper()
    rail=['']*depth
    direction=False
    row=0
    for char in txt:
        rail[row]+=char
        if row==0 or row ==depth-1:
            direction=not direction
        row+=1 if direction else -1
    return "".join(rail)

print(railfence("hello i am debasish",4))