def friendsInTrouble(j_angry, s_angry):
    if ((j_angry == "Yes" or j_angry == "yes") and (s_angry == "Yes" or s_angry == "yes")):
        print("You are in trouble")
        return True
    elif((j_angry == "No" or j_angry == "no") or (s_angry == "No" or s_angry == "no")):
        print("You are not in trouble")
        return False
    

j_angry = input("Is John angry?: ")
s_angry = input("Is Smith angry?: ")
      
friendsInTrouble(j_angry, s_angry)


