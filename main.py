import sys
import string
result = {}
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
] 
for argument in sys.argv[1:]:
    with open(argument) as filename:
        for line in filename:
            words = line.split(' ')
            for word in words:
                # Remove punctuation
                word = "".join(c for c in word if c not in ('!','.',':',','))   
                word = word.lower()
                # if word is in stop words then don't process it
                if word not in STOP_WORDS:    
                    result[word] = result.get(word, 0) + 1
        # Print all words in result along with counter value
for key in result:
    print(key, ' | ', result[key], ' ', '*' * result[key])     
