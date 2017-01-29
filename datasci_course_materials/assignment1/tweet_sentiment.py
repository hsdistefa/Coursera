import json
import sys


def get_sent_scores(data, sent_scores):
    # construct dictionary of sentiment pairs
    sent_dict = {}
    for sent_pair in sent_scores:
        phrase, score = sent_pair.split('\t')
        sent_dict[phrase] = float(score)

    tweet_sent_scores = []
    for line in data:
        json_tweet = json.loads(line)
        if u'text' in json_tweet:
            text = json_tweet[u'text'].encode('utf-8')
            tweet_sent_scores.append(
                get_sent_of_text(text, sent_dict))
        else: # has no text
            tweet_sent_scores.append(0)
    return sent_dict, tweet_sent_scores


def get_sent_of_text(text, sent_dict):
    phrases = _get_phrase_list(text)

    tot_score = 0
    for phrase in phrases:
        if phrase in sent_dict:
            tot_score += sent_dict[phrase]

    return tot_score


def _get_phrase_list(text):
    # NOTE assumes semantic score list has phrases with max length 2
    # construct phrase list of that max length
    words = text.split(' ')
    # could improve word parsing
    phrases = []
    phrases.append(words[0])
    for i in range(len(words)-1):
        phrases.extend((words[i] + ' ' + words[i+1], words[i+1]))
    return phrases


def main():
    with open(sys.argv[1]) as sent_file, open(sys.argv[2]) as tweet_file:
        tweet_data = tweet_file.readlines()
        sent_data = sent_file.readlines()
        for _, sent_score in get_sent_scores(tweet_data, sent_data):
            print(sent_score)


if __name__ == '__main__':
    main()
