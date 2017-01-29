import json
import sys

def print_term_freq(tweet_data):
    '''Returns the relative frequency of terms found in the given tweet data
    '''
    freq = {}
    for tweet in tweet_data:
        json_tweet = json.loads(tweet)
        if u'text' in json_tweet:
            text = json_tweet[u'text'].encode('utf-8')
            # could improve word parsing
            for word in text.split(' '):
                if word in freq:
                    freq[word] += 1.0
                else:
                    freq[word] = 1.0

    # print each relative frequency in ascending order
    num_words = len(freq)
    for word, value in sorted(freq.iteritems(), key=lambda x: x[1]):
        print(word + ' ' + str(value/num_words))


def main():
    with open(sys.argv[1]) as tweet_file:
        tweet_data = tweet_file.readlines()
        print_term_freq(tweet_data)


if __name__ == '__main__':
    main()
