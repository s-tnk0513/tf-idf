import codecs
import math as mt
import time

#文書数
FILE_NUMBER = 10



unique_word_list = [[] for i in range(FILE_NUMBER)]

#文書の単語リスト
#word_list：文書の単語リスト
#【例】word_list[0]=["りんご"、"みかん"]
word_list = [[] for i in range(FILE_NUMBER)]


#辞書式配列：file_number_in_wordについて
#Key：単語（重複なし）、Value：Keyの単語を含む文書数
#【例】{りんご：2}はりんごが出てきた文書数が2つであることを示す。
file_number_in_word = {}



def open_file(file_name):
	file_name = "input/{}".format(file_name)
	return open(file_name,'r',encoding="shift-jis")

def write_file(file_name,unique_word,tf_idf):
	file_name = "output/{}".format(file_name)
	f = open(file_name,'a',encoding="utf-8")
	output = '{}	{}\n'.format(unique_word,tf_idf)
	f.write(output)
	


def func_file_number_in_word():	
	global file_number_in_word

	for name in range(FILE_NUMBER):
		file_name = '{}.txt'.format(name)
		f = open_file(file_name)
		for word in f:
			#行末の改行コードを取り除く
			word = word.replace('\n','')
			#file_number_in_wordに単語とその単語を含む文書数をfile_number_in_wordに追加する。
			if word not in file_number_in_word:
				file_number_in_word[word] = [1,1]
			if file_number_in_word[word][1] == 0:
				file_number_in_word[word][0] = file_number_in_word[word][0] + 1
				file_number_in_word[word][1] = 1
		for word in file_number_in_word:
			file_number_in_word[word][1] = 0




def tf(unique_word,name):
	global word_list
	return word_list[name].count(unique_word)
	
def idf(unique_word):
	global FILE_NUMBER
	global file_number_in_word
	return mt.log(float(FILE_NUMBER)/float(file_number_in_word[unique_word][0]))

def calculate_tf_idf(unique_word,name):
	return tf(unique_word,name)*idf(unique_word)


def write_word_and_tf_idf():
	global word_list
	global unique_word_list
	# name:ファイル名
	#【例】0.txtの0の部分を表す。
	for name in range(FILE_NUMBER):
		file_name = '{}.txt'.format(name)
		f = open_file(file_name)
		for word in f:
			#行末の改行コードを取り除く
			word = word.replace('\n','')
			word_list[name].append(word)	
		unique_word_list[name] = list(set(word_list[name]))
		for unique_word in unique_word_list[name]:
			file_name = '{}.txt'.format(name)
			write_file(
				file_name,unique_word,
				calculate_tf_idf(unique_word,name)
				)
		



if __name__ == '__main__':
	t1 = time.time()
	func_file_number_in_word()
	write_word_and_tf_idf()
	t2 = time.time()
	print("経過時間：{}秒").format(t2-t1)
	
	
	



