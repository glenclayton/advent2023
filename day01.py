def find_number(s):
    res = [int(i) for i in s if i.isdigit()]
    num=res[0]*10+res[len(res)-1]
    print(f"{s}={num}")
    return num

numberlist=[('twone',21),('sevenine',79),('eighthree',83),('one',1),
('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9)]

def replace_text(s):
 #   print(f"replace_text {s}")
    on=len(s)
    minf=999
    minn=0
    mins=''
    for i in range(1,len(numberlist)+1):
        tnum = numberlist[i-1]
        occ = s.find(tnum)
        if occ>=0 and occ<minf:
            minf= occ
            minn= i
            mins= tnum
    if(minn>0):        
        s=s.replace(mins,str(minn),1)
 #   print(f"{len(s)} - {minf} - {len(mins)}")
    if (len(s) - minf - 1) < 3 or minn==0:
         return s
  #  print(f"Recursion {s[:minf+1]} {s[minf+1:]}")
    return s[:minf+1]+replace_text(s[minf+1:])



text_file = open("data/input.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()

t1 = "a1b2c"
o1 = find_number(t1)
print(o1)
rt = 0
for line in lines:
    rt = rt + find_number(line)

print(f"Final total = {rt}")

t2 = "onehdhtwo"
o2 = replace_text(t2)
print(o2)

rt = 0
for line in lines:
    num=find_number(replace_text(line.replace('\n','')))
    rt = rt + num
    print(f"{line} = {num} rt={rt}")
print(f"Final total = {rt}")

t2 = "twone"
o2 = replace_text(t2)
print(o2)

print(f"Final total = {rt}")