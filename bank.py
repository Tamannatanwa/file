



# banks=["HDFC","SBI","BOI","KOTAK"]
# with open("banks.txt","w") as f:
#     for i in banks:
#         f.write("\n"+i)
#         f.write("\n")
# with open ("banks","a") as f:
#     print(23*"=",file=f)
#     print(file=f)
#     print("these are the 5 banks.",file=f)
# f.close()





banks=["HDFC","SBI","BOI","KOTAK"]
with open("banks","w") as f:
    for i in banks:
        f.write("\n"+i)
        f.write("\n")
with open ("banks","a") as f:
    print("\n","these are the 4 banks.",file=f)
f.close()
                                                                                                                                                                                                                                                                                                                                                    




