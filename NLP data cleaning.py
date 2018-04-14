from docx import Document
import nltk
import re


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
	for i in range(len(sentence)):
		sentence[i] = sentence[i].split(' ')
		if(len(sentence[i]) <= 3 or (sentence[i][0] == 'Like' and sentence[i][2] == 'Reply')):
			#ignore sentence left than 4 words
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
		text = str(clean_sentence[i])
		clean_sentence[i]= emoji_pattern.sub(r' ',text)	
			
	return clean_sentence		



document = Document('C:\\Users\\User\\Desktop\\UM\\Sem 6\\NLP\\NLP part1.docx')
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
print(clean_sentence)

for i in range(len(clean_sentence)):
	tokens += nltk.word_tokenize(clean_sentence[i])
text = nltk.Text(tokens)
print(text.collocations())



