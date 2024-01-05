from datetime import datetime
def function(sana):
    
    date_object = datetime.strptime(sana, "%d-%m-%Y")

    
    start_of_year = datetime(date_object.year, 1, 1)



    days_difference = (date_object - start_of_year).days

    return days_difference





input_date = "25-07-2024"
result = function(input_date)
print(result)
