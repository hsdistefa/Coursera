import json
import sys
import tweet_sentiment

def print_term_sent(tweet_data, sent_data):
    sent_dict, sent_scores = tweet_sentiment.get_sent_scores(
            tweet_data, sent_data)

    # get max word score to use as normalizer
    max_word_score = _max_score_value(sent_dict)

    # avoid div by 0!
    if max_word_score == 0:
        raise ValueError('Sentiment dictionary has no nonzero values')

    # create new dict with new words for words that appear in
    # tweets with scores != 0
    similar_words = {}
    for i in range(len(tweet_data)):
        json_tweet = json.loads(tweet_data[i])
        if u'text' in json_tweet and sent_scores[i] != 0:
            text = json_tweet[u'text'].encode('utf-8')
            # could improve word parsing
            for word in text.split(' '):
                # NOTE could come up with better formula
                # this one will tend to give common words a high value in the
                # direction that the overall sentiment points
                # i.e. if sentiment is generally positive, words such as 'a'
                # and 'the' will have strongly positive scores
                word_score = sent_scores[i] / max_word_score
                if word in similar_words:
                    similar_words[word] += word_score
                else:
                    similar_words[word] = word_score

    for word, value in similar_words.iteritems():
        print(word + ' ' + str(value))

def _max_score_value(sentiment_dict):
    '''Returns the maximum absolute value of a word score found given
    a sentiment dictionary
    '''
    return abs(sentiment_dict[max(sentiment_dict,
                    key=(lambda key: abs(sentiment_dict[key])))])


def lines(fp):
    print str(len(fp.readlines()))

def main():
    with open(sys.argv[1]) as sent_file, open(sys.argv[2]) as tweet_file:
        tweet_data = tweet_file.readlines()
        sent_data = sent_file.readlines()
        print_term_sent(tweet_data, sent_data)

if __name__ == '__main__':
    main()
