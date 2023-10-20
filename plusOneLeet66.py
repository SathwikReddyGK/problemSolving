import math
def plusOne(digits):
        # Solution by an user
        for i in range(-1,-(len(digits)+1),-1):
               if digits[i] < 9:
                      digits[i] += 1
                      return digits
               digits[i] = 0

        digits.insert(0,1) 
        # Below is my solution
        # modValue = 0
        # for i in range(-1,-(len(digits)+1),-1):
        #     if i == -1:
        #         intermediate = digits[i] + 1 + modValue
        #     else:
        #         intermediate = digits[i] + modValue 
        #     if intermediate > 9:
        #         modValue = intermediate%10
        #         digits[i] = modValue
        #         modValue = math.floor(intermediate/10)
        #     else:
        #         digits[i] = intermediate
        #         modValue = 0
        #         break
        # if modValue != 0:
        #     digits.insert(0,modValue)

        
        return digits

if __name__ == "__main__":
     digits = [9,9,9]
     print(plusOne(digits))