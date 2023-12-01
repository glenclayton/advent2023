def find_number(s):
    res = [int(i) for i in s if i.isdigit()]
    num=res[0]*10+res[len(res)-1]
    print(f"{s}={num}")
    return num

numberlist=['one','two','three','four','five','six','seven','eight','nine']

def replace_text(s):
    for i in range(1,len(numberlist)):
        s=s.replace(numberlist[i+1],str(i))
    return s



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