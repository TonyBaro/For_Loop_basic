for x in range(151):
    print(x)

for x in range(1000):
    if x%5==0:
        print(x)

for x in range(101):
    if x%10==0:
        print("Coding Dojo")
    elif x%5 ==0:
        print("Dojo")
    else:
        print(x)

sum1=0
count=0
while count<=500000:
    if count%2!=0:
        sum1=sum1 + count
    count=count+1
else:
    print(sum1)

byfours=2018
while byfours>=0:
    print(byfours)
    byfours=byfours-4

lowNum=2
highNum=9
mult=3
for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)

