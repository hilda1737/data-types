# write a python function that takes in alist and removes the second and last
from itertools import count
from operator import truediv
from string import digits


def numbers():
    digits=[1,2,3,4,5,6,7]
    digits2=[1,2,3,4,5,6,7]
    digits.pop()
    del digits[-2]
    print(digits2)
    print(digits)
numbers()


def days():
    week_days=["Monday","Tuesday","friday","Monday"]
    # c= week_days.count("Monday")
    # print(c)
    countt=0
    for x in week_days:
        if x=="Monday":
            countt+=1
            print(countt)
days()

# A function named divisible by seven using range and fo loop returns a list containg numbers divisible by7
def divisible_seven():
    for x in range(100,200):
        if x%7==0:
            print(x)
divisible_seven()
 
#  a function that takes in two inputs as integer and adds the two numbers checks if the sum is greater than 10\
#     or equel to ten 
def addition():
    digit1=int(input("two numbers"))
    digit2=int(input("number 2"))
    sum=digit1+digit2
    if sum > 10:
        print("greater than")
    elif sum <10:
        print("less than 10")
    elif sum==10:
        print("equal to")
    else:
        print("none of the above")

addition()
# function that takes an urgument that has list[1,2,3,4,5] and returns true in four is present
from os import fork


def numbers(a):
    if (4 in a):
            print(True)
numbers([1,2,3,4,5])



# x="children are playing football"
# x=len(x)
# x2=x/2.lowe
# x3=x/2
# print(x2,x3) 


def words(word):

     s_reversed=word[::-1]

     if(word==s_reversed):
            
           print("yes its a palidrome")
     else:
         print("no its not")
words("woow")

def rever(r):
    result=""
    for i in r:
        result=i+result
    print(result)
rever("hilda")

# write a python program that takes in a string and returns the reversed of a strinng
def reversal(word):
    r_reverses=""
    for i in word:
        r_reverses=i+r_reverses
        print (r_reverses)
reversal("Hilda")


def reversal2(word2):
    reversal2=word2[-1::-1]
    print(reversal2)
reversal2("hilda")

s=[1,2,3]
s[:]=[5,7]
print(s)

my_list = ['p','r','o','b','l','e','m']
my_list[2:4]=[]

print(my_list)

def splited_words():
    sentence="Python is a good language"
    words=sentence.split(" ")
    words=words[-1::-1]
    # output=" ".join(words)
    new_string=splited_words(words)
    print(new_string)
splited_words()