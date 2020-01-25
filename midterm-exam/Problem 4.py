"""
Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence.
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #Create a list that contains all maximum contiguous sums starting from every different number of the list
    max_sum_list = []
    #Iterate through every item of the list, as all of them will be treated as starting points for the sum
    for i in range(len(L)):
        #max2 is a list of ints that contains every possible contiguous sum starting from the number in the ith position
        max2 = []
        max2.append(L[i])
        for k in range(i+2, len(L)+1):
            myval = sum([item for item in L[i:k]])
            max2.append(myval)
        max_sum_i = max(max2)
        max_sum_list.append(max_sum_i)
    return max(max_sum_list)