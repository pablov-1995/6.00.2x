###########################
# 6.00.2x problemset1: Space Cows

from problemset1 import ps1_partition as pt
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # Turn dictionary into ordered list of tuples
    elements = sorted(cows.items(), key=operator.itemgetter(1))
    elements.reverse()

    # Filter out those cows that are too heavy to fly in the spaceship
    elements = [element for element in elements if element[1] <= limit]

    # Define trip function
    def trip(cows, available_capacity):
        """
        Return a list containing the name of the cows that will do the next trip in the spaceship.
        :param cows: list of tuples, each tuple representing a cow that still has to do the trip, whose name (string)
        is the first parameter of the tuple and whose weight (int) is the second.
        :param available_capacity: int, maximum weight that the spaceship can carry
        :return: trip: list of strings, names of the cows that will go in the spaceship
        """
        travellers = []
        for cow in cows:
            heaviest_cow_name = cow[0]
            heaviest_cow_weight = cow[1]
            if not available_capacity:
                break
            elif heaviest_cow_weight <= available_capacity:
                travellers.append(heaviest_cow_name)
                available_capacity -= heaviest_cow_weight

        return travellers

    # Initialise the variable trips, which will contain every trip done by the spaceship and the cows contained in it
    trips = []

    # Keep calculating new trips until the remaining cows equal zero
    while elements:
        next_trip = trip(elements, limit)
        trips.append(next_trip)
        elements = [cow for cow in elements if cow[0] not in next_trip]

    return trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Turn dictionary into ordered list of tuples
    elements = sorted(cows.items(), key=operator.itemgetter(1))
    elements.reverse()

    # Define check_trips function
    def check_trips(partition):
        """
        Check if any trip in the partition is impossible to do due to the total weight of all the cows
        exceeding the weight limit of the spaceship.
        :param partition: list of lists, combination of trips that is being checked
        :return: True if all the trips are doable; False if not.
        """
        valid_trip = lambda x: sum([cow[1] for cow in x]) <= limit
        return all([valid_trip(trip) for trip in partition])

    # Define partitions, a generator that will yield every possible combination of trips
    partitions = pt.get_partitions(elements)

    # Filter out those combination that do not pass the check, and sort the remaining ones by length in ascending order
    valid_partitions = [partition for partition in partitions if check_trips(partition)]
    valid_partitions.sort(key=len)

    # Return the first combination of the list (it could as well be any other with the same length)
    return_partition = valid_partitions[0]
    cows_names = [[cow[0] for cow in trip] for trip in return_partition]

    return cows_names


# Problem 3
def compare_cow_transport_algorithms(cows):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start_time = time.time()
    greedy_cow_transport(cows)
    greedy_time = time.time() - start_time
    print(f"Number of trips using greedy algorithm: {len(greedy_cow_transport(cows))}")
    print(f"Time it takes for the greedy method to run: {greedy_time}\n")
    start_time = time.time()
    brute_force_cow_transport(cows)
    brute_time = time.time() - start_time
    print(f"Number of trips using brute force algorithm: {len(brute_force_cow_transport(cows))}")
    print(f"Time it takes for the method to run: {brute_time}")

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms(cows)


