import sys
import json


def print_top_n_hashtags(tweet_data, n):
    '''Prints the top n most frequent hashtags in the given tweet data
    '''
    if n >= len(tweet_data):
        raise ValueError('amount to print must be smaller than size of data')

    hash_freq = {}
    for tweet in tweet_data:
        json_tweet = json.loads(tweet)
        if u'entities' in json_tweet and \
                len(json_tweet['entities']['hashtags']) != 0:
            hashtags = json_tweet['entities']['hashtags']
            for hashtag in hashtags:
                text = hashtag['text']
                if text in hash_freq:
                    hash_freq[text] += 1
                else:
                    hash_freq[text] = 1

    # print the top n hashtags by frequency in descending order
    for pair in sorted(hash_freq.iteritems(), key=lambda x: x[1],
            reverse=True)[:n]:
        print(pair[0] + ' ' + str(pair[1]))


def main():
    TOP_N = 10

    with open(sys.argv[1]) as tweet_file:
        tweet_data = tweet_file.readlines()
        print_top_n_hashtags(tweet_data, TOP_N)

if __name__ == '__main__':
    main()
