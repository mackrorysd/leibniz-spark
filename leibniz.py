import sys

# Returns a list of tuples, each tuple containing the bounds of a range of positive integers
def split_ranges(count, pairs):
    # Minimum span is 4, as ranges must contain an even number of odd integers. That way, each
    # subseries can start with addition, end with subtraction, and they can all be added together
    size = pairs * 4
    splits = []
    for i in range(count):
        first = (i * size) + 1
        last = first + size - 2
        pair = (first, last)
        splits.append(pair)
    return splits

# Iterates through the range (given as a tuple), converts odd numbers to fractions, and adds or
# subtracts according to the Leibniz series
def sum_split(denominator_range):
    term = denominator_range[0]
    last_term = denominator_range[1]
    sign = 1
    total = 0.0
    while term <= last_term:
        total = total + (float(sign) / term)
        sign = -sign
        term = term + 2
    return total

split_count = 16
split_size = 1000000

splits_list = split_ranges(split_count, split_size)
splits_rdd = sc.parallelize(splits_list)
intermediate_sums = splits_rdd.map(sum_split)
final_sum = intermediate_sums.sum()
pi = final_sum * 4
terms = 2 * split_size * split_count
print "Estimated value of pi with %i terms: %f" % (terms, pi)

