my_boolean = True
print(my_boolean)

square = {1: 2, 2: 3, 3: "error", 4: 5}
square[8] = 64
square[3] = 9
print(square)

prime = {1: 2, 2: 3, 4: 7, 7: 17}
print(prime[prime[4]])

nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

print("new")
paris = {1: "apple",
         "orange": [2, 3, 4], True: False, None: "True", }
print(paris.get("orange"))
print(paris.get(7))
print(paris.get(12345, "not in dist"))

print("new")
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(7,5))

print("new")
words=("spam","eggs","SPAM")
print (words[0])

print("new")
my_tuple=(1,(1,2,3))
print(my_tuple[1])

print("new")
squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[5:7:-1])

cubes=[i**3 for i in range(5)]
print(cubes)
print("new")
evens=[i**2 for i in range(10) if (i**2)%2==0]
print(evens)

print("new")
nums=[4,5,6]
msg="Numbers:{0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)

print("{0]{1}{0}".format("abra","cad"))

a = "{x},{y}".format(x=5,y=6)
print(a)

print(abs(42))

