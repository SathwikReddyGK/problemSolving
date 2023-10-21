def fizzBuzz(n):
    # User Solution 2
    return ["Fizz"*(not i%3)+"Buzz"*(not i%5) or str(i) for i in range(1,n+1)]
    # User solution
    # answer = []
    # fizz = 0
    # buzz = 0
    # for i in range(1,n+1):
    #     fizz += 1
    #     buzz += 1
    #     if fizz == 3 and buzz == 5:
    #         answer.append("FizzBuzz")
    #         fizz = 0
    #         buzz = 0
    #     elif fizz == 3:
    #         answer.append("Fizz")
    #         fizz = 0
    #     elif buzz == 5:
    #         answer.append("Buzz")
    #         buzz = 0
    #     else:
    #         answer.append(str(i))
    
    # return answer
    # Below is my solution
    # for i in range(1,n+1):
    #     if i%15 == 0:
    #         answer.append("FizzBuzz")
    #     elif i%3 == 0:
    #         answer.append("Fizz")
    #     elif i%5 == 0:
    #         answer.append("Buzz")
    #     else:
    #         answer.append(str(i))
    
    # return answer

if __name__ == "__main__":
    print(fizzBuzz(20))