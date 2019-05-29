
from telegram.ext import Updater, MessageHandler, Filters

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


def Vader_score(tweets):
    vadersenti = analyser.polarity_scores(tweets)
    sentiment = []
    index = ["pos", "neg", "neu", "compound"]

    for i in index:
        sentiment.append(vadersenti[i])
    return sentiment[3]

def send_the_result(bot, update):

    keyword = update.message.text
    final_score = Vader_score(keyword)

    if final_score >= 0.5:
        status = 'positive'
    elif final_score > -0.5:
        status = "neutral"
    else:
        status = "negative"


    bot.send_message(chat_id=update.message.chat_id,
                     text='Average score for '
                           + str(keyword)
                           + ' is '
                           + str(final_score)
                           + ' | ' + status)
def main():
    updater = Updater('817129166:AAFYY9gn6hq2a02VOltCjnUrXXS34ONm2G8')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, send_the_result))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
