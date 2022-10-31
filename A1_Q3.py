def flatten(arr):
    res_arr = []

    def nest(a):
        for i in range(0,len(a)):
            if(type(a[i])==list):
                nest(a[i])
            else:
                res_arr.append(a[i])

    nest(arr)
    res_arr.sort()
    return res_arr

#Initialize the values
arr = [10,[40,20],30,50]

#Execute the function
print(flatten(arr))