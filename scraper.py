import tweepy
import string
import csv

BEARER_TOKEN = "~insert bearer-token here~"
# enter bearer token above before execution

obj = tweepy.Client(bearer_token = BEARER_TOKEN, wait_on_rate_limit = True)

corr_file = { 
    "#djokovic" : "djokovic", "#novaxdjocovid" : "novaxdjocovid", "#novaxdjokovic":"novaxdjokovic",
    "#NoleFam" : "nolefam", "#WeStandWithNovak" : "westandwithnovak", 
    "#istandwithnovak":"istandwithnovak", "#djokovicout":"djokovicout", "#nolegohome":"nolegohome",
    "#BoycottAustralianOpen": "BoycottAustralianOpen", "#boycottausopen" : "boycottausopen"

}

allowed_chars = set(string.printable)

def clean_string(text):
    text = [x for x in text if x in allowed_chars]
    text = "".join(text)
    return text

DELIM = "~"


for in_hashtag, out_file in corr_file.items():
    with open (out_file + ".csv", "w", encoding = "utf-8", newline = "") as file:
        csv_writer = csv.writer(
            file, delimiter=DELIM, quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        query = in_hashtag + " lang:en -is:retweet"

        for tweet in tweepy.Paginator(
            obj.search_recent_tweets, query, max_results=100
        ).flatten(limit=1000):
            id_text = tweet.id
            text = tweet.text
            text = [x for x in text if x in allowed_chars]
            text = "".join(text)
            text = text.replace("\n", " ")
            text = text.replace(DELIM, " ")
            text = text.replace("https", " ")
            text = text.replace("\r", " ")
            #id = clean_string(tweet.id)
            timestamp = tweet.created_at
            csv_writer.writerow([id_text, text, timestamp])
            #file.write(f"{id_text}\t{text}\n")

#end


#tweets = obj.search_recent_tweets(query = "AusOpen")

#for tweet in tweets:
    #print (tweet)
    #print ("\n")

# end