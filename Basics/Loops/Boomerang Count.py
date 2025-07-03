
input_list = [1,2,1,2,5,5,5,6] 

def count(list):
    num_of_boomerangs = 0
    for i in range(len(list)):
        try:
            f_num = list[i]
            s_num = list[i+1]
            t_num = list[i+2]
        except:
            break
        if f_num == t_num and (f_num or t_num) != s_num:
            num_of_boomerangs += 1
    return num_of_boomerangs
        
        
print("There are " + str(count(input_list)) + " boomerangs in " + str(input_list))
