def man_of_match(names, runs, wickets, bowls):
    '''
    input:
    names -> list of names of the players
    runs -> list of runs of the respective players
    wickets -> list of wickets taken by the respective players
    bowls -> list of bowls by the respective players
    
    output:
    data -> data of the players in dictionary format
    manOfMatch -> name of the man of the match
    '''
    data = {}
    manOfMatch = ""
    max1=0
    # Your code starts here
    data = {names[i]:[runs[i],wickets[i],bowls[i]]for i in range(0,len(names))}
    for i in range(0,len(names)):
        if((runs[i]/bowls[i])>4 and wickets[i]>2):
            manOfMatch = names[i]
        elif((runs[i]/bowls[i])>2 and wickets[i]>4):
            manOfMatch=names[i]

    # Your code ends here
    return data, manOfMatch

names = ["Arun","Nihal","Sanjay"]
runs = [25,50,10]
wickets = [3,5,4]
bowls = [7,12,3]
print(man_of_match(names, runs, wickets, bowls))