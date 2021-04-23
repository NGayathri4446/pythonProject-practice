my_boolean=True
print(my_boolean)

square={1:2,2:3,3:"error",4:5}
square[8]=64
square[3]=9
print(square)

prime={1:2,2:3,4:7,7:17}
print(prime[prime[4]])

nums={
    1:"one",
    2:"two",
    3:"three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


print("new")
paris={1:"apple",
       "orange":[2,3,4], True:False, None:"True",}
print(paris.get("orange"))
print(paris.get(7))
print(paris.get(12345,"not in dist"))