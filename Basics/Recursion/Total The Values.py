values = input("Enter the numbers you want to find the sum of: ")

def find_sum(num, sum):
    if len(num) == 0:
        return
    
    sum += int(num[0])
    print(sum)
    find_sum(num[1:], sum)
    
find_sum(values, 0)
