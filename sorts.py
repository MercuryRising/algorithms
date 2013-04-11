import random

def bubble_sort(l):
	'''
	bubble sort works by looping through the input list, comparing the current value to the next value,
	if the next value is bigger, it swaps the entries, and breaks the inner loop (to loop again, until the
	list is sorted.
	'''
	ordered = False
	while not ordered:
		ordered = True
		for index, value in enumerate(l[:-1]):
			if value > l[index+1]:
				ordered = False
				l[index] = l[index+1]
				l[index+1] = value
				break

	return l

def cocktail_sort(l):
	'''
	Cocktail sort also solves the turtle problem that in bubble sort by implementing bubble sort, then reversing the list and bubble sorting.
	'''
	ordered = False
	while not ordered:
		ordered = True
		for index, value in enumerate(l[:-1]):
			if value > l[index+1]:
				ordered = False
				l[index] = l[index+1]
				l[index+1] = value
				break

		for index, value in enumerate(l[1:][::-1]):
			if value < l[::-1][index+1]:
				ordered = False
				l[::-1][index] = l[::-1][index+1]
				l[::-1][index+1] = value
				break

	return l

def comb_sort(l):
	'''
	Comb sort improves bubble sort by allowing elements to move by more than just one step.
	'''
	gap = len(l)
	scale_factor = 4/3.

	ordered = False
	while not ordered:
		ordered = True
		gap = int(gap / scale_factor)
		if gap < 1: gap = 1
		for index, value in enumerate(l[:-gap]):
				if value > l[index+gap]:
					ordered = False
					l[index] = l[index+gap]
					l[index+gap] = value
					break

	return l

def bucket_sort(l, num_buckets=None):
	'''
	bucket sort chunks the entities of the input list into smaller 'close' lists that are later sorted and then merged to form the final sorted list.
	'''
	if not num_buckets:	
		num_buckets = len(l) / 15 if len(l) > 10 else 1

	start, stop = min(l), max(l)
	bucket_width = (stop - start ) / num_buckets

	bucket_ranges = [start+bucket_width*index for index in range(num_buckets+1)]
	buckets = dict(zip(bucket_ranges, [ [] for _ in range(len(bucket_ranges))]))

	for item in l:
		bucket = [y for y in bucket_ranges if y <= item][-1]
		buckets[bucket].append(item)

	sorted_list = []
	for key in bucket_ranges:
		bucket = buckets[key]
		if bucket:
			sorted_list.extend(bubble_sort(bucket))

	return sorted_list

def odd_even_sort(l):
	'''
	Odd even sort breaks the list into odd and even components, compares each set of values, if the first element is larger swaps them
	'''

	ordered = False
	while not ordered:
		ordered = True

		evens = l[::2]
		odds = l[1::2]
		pairs = zip(evens, odds)
		for index, p in enumerate(pairs):
			if p[0] > p[1]:
				ordered = False
				l[index*2] = p[1]
				l[index*2+1] = p[0]

		odds = l[1::2]
		evens = l[2::2]
		pairs = zip(odds, evens)
		for index, p in enumerate(pairs):
			if p[0] > p[1]:
				ordered = False
				l[index*2+1] = p[1]
				l[index*2+2] = p[0]
				
	return l

def gnome_sort(l):
	'''
	gnome sort is a simple sorting algorithm that starts at index 1 and compares that value to index 0. If the previous entry is smaller, the position is incremented forwards (ordered so far).
	if the previous entry is larger, the current position and previous position are swapped, and the position is decremented, this procedure repeats until the position is equal to the length
	of the list (the list is sorted when the position is equal to the length of the list)
	'''
	position = 1
	while position < len(l):
		if l[position] > l[position-1]:
			position += 1
		else:
			l[position-1], l[position] = l[position], l[position-1]
			if position > 1:
				position -= 1

	return l

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

def insertion_sort(l):
	'''
	Insertion sort creates the final sorted list element by element
	'''

	if l[1] > l[0]:
		sorted_list = l[:2]
	else:
		sorted_list = l[:2][::-1]
	for value in l[2:]:
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

def merge_sort(l):
	'''
	Breaks lists apart into 2s, successively builds up larger lists by merging them.
	'''
	if len(l) <= 1:
		return l

	pairs = zip(l[::2], l[1::2])
	sorted_pairs = []
	for pair in pairs:
		if pair[0] < pair[1]:
			sorted_pairs.append(pair)
		else:
			sorted_pairs.append(pair[::-1])
	sorted_pairs = merge_sort(sorted_pairs)
	return sorted_pairs

def selection_sort(sequence):
	length = len(sequence)
	sorted_sequence = []
	while len(sorted_sequence) < length:
		value = min(sequence)
		sequence.remove(value)
		sorted_sequence.append(value)
	return sorted_sequence

def py_sort(l):
	return l.sort()

def py_sorted(l):
	return sorted(l)

if __name__ == "__main__":

	test_list = range(20)
	test_list = list(test_list)
	random.shuffle(test_list)
	print(selection_sort(test_list))