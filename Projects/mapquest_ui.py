# Vladislav Varadinov 32979197
import mapquestinput
def trip_locations():
    """
    """
    number_input = int(input())
    if number_input < 2:
        print("ERROR")
        return trip_locations()
    location_list = []
    for obj in range(number_input):
        location_list.append(input())
        print(location_list)
    return location_list





def num_of_outputs()-> int:
    """
    Specify how many outputs the user wants to generate from the API
    """
    user_input = int(input())
    if user_input < 1:
        print("Error")
        return num_of_outputs()
    else:
        return int(user_input)

if __name__ == "__main__":
   print(mapquestinput.make_a_search(trip_locations()))
