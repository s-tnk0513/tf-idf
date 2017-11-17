# coding : utf-8
import codecs
import math as mt
import time

#ファイル数
FILE_NUMBER = 10

#{単語：その単語を含む文書数}
file_number_in_word = {}

#{あるファイルAの単語:そのファイルAの中の単語数}
#ただしA=0.txt,1,txt,・・・・,9,txtのいづれか
unique_word_list = {}

def count_file_number_in_word():	
	global file_number_in_word

	for name in range(FILE_NUMBER):
		file_name = '{}.txt'.format(name)
		f = open_file(file_name)
		for unique_word in f:
			unique_word = unique_word.replace('\n','')
			if unique_word not in file_number_in_word:
				file_number_in_word[unique_word] = [1,1]
			if file_number_in_word[unique_word][1] == 0:
				file_number_in_word[unique_word][0] = file_number_in_word[unique_word][0] + 1
				file_number_in_word[unique_word][1] = 1
		for word in file_number_in_word:
			file_number_in_word[word][1] = 0

def count_word_number_in_file(f):
	for unique_word in f:
			unique_word = unique_word.replace('\n','')
			if unique_word not in unique_word_list:
				unique_word_list[unique_word] = 1
			else:
				unique_word_list[unique_word] = unique_word_list[unique_word] + 1


def calculate_tf_idf(unique_word):
	return tf(unique_word)*idf(unique_word)


def tf(unique_word):
	global unique_word_list
	return unique_word_list[unique_word]
	
def idf(unique_word):
	global FILE_NUMBER
	global file_number_in_word
	return mt.log(FILE_NUMBER/file_number_in_word[unique_word][0])


def open_file(file_name):
	file_name = "input/{}".format(file_name)
	return open(file_name,'r',encoding="shift-jis")

def write_file(file_name,unique_word,tf_idf):
	file_name = "output/{}".format(file_name)
	f = open(file_name,'a',encoding="utf-8")
	output = '{}	{}\n'.format(unique_word,tf_idf)
	f.write(output)

def run():
	global unique_word_list

	count_file_number_in_word()

	for name in range(FILE_NUMBER):
		file_name = '{}.txt'.format(name)
		f = open_file(file_name)
		count_word_number_in_file(f)
		for unique_word in unique_word_list:
			write_file(
				file_name,unique_word,
				calculate_tf_idf(unique_word)
				)
		unique_word_list.clear()
	
if __name__ == '__main__':
	t1 = time.time()
	run()
	t2 = time.time()
	elapsed_time = "ElaspedTime　：　{}".format(t2 - t1)
	print(elapsed_time)