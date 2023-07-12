import random
suzlar=["salom","ronaldo","messi","ozil","saloh"]
compyuter=random.choice(suzlar)
player=""
while player!="stop":
    player=input("salom,ronaldo,messi,ozil,saloh shulardan birni kiriting:").lower()
    if player=="stop":
        print("dastur tugadi")
        break
    if compyuter==player:
        print(f"siz tugri topdiz compyuter uylagan suz:{compyuter} edi")
    else:
        print(f"siz tugri topa olmadiz compyuter uylagan suz:{compyuter} edi")
    compyuter=random.choice(suzlar)
