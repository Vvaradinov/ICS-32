# Vladislav Varadinov 32979197
import mapquestinput
import mapquestoutput
def trip_locations():
    """
    User input for the number of locations
    as well as the cities or streets
    """
    number_input = int(input())
    if number_input < 2:
        print("ERROR")
        return trip_locations()
    location_list = []
    for obj in range(number_input):
        location_list.append(input())
    return location_list

def action_outputs():
    """
    User input for the number of outputs
    as well as the specific outputs the user wants
    """
    number_input = int(input())
    if number_input > 5:
        print("ERROR")
        return action_outputs()
    output_list = []
    for obj in range(number_input):
        output_list.append(input())
    return output_list



if __name__ == "__main__":
    mapquestoutput.start(mapquestinput.convert_to_python_obj
                         (mapquestinput.make_a_search(trip_locations())),
                         mapquestoutput.sorted_output(action_outputs()))
    print()
    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")

