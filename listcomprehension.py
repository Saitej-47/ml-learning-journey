num=[x for x in range(1,11)]

odd_cubes=[x**3 for x in num if x%2!=0]

result=list(filter(lambda x: x >50,odd_cubes))
print(result)


