







#Write code to test if a number if a prime number?
#Prime is a number that can be divibe by one and itself
#for example: 1, 2 => prime number => base case
#3, 4 ,5, 6 , 7 
#set a counter to zero 
#Case of 4: start with 3, and then 4 , at every iteration: 4%3 = none zero , 4%4 = zero => have a counter increase => 
#Time complexity: O(N)
#Space complexity: O(1)
#BLocking: how to do it in O(1) time complexity!!!
def is_Prime(number):
    if number <= 0:
        return False
    elif number == 1 or number == 2:
        return True
    else:
        nums_zero = 0
        for i in range(1, number+1):
            if number % i == 0:
                nums_zero += 1
            if nums_zero > 2:
                return False
        if nums_zero == 2:
            return True
        return False

def main():
    for i in range(30):
        print(is_Prime(i))

if __name__ == "__main__":
    main()