def calc_acc(actual_labels, predicted_labels):
    count = 0
    for i in range(0,len(actual_labels)):
        if(actual_labels[i]==predicted_labels[i]):
            count+=1
    acc = round((count*100)/len(actual_labels))
    return acc

#Initialize the Values
actual_labels = ['Dog','Dog','Cat','Cat','Cat']
predicted_labels = ['Cat','Dog','Cat','Dog','Cat']

#Execute the Function
print(calc_acc(actual_labels,predicted_labels))