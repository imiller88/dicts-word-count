import sys, collections, operator

def word_count(phrase):
    """ """
    text = open(phrase)

    word_list = []
    for line in text:
        line = line.rstrip()
        line = line.split(' ')
        word_list.extend(line)

    stripped_list = [word.lower().rstrip('\'\"-,.:;!?_').lstrip('\"_') for word in word_list]
    word_counts = collections.Counter(stripped_list)
    #for word in stripped_list:
        #word_counts[word] = word_counts.get(word, 0) + 1

    sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1))
    print sorted_word_counts  
    for word, count in sorted_word_counts:
        print word, count


word_count(sys.argv[1])