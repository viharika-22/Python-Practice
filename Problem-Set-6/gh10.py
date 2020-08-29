li1=["Arjun", "Sameeth", "Yogesh", "Vikas" , "Rehman","Mohammad", "Naveen", "Samyuktha", "Rahul","Asifa","Apoorva"]
li2= ["Subramanian", "Aslam", "Ahmed", "Kapoor", "Venkatesh","Thiruchirapalli", "Khan", "Asifa" ,"Byomkesh", "Hadid"]
fname=max(li1,key=len)
lname=max(li2,key=len)
longname=fname+" "+lname
print(longname)
ln=longname[::2]
for i in ln:
    
