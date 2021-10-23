from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from data import *


def get_symbol(comment):
    spilt = comment.split(" ")
    for word in spilt:
        word = word.replace("$", "")
        if word.isupper() and word in us_symbols:
            return word


def sentiment_analysis(a_comments, symbols):
    scores = {}
    score_cmnt = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    vader = SentimentIntensityAnalyzer()
    vader.lexicon.update(new_words)


def run():
    sample_comments = ["TSLA is mooning!!!",
                       "TSLA is mooning!!",
                       "TSLA is mooning!",
                       "AAPL is not mooning!!!",
                       "AAPL is not mooning!!",
                       "AAPL is not mooning!",
                       "TSLA 🚀🚀🚀",
                       "which stock should I buy?"]

    vader = SentimentIntensityAnalyzer()
    vader.lexicon.update(new_words)
    tickers, count, a_comments = {}, 0, {}
    for cm in sample_comments:
        ticker = get_symbol(cm)
        if ticker in tickers:
            tickers[ticker] += 1
            a_comments[ticker].append(cm)
            count += 1
        else:
            tickers[ticker] = 1
            a_comments[ticker] = [cm]
            count += 1
        score = vader.polarity_scores(cm)
        print(f"{cm} {str(score)} {ticker}")

    print("\n")

    score_cmnt = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    for ticker in a_comments:
        if ticker is not None:
            for cm in a_comments[ticker]:
                score = vader.polarity_scores(cm)
                for key, _ in score.items():
                    score_cmnt[key] += score[key]
                # print(f"{cm} {str(score)} {ticker}")
            count = len(a_comments[ticker])
            for res in score_cmnt:
                score_cmnt[res] = round(score_cmnt[res] / count, 3)
            print(f"{ticker}: {count} - {score_cmnt}")

    # Top mention
    print("\nSymbols, Count")
    # sort dictionary
    tickers = dict(sorted(tickers.items(), key=lambda item: item[1], reverse=True))
    for i in tickers:
        if i is not None:
            print(f"{i}: {tickers[i]}")
    print(a_comments)


if __name__ == '__main__':
    run()
