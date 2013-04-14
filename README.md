algorithms
==========

Implementation of various algorithms (just sorting for the moment, others are coming soon)

The list of algorithms implemented so far:
* bubble sort
* cocktail sort
* comb sort
* gnome sort
* odd even sort
* quicksort
* insertion sort
* selection sort

There's also the ability to visualize some of the algorithms in gif form. 

How this works is matplotlib saves the list after each iteration (done from within the sorting loop).
It creates many, many PNGs (how many pngs is determined by the runtime of the algorithm).
It uses ImageMagick to combine all the PNGs into a gif. 

I've only tested it on Linux. OSX should work, Windows probably not.
Windows can save all the images and convert them into a gif some other way.

The algorithms that work best for visualizing are the inplace algorithms, as the list is being modified in place.
Others may work, but you'll have to look a bit deeper how to do it (and they might be kind of boring to watch).

