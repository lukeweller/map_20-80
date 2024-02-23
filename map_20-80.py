#!/usr/bin/env python3
from statistics import stdev
from numpy import interp

def convert_percent_str_to_fraction(percent_str):

	return round((float(percent_str[:-1]) / 100), 3)

if __name__ == '__main__':

	test_arr = ['24.1%', '12.1%', '15.6%', '22.1%', '22.3%', '21.4%', '31.0%', '19.3%', '21%']
	test_arr_fractions = [convert_percent_str_to_fraction(_) for _ in test_arr]

	sample_std_dev = stdev(test_arr_fractions)
	sample_mean = sum(test_arr_fractions) / len(test_arr_fractions)

	# boolean that accounts for whether > mean is better than average or worse than average
	# e.g., a batter with a K% > mean is worse than average, but a batter with a BB% > mean is better than average
	bigger_is_better = False

	for _ in test_arr_fractions:
		print(interp((sample_mean - _) / sample_std_dev, [-3, 3], [20,80]))