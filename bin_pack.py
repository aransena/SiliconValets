# define a function to take a dictionary sizes with sizes for objects,
# and return a list of sets of objects, where the summed size of the objects in
# each set is <= max_summed_size_per_bin. This is a bin packing problem, and uses
# a simple algorithm, the 'First Fit Decreasing' (FFD) algorithm: first sort
# the items in decreasing orders by their sizes, and then insert each item in
# the first bin in the list with sufficient remaining space. 

def first_fit_decreasing_algorithm(sizes, max_summed_size_per_bin, return_sizes=None):
    #"""partition objects into bins, where the summed size of objects in a bin is <= max_summed_size_per_bin
    #>>> first_fit_decreasing_algorithm({'seq1': 5, 'seq2': 4, 'seq3': 4, 'seq4': 3, 'seq5': 2, 'seq6': 2}, 10.0, return_sizes=True)
    #[[4, 5], [2, 3, 4], [2]]
    #"""
    # Returns [{'seq1', 'seq2'}, {'seq3', 'seq4', 'seq5'}, {'seq6'}]
    # Note that this algorithm is heuristic and does not give the optimal solution,
    # which is ({'seq2', 'seq3', 'seq5'}, {'seq1', 'seq4', 'seq6'}]
    # However, optimal bin packing is NP-hard and exact algorithms that do it are complicated.

    # define a list of sets, to store the objects to put in each bin:
    list_of_bins = []

    # sort the objects in decreasing order by their sizes:
    objects = list(sizes.keys())
    sorted_objects = sorted(objects, key=lambda x: sizes[x], reverse=True) # sort in descending order

    # insert each object in the first bin with sufficient remaining space:
    for my_object in sorted_objects:
        found_a_bin = False
        object_size = sizes[my_object]
        # check if there is a bin with space for this object 
        for index, my_bin in enumerate(list_of_bins): # 'my_bin' is a set of objects in a bin
            # get the summed size of the objects in my_bin:
            summed_sizes_in_bin = sum([sizes[x] for x in my_bin])
            # if there is room for this object in the bin, put it in this bin:
            if object_size <= (max_summed_size_per_bin - summed_sizes_in_bin):
                list_of_bins[index].add(my_object)
                found_a_bin = True
                break # jump out of the 'for index, my_bin' loop
        # if we didn't put my_object in any bin, then put it in a new bin:
        if found_a_bin == False:
            list_of_bins.append({my_object})

    # Return a list of sets:
    if return_sizes is None:
        return list_of_bins
    else: # this is just to make testing easy
        # make a list of sublists, where each sublist has the sizes of objects in a bin:
        list_of_sizes = [sorted([sizes[x] for x in sublist]) for sublist in list_of_bins]
        return list_of_sizes