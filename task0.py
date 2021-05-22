#1.program
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 7:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
#2.program		
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#3.program
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog'))
#4.program
n=5
n1 = int("%s" %n)
n2 = int("%s%s" %(n,n))
n3 = int("%s%s%s" %(n,n,n))
print(n1+n2+n3)
#7.program
d={'rahul':57,'kishore':87,'vidya':67,'raakhi':79}
print(max(d,key=d.get))
#8.program
a = "hello world!123"
d=i=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        i=i+1
    else:
        pass
print("Letters", i)
print("Digits", d)
#6.program
items = "without,hello,bag,world"
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
#11.program
pos = {"x":0,"y":0}
while True:
    n =input()
    if not n:
        break
    direction,steps=n.split()
    if direction=="UP":
        pos["y"]+=int(steps)
    elif direction=="DOWN":
        pos["y"]-=int(steps)
    elif direction=="LEFT":
        pos["x"]-=int(steps)
    elif direction=="RIGHT":
        pos["x"]+=int(steps)
print (int(round((pos["x"]**2+pos['y']**2)**0.5)))
#9.program
d = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

newData = {'Name' : [],'Ratings' : []}
index = 0
for sub in d['Subject']:
    if(sub == 'Python'):
        newData['Name'].append(d['Name'][index])
        newData['Ratings'].append(d['Ratings'][index])
    index += 1 

print('new dictionary of students : ',newData)

##5.program
input_string =input('enter the stringin required fashion:')
input_list = input_string.split('#')
list_1 = input_list[0].split()
list_2 = input_list[1].split()
list_1 = [int(i) for i in list_1]
list_2 = [int(i) for i in list_2]
print('list_1:',list_1)
print('list_2:',list_2)
#10.program
n= int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False  
        print(i, value)
        
divChecker(n)  
