from nltk.corpus import stopwords,state_union
from nltk.tokenize import word_tokenize, sent_tokenize,PunktSentenceTokenizer
from nltk.stem import PorterStemmer,WordNetLemmatizer

#################### For downloading all the NLTK packages ################################
import nltk
#nltk.download()
###########################################################################################

str = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."

########################### Word Tokenize and Sentence Tokenize ###########################
print(word_tokenize(str))
print(sent_tokenize(str))

############################## Stop Words in NLTK ##########################################
stop_words = set(stopwords.words('english'))
print(stop_words)
############################################################################################
############### Filter Stop words from sentense and tokenize that ##########################
word = word_tokenize(str)
filter_word = []

for w in word:
    if w not in stop_words:
        filter_word.append(w)

print(filter_word)
################################ One Liner #################################################

filter_word = [w for w in word if not w in stop_words]
print(filter_word)
############################################################################################
###### Stemiing Porter Stemmer #############################################################
## fibding the root word of any word
words1 = ["game", "gaming", "gamed", "games"]
ps = PorterStemmer()

for word1 in words1:
    print(ps.stem(word1))

for w in word:
    print(ps.stem(w))
############################################################################################
####### Speach tagging : PunktSentenceTokenizer#############################################
##Given a sentence or paragraph, it can label words such as verbs, nouns and so on.
document = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'
sentences = nltk.sent_tokenize(document)
for sent in sentences:
    wd = nltk.word_tokenize(sent)
    print(nltk.pos_tag(wd))
############################################################################################
###################### Chunking : Modifiers ################################################
###################### Chinking ############################################################
###################### Lemetizer ###########################################################
lemetizer = WordNetLemmatizer()
print(lemetizer.lemmatize("cats"))
############################################################################################
######################### NLTK CORPORA #####################################################