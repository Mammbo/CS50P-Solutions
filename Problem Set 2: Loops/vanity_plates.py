
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
        nums = []
        first = s[0:1]
        if len(s) < 2 or len(s) > 6: 
             return False
        elif not s[0].isalpha() and s[1].isalpha():
            return False 
        elif s.isalpha():
            return True
        elif s.isalnum() and first.isalpha():
            if not s[-1].isalpha():
                for char in s[2:]:
                    nums.append(char)
                    if nums[0]== "0":
                        return False
                    else:
                        return True
      
              
                    
        else: 
            return False
                         
main()