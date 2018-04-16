from docx import Document
import nltk
import re
import json
#method to find entity group but not accurate
def extract_entities(clean_sentence):
	for i in range(len(clean_sentence)):
		print('---------------------------------------')
		text = str(clean_sentence[i])
		print(text)
		for sent in nltk.sent_tokenize(text):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				# print(nltk.word_tokenize(sent))
				# print(nltk.pos_tag(nltk.word_tokenize(sent)))
				# print(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))))#chunk return nested nltk.tree.Tree object so you have to traverse the Tree object to get NEs
				if hasattr(chunk, 'label'):
					print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))

def remove_like_reply(sentence):
	clean_sentence = []
	pattern1 = '^Repl'
	for i in range(len(sentence)):
		sentence[i] = sentence[i].split(' ')
		if(len(sentence[i]) <= 3 or (sentence[i][0] == 'Like' and sentence[i][2] == 'Reply')):
			#ignore sentence left than 4 words
			pass
		elif((re.match(pattern1,sentence[i][1]) != None)==True):
			pass
		else:
			clean_sentence.append(sentence[i])
		
	return clean_sentence

def remove_emoji(clean_sentence):
	emoji_pattern = re.compile("["
		u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
	for i in range(len(clean_sentence)):
		# print()
		# text = str(clean_sentence[i])
		for j in range(len(clean_sentence[i])):
			clean_sentence[i][j]= emoji_pattern.sub(r' ',clean_sentence[i][j])	
			
	return clean_sentence		



document = Document('.\\NLP part1.docx')
sentence = []
tokens = []
clean_sentence = []
for para in document.paragraphs:
	#para.text.replaceAll("\n","\s")
	sentence.append(para.text)
	# print(tokens)
clean_sentence = remove_like_reply(sentence)
# extract_entities(clean_sentence)
clean_sentence = remove_emoji(clean_sentence)
deto_clean_sentence = []
for i in range(len(clean_sentence)):
	deto_clean_sentence.append(' '.join(clean_sentence[i]))
	deto_clean_sentence.append('')

new_document = Document()
# write clean sentence to word doc
new_document.add_paragraph(deto_clean_sentence)
new_document.save('nlp cleaned part1.docx')
# for i in range(len(clean_sentence)):
# 	tokens += nltk.word_tokenize(clean_sentence[i])
# text = nltk.Text(tokens)
# print(text.collocations())



