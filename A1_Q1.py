def replace_cube(arr, N):
    res_list = arr

    for i in range(N-1,len(res_list),N):
        res_list[i] = res_list[i]**3
    return res_list
    
#Initialize the variable
arr = [1,2,3,4,5] 
N = 2

# Execute the function
result = replace_cube(arr,N)
print(result)
