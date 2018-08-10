points=int(input('输入分数：'))
if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade='B'
print(grade)
