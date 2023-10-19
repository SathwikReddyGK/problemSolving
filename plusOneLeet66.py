def plusOne(digits):
        modvalue = 0
        for i in range(-1,-(len(digits)+1)):
            intermediate = digits[i] + 1 + modValue
            if intermediate > 9:
                modValue = intermediate%10
                digits[i] = modValue
                modValue = floor(intermediate/10)
            else:
                modValue = 0
            if i == -(len(digits)+1) and modValue != 0:
                digits.insert(0,modValue)

        
        return digits

if __name__ == "__main__":
     digits = [1,2,3]
     print(plusOne(digits))