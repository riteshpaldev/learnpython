indianteam = {}
rolesize = 3
rolename = {"0":"ballor","1":"batsman","2":"wicket keeper", "3":"captain"}
for i in rolename:
    print("pleae find the role in cricket team", i )
for i in rolename.values():
    print("pleae find the role in cricket team", i )
teamsize = 2
playername = []
for i in range(0, teamsize):
    print("Enter player name  at index", i, )
    name = str(input())
    print("Enter role name  at index", i, )
    item1 = str(input())
    print(eval(item1))
    print(rolename[eval(item1)])
    #indianteam.update('name') = item1
    indianteam[name] = item1
    #item = str(input())
    #playername.append(item)
print("User list is ",indianteam)
#indianteam = {"Virat Kohli":"Batsman", "Rohit Sharma":"Batsman","KL Rahul":"batsman","Suryakumar Yadav":"batsman","Rishabh Pant":"Wicketkeper","Ishan Kishan":"wiketkeper","Hardik Pandya":"all rounder","Ravindra Jadeja":"all rounder",
#"Rahul Chahar":"Spinners","Ravichandran Ashwin":"Spinners","Varun Chakravarthy":"Spinners","Jasprit Bumrah":"Fastbowler","Bhuvneshwar Kumar":"fast bowler","Mohammed Shami":"fast bowler","Shardul Thakur":"fast baller" }
#indianteam = {}
#indianteam[playername] = 'role'
#for i in indianteam:
 #   print( item = str(input())
    #rolename.append(itemm)
#print("role list is ",rolename)
#rolename = {"0":"ballor","1":"batsman","2":"wicket keeper", "3":"captain'}:
