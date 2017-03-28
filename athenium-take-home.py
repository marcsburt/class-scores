	#author: Marc Burt
	#Using python version 2.7
	# pip install numpy, pandas, collections(might be part base python package), and copy(also might be in orginal package)

import numpy as np
import pandas as pd
from collections import Counter
import copy


def atheniumGrading(scores):
	#order scores
	scores.sort(reverse = True)
	# get unique values and order set by transforming into set notation
	unique_scores = list(set(scores))
	#order unique values
	unique_scores.sort(reverse = True)

	#get duplicate elements of array
	scores_c = Counter(scores)
	unique_c = Counter(unique_scores)
	duplicates = list((scores_c - unique_c).elements())


	#create output array that will == the return of scoresWithGrades
	output_array = []
	#loop counter
	last = 0.0
	#get average in float form
	avg = len(unique_scores) / 5.0

	
	# split unique scores into semi equal lengthed arrays by average
	for i in range(5):
		output_array.append(unique_scores[int(last): int(last+avg)])
		last += avg

	#add back duplicates
	for dup in duplicates:	
		for key, value in enumerate(output_array):
			if dup in value:
				output_array[key].append(dup)
				output_array[key].sort(reverse = True)
	
	# create temp array to append output array from
	#	deep copy to not have temp_array point to same place in memory
	temp_array = copy.deepcopy(output_array)

	#normalize array based on unique values being added of there are 5 unique values
	if len(unique_scores) >= 5:
		for key in range(len(output_array)-1):
			# if the length of first array is greater than the next and the last two numbers in the first array are NOT equal and there are more than two numbers in the array, then push the last number down to the next array
			if output_array[key][len(output_array[key])-1] != output_array[key][len(output_array[key])-2] and len(output_array[key]) > len(temp_array[key+1]) and len(output_array[key]) >= 2 :
				#append last number to next array, delete orginal, then re-sort
				output_array[key+1].append(temp_array[key].pop(len(temp_array[key])-1))
				del output_array[key][len(output_array[key])-1]
				output_array[key+1].sort(reverse = True)
	#
	else:
		#clear empty arrays in list of lists to set up for appending to dataframe
		output_array = filter(None, output_array)

	#make human readable with Pandas dataframe
	letter_grades = ['A', 'B', 'C', 'D', 'F']
	#setting empty dataframe
	df = pd.DataFrame()
	#enumerate of output array to align with letter grades
	#use concat so columns takes different sized arrays
	for key, scores in enumerate(output_array):
		new_df = pd.DataFrame({letter_grades[key]: scores})
		df = pd.concat([df, new_df], axis =1)

	# add space and align rows with by reformating to string
	print ''
	scoresWithGrades = df.to_string()



	return scoresWithGrades

print(atheniumGrading([99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]))