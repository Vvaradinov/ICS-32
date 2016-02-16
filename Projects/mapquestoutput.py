# Vladislav Varadinov 32979197
import mapquestinput




class elevation:
    """
    Elevation class that returns the elevation
    for every city individually instead
    of return the elevation of the whole route
    """
    def output(self, json_output):
        print()
        print("ELEVATION")
        lat_long_list = lat_long(json_output)
        for obj in range(0,len(lat_long_list),2):
            lat_long_single = str(lat_long_list[obj]) + "," + str(lat_long_list[obj + 1])
            json_file = mapquestinput.convert_to_python_obj(mapquestinput.get_elevation(lat_long_single))
            for obj1 in json_file["elevationProfile"]:
                print((round(obj1["height"])))


class total_distance:
    """
    Total Distance class
    returns the total distance of the route
    """
    def output(self, json_output):
        print("TOTAL DISTANCE:",round(json_output["route"]["distance"]),"miles")


class narrative_directions:
    """
    Narrative Directions class
    returns the step by step directions
    to the destination (GPS format)
    """
    def output(self, json_output):
        print("DIRECTIONS")
        for obj in json_output["route"]["legs"]:
            for item in (obj["maneuvers"]):
                print(item['narrative'])
        print()


class total_time:
    """
    Total Time class
    returns the estameted time
    of the route
    """
    def output(self, json_output):
        data = json_output["route"]["time"] / 60
        print("TOTAL TIME:",round(data), "minutes")
        print()

class lat_and_long:
    """
    Lat and Lng class
    returns the formatted Lat and Lng
    with the compass directions
    """
    def output(self, json_output):
        data = json_output["route"]["locations"]
        print("LATLONGS")
        for obj in data:
            lat = (obj["displayLatLng"]["lat"])
            lng = ((obj["displayLatLng"]["lng"]))
            if lat > 0:
                direction_lat= "N"
            else:
                direction_lat = "S"
            if lng > 0:
                direction_lng = "E"
            else:
                direction_lng = "W"
            print('{0:.2f}'.format(abs(lat)) + direction_lat + " " + '{0:.2f}'.format(abs(lng)) + direction_lng)
        print()


def lat_long(json_output: dict)-> list:
    """
    Takes a json converted object
    and returns a list with the lat and lng
    """
    data = json_output["route"]["locations"]
    lat_long_list = []
    for obj in data:
        lat_long_list.append(obj["displayLatLng"]["lat"])
        lat_long_list.append((obj["displayLatLng"]["lng"]))
    return lat_long_list

def sorted_output(input_list: list)-> list:
    """
    Takes the list of the user inputs
    and sorts the outputs depending on
    the order the user inputs them
    """
    sorted_list = []
    for obj in input_list:
        if obj == "LATLONG":
            sorted_list.append(lat_and_long())
        elif obj == "STEPS":
            sorted_list.append(narrative_directions())
        elif obj == "TOTALTIME":
            sorted_list.append(total_time())
        elif obj == "TOTALDISTANCE":
            sorted_list.append(total_distance())
        elif obj == "ELEVATION":
            sorted_list.append(elevation())
    return sorted_list

def start(json_obj: dict, input_list: list):
    """
    takes the json dictionary and
    the sorted list and using duck typing
    initiated the classes to the program
    """
    for obj in input_list:
        data = obj.output(json_obj)
    return json_obj







