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

#print("{0]{1}{0}".format("abra","cad"))

a = "{x},{y}".format(x=5,y=6)
print(a)

print(abs(-99))
print(abs(42))

a=min([sum([11,22]),max(abs(-30),2)])
print(a)

nums=[55,44,33,22,11]
if all([i>5 for i in nums]):
    print("larger")
if any([i%2==0 for i in nums]):
    print("even")

nums=[-1,2,-3,4,-5]
if all([abs(i)<3 for i in nums]):
    print(1)
else:
    print(2)

text = input().split()
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text[text_index])

print("new")
def apply_twice(func,arg):
    return func(func(arg))
def add_five(x):
    return x+5
print(apply_twice(add_five,10))

print("new")
def my_func(f, arg):
    return f(arg)
print(my_func(lambda x: 2*x*x, 5))

print("new")
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

double=lambda x:x*2
print(double(7))

nums=[11,22,33,44,55]
result=list(map(lambda x:x+5,nums))
print(result)

nums=[11,22,33,44,55]
res=list(filter(lambda x:x%2==0,nums))
print(res)

print("gen")
def countdown():
    i=5
    while i>0:
        yield i
        i-=1
for i in countdown():
    print(i)

print("yield")

def numbers(X):
    for i in range(X):
        if i %2 ==0 :
            yield i
print(list(numbers(11)))

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

print("decor")
def decor(func):
    def wrap():
        print("+======")
        func()
        print("========")
    return wrap
def print_text():
    print("hello world")
decorated=decor(print_text)
decorated()

print("decorator")
def print_text():
    print("HEllo world!")
print_text=decor(print_text)
@decor
def print_text():
    print("h")



