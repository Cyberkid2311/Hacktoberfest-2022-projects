def new_menu(item_list):
    Menu = [['Sweet_Corn_Soup', 300.0], 
            ['Cream_of_Tomato_Soup', 100.0], 
            ['Bacon_and_Cheese', 150.0], 
            ['Honey_Mustard', 230.0], 
            ['Hot_Coffee', 50.0], 
            ['Cold_Coffee', 50.0], 
            ['Egg_Sandwiches', 130.0], 
            ['Tacos', 400.0]]
            
    for i in range(0,len(Menu)):
        if(Menu[i][0] in item_list):
            Menu[i][1] = (Menu[i][1]*11)/10
    
    return Menu

#Initialize the values
item_list = ["Hot_Coffee","Cold_Coffee","Tacos"]

#Execute the Function
print(new_menu(item_list))