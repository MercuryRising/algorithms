import random
import time
import matplotlib.pylab as plt
import subprocess
import glob
import os
import sys

def bubble_sort(sequence):
    '''
    bubble sort works by looping through the input list, comparing the current value to the next value,
    if the next value is bigger, it swaps the entries, and breaks the inner loop (to loop again, until the
    list is sorted.
    '''
    ordered = False
    while not ordered:
        ordered = True
        for index, value in enumerate(sequence[:-1]):
            if value > sequence[index+1]:
                ordered = False
                sequence[index] = sequence[index+1]
                sequence[index+1] = value
                break
        if make_gifs: animate(sequence, "bubble_sort", 5)
    return sequence

def cocktail_sort(sequence):
    '''
    Cocktail sort also solves the turtle problem that in bubble sort by implementing bubble sort, then reversing the list and bubble sorting.
    '''
    ordered = False
    while not ordered:
        ordered = True
        for index, value in enumerate(sequence[:-1]):
            if value > sequence[index+1]:
                ordered = False
                sequence[index] = sequence[index+1]
                sequence[index+1] = value
                break

        for index, value in enumerate(sequence[1:][::-1]):
            if value < sequence[::-1][index+1]:
                ordered = False
                sequence[::-1][index] = sequence[::-1][index+1]
                sequence[::-1][index+1] = value
                break
    return sequence

def comb_sort(sequence):
    '''
    Comb sort improves bubble sort by allowing elements to move by more than just one step.
    '''
    gap = len(sequence)
    scale_factor = 4/3.

    ordered = False
    while not ordered:
        ordered = True
        gap = int(gap / scale_factor)
        if gap < 1:
            gap = 1
    
        for index, value in enumerate(sequence[:-gap]):
            if value > sequence[index+gap]:
                ordered = False
                sequence[index] = sequence[index+gap]
                sequence[index+gap] = value
                break
    return sequence

def bucket_sort(sequence, num_buckets=None):
    '''
    bucket sort chunks the entities of the input list into smaller 'close' lists that are later sorted and then merged to form the final sorted list.
    '''

    if not num_buckets: 
        num_buckets = len(sequence) / 15 if len(sequence) > 10 else 1

    start, stop = min(sequence), max(sequence)
    bucket_width = (stop - start ) / num_buckets

    bucket_ranges = [start+bucket_width*index for index in range(num_buckets+1)]
    buckets = dict(zip(bucket_ranges, [ [] for _ in range(len(bucket_ranges))]))

    for item in sequence:
        bucket = [y for y in bucket_ranges if y <= item][-1]
        buckets[bucket].append(item)

    sorted_list = []
    for key in bucket_ranges:
        bucket = buckets[key]
        if bucket:
            sorted_list.extend(bubble_sort(bucket))
    return sorted_list

def odd_even_sort(sequence):
    '''
    Odd even sort breaks the list into odd and even components, compares each set of values, if the first element is larger swaps them
    '''

    ordered = False
    while not ordered:
        ordered = True
        evens = sequence[::2]
        odds = sequence[1::2]
        pairs = zip(evens, odds)
        for index, p in enumerate(pairs):
            if p[0] > p[1]:
                ordered = False
                sequence[index*2] = p[1]
                sequence[index*2+1] = p[0]
        odds = sequence[1::2]
        evens = sequence[2::2]
        pairs = zip(odds, evens)
        for index, p in enumerate(pairs):
            if p[0] > p[1]:
                ordered = False
                sequence[index*2+1] = p[1]
                sequence[index*2+2] = p[0]
        if make_gifs: animate(sequence, "odd_even", 15)

    return sequence

def gnome_sort(sequence):
    '''
    gnome sort is a simple sorting algorithm that starts at index 1 and compares that value to index 0. If the previous entry is smaller, the position is incremented forwards (ordered so far).
    if the previous entry is larger, the current position and previous position are swapped, and the position is decremented, this procedure repeats until the position is equal to the length
    of the list (the list is sorted when the position is equal to the length of the list)
    '''
    position = 1
    while position < len(sequence):
        if sequence[position] > sequence[position-1]:
            position += 1
        else:
            sequence[position-1], sequence[position] = sequence[position], sequence[position-1]
            if position > 1:
                position -= 1
        if make_gifs: animate(sequence, "gnome_sort", 15)
    return sequence

def quick_sort(sequence):
    '''
    Quicksort randomly chooses a pivot value to populate a greater than or less than list.
    Recursively calls quick_sort to create smaller and smaller sorted lists, until lists of length 1 or 0 remain.
    '''
    if len(sequence) <= 1:
        return sequence

    pivot = random.choice(sequence)
    sequence.remove(pivot)
    greater = [value for value in sequence if value >= pivot]
    lesser = [value for value in sequence if value < pivot]

    sorted_list = quick_sort(lesser) + [pivot] + quick_sort(greater)

    return sorted_list

def quick_sort_partition(sequence, left, right):
    '''
    In place sorts the subsequence of sequence[left:right]

    '''
    pivot_value = random.choice(sequence[left:right])
    pivot_index = sequence.index(pivot_value)

    sequence[pivot_index], sequence[right]  = sequence[right], sequence[pivot_index]
  
    for index in range(left, right):
        if sequence[index] <= pivot_value:
            sequence[index], sequence[left] = sequence[left], sequence[index]
            left += 1

    sequence[right], sequence[left] = sequence[left], sequence[right]

    return left

def quick_sort_inplace(sequence, left=None, right=None):
    '''
    Quicksort randomly chooses a pivot value to populate a greater than or less than list.
    Recursively calls quick_sort to create smaller and smaller sorted lists, until lists of length 1 or 0 remain.
    '''
    if left < right:
        new_pivot = quick_sort_partition(sequence, left, right)
        if make_gifs: animate(sequence, "quick_sort_inplace", 5)
        quick_sort_inplace(sequence, left, new_pivot-1)
        quick_sort_inplace(sequence, new_pivot+1, right)

def quick_sort_inplace_helper(sequence):
    '''
    Helper function for inplace quick sort.
    Starts the algorithm with 0, len(seq)-1 for initial subsequence
    '''
    quick_sort_inplace(sequence, 0, len(sequence)-1)
    return sequence

def insertion_sort(sequence):
    '''
    Insertion sort creates the final sorted list element by element
    '''
    if sequence[1] > sequence[0]:
        sorted_list = sequence[:2]
    else:
        sorted_list = sequence[:2][::-1]
    for value in sequence[2:]:
        seeking = False
        insertion_index = 0
        for index, item in enumerate(sorted_list[::-1]):
            if value < item:
                seeking = True
            elif value > item and seeking == True:
                insertion_index = len(sorted_list)-index
                sorted_list.insert(insertion_index, value)
                break
        if not seeking:
              sorted_list.append(value)
        if seeking and not insertion_index:
            sorted_list.insert(0, value)
    return sorted_list


def selection_sort(sequence):
    '''
    Repeatly finds the minimum of the sequence and adds it to a new list.
    Pops the minimum from the sequence, and repeats.
    '''

    length = len(sequence)
    sorted_sequence = []
    while len(sorted_sequence) < length:
        value = min(sequence)
        sequence.remove(value)
        sorted_sequence.append(value)
    return sorted_sequence

def py_sort(sequence):
    return sequence.sort()

def py_sorted(sequence):
    return sorted(sequence)

def humanize_time(time_delta):
    if time_delta > 1:
        return "%s s" % round(time_delta, 2)
    elif time_delta > .001:
        return "%s ms" %round(time_delta*1000, 2)
    else:
        return "%s us" %round(time_delta*1000*1000, 2)

def animate(sequence, name, delay):
    if steps.has_key(name):
        step = steps[name]
        steps[name] += 1
    else:
        step = 0
        steps[name] = 0
  
    ax = plt.subplot(111)
    ax.plot(range(len(sequence)), sequence, "b.")
    ax.set_title(name.replace("_", " "))  
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    file_name = '%s_%05d.png'%(name, step)
    plt.savefig(file_name)
    plt.clf()
    print "Saved figure: %s"%file_name

def gif_it(file_name_root, delay_time=15):
    images = "%s_*"%file_name_root
    gif_name = "%s.gif" %file_name_root

    try:
        print "Creating %s" %gif_name    
        command = ["convert", "-delay", str(delay_time), images, gif_name]
        subprocess.call(command)
        if glob.glob(file_name_root+"_*"):
            removers = glob.glob(file_name_root+"_*")
            command = ["rm"] + removers
            subprocess.call(command)
    except:
        print "Is ImageMagick installed? Can you access it with 'convert' through the command line?"
        print "Images are located in %s/%s if you'd like to make the gif yourself." %(os.getcwd()+os.sep+images)

    if os.path.exists(file_name_root+".gif"):
        print "File %s created successfully." %(file_name_root+".gif")

def test_sorts(size=25, debug=False):
    functions = [bubble_sort, cocktail_sort, comb_sort, gnome_sort, odd_even_sort, insertion_sort, \
                selection_sort, quick_sort_inplace_helper, quick_sort, sorted]

    test_list = range(size)
    random.shuffle(test_list)
    sorted_test = sorted(test_list)

    for fun in functions[::-1]:
        a = time.time()
        result = fun(test_list[:])
        if debug: print result
        time_taken = time.time()-a
        check = result == sorted_test
        print "[res:%s] %s (%s)" %(check, fun.__name__, humanize_time(time_taken))

steps = {}
if __name__ == "__main__":
    list_size = 100
    make_gifs = True
    debug = False
    test = False

    if test:
        test_sorts(list_size, debug)

    test_list = range(list_size)
    random.shuffle(test_list)

    # Functions we want to make gifs of 
    if make_gifs:
        quick_sort_inplace_helper(test_list[:])
        #bubble_sort(test_list[:]) 
        odd_even_sort(test_list[:]) 

        for key in steps.keys():
            gif_it(key)


