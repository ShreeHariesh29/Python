email = input("Email = ")
password = input("Password = ")
DomainSpilting = email.split(".") #["AABBCC@gmail","com"]
domain = "."+DomainSpilting[1]
domainlist = [".com",".in",".org"]
mailList = ["gmail","yahoo","email"]
mailSpilt = email.split("@")
print(mailSpilt)
aa = mailSpilt[1]
mailSplit2 = aa.split(".")
print(mailSplit2)
mail = "@"+mailSplit2[0]
print(mail)

for a in range(1,2):
    for b in range(0,len(domainlist)):
        if(domain == domainlist[b]):
            print("valid domain")
    for c in range(0,len(mailList)):
        if(mail == "@"+mailList[c]):
            print("valid mail")

# if(domain == ".com" or domain == ".in" or domain == ".org"):
#     print("valid")

# print(domain)