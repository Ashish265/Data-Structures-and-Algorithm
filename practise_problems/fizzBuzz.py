def fizzBuzz(A):
    
    
    if A > 0:
        res = []


        for ele in range(1,A+1):

            if ele%3 ==0 and ele%5==0:
                res.append("FizzBuzz")
            elif ele%3==0:
                res.append("Fizz")
            elif ele%5==0:
                res.append("Buzz")
            else:
                res.append(ele)

    return res

print(fizzBuzz(3))