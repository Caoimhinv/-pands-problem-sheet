# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)
# I suggest that you look at the newton method at estimating square roots

# Newton's method involves a guess which I don't think was in the remit of this task
# so I'm going with a random number and lots of reiterations of the calculation.
import random

def sqrt():
    L=[]
    global number # gives me access to the number outside of the function
    number = float(input("Enter a postive number: "))
    A = random.uniform(1, number) # generates a random positve number lower than the inputted number
    while len(L) < 100: # reiterate the calculation - this could be increased for huge numbers?
        A = 0.5 * ((number / A) + A) # Newton's calculation
        L.append(A) # adds each new number to the list L. 
    return L

result = sqrt() #calling the function
roundedResult = round(result[99], 1) # accessing the last item in the list which should be
                                    # the most accurate. And then rounding to 1 decimal place.
print("The square root of ", number, "is approximately ", roundedResult)