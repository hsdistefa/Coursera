import json
import reverse_geocoder
import sys
import tweet_sentiment



def print_state_sentiment(tweet_data, sent_data):
    sent_dict, sent_scores = tweet_sentiment.get_sent_scores(
            tweet_data, sent_data)

    state_sentiment = {}
    for i in range(len(tweet_data)):
        json_tweet = json.loads(tweet_data[i])
        if u'text' in json_tweet and \
           sent_scores[i] != 0 and \
           json_tweet[u'coordinates'] != None:
               text = json_tweet[u'text'].encode('utf-8')
               lat, lon = json_tweet[u'coordinates'][u'coordinates']
               geo = reverse_geocoder.search((lat, lon))[0]
               if geo['cc'] == 'US':
                   # admin1 is the state
                   state = geo['admin1']
                   sent = tweet_sentiment.get_sent_of_text(text, sent_dict)
                   if state in state_sentiment:
                       state_sentiment[state] += sent
                   else:
                       state_sentiment[state] = sent

    print max(state_sentiment, key=(lambda key: state_sentiment[key]))


def main():
    with open(sys.argv[1]) as sent_file, open(sys.argv[2]) as tweet_file:
        tweet_data = tweet_file.readlines()
        sent_data = sent_file.readlines()
        print_state_sentiment(tweet_data, sent_data)

if __name__ == '__main__':
    main()
