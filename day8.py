words=["ich","komme","aus","Deutschland","gut"]
for w in words :
    if len(w)>4:
        print(w.upper())
    else:
        print(w+" is short")
        print("finished!")