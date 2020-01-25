###########################
# 6.00.2x problemset1: Space Cows

from problemset1 import ps1_partition as pt
import time

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
    import operator
    elements = sorted(cows.items(), key=operator.itemgetter(1))
    elements.reverse()
    reslis = []
    elements_base = elements.copy()
    while elements_base:
        elements = elements_base.copy()
        trip = []
        weight = 0
        for cow in elements:
            if cow[1] <= (limit - weight):
                trip.append(cow[0])
                weight += cow[1]
                elements_base.remove(cow)
        reslis.append(trip)
    return reslis


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
    import operator
    elements = sorted(cows.items(), key=operator.itemgetter(1))
    elements.reverse()
    pot_ret = []
    for partition in pt.get_partitions(elements):
        flag = True
        newval = partition
        for trip in partition:
            weight = sum([cow[1] for cow in trip])
            if weight > limit:
                flag = False
                break
        if flag:
            retval = []
            for el in newval:
                lista = [tup[0] for tup in el]
                retval.append(lista)
            pot_ret.append(retval)
    min_len = min([len(ret) for ret in pot_ret])
    return [ret for ret in pot_ret if len(ret) == min_len][0]


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
    print(f"Time it takes for the method to run: {greedy_time}")
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


