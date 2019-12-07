from pyatom import AtomFeed
import datetime

feed = AtomFeed(title="Justin Abrahms",
                feed_url="http://feeds.feedburner.com/justinlilly",
                url="http://justin.abrah.ms",
                author="Justin Abrahms")

# Do this for each feed entry
feed.add(title="Why I made pisces, a testable web framework",
         content="Pisces is a Python web framework that was written with testing in mind. It was birthed as a reaction to the typical workflow in a Django project, which I've come to dislike as it encourages you to make your code tightly coupled and less testable.",
         content_type="text",
         author="Justin Abrahms",
         url="http://justin.abrah.ms/python/why_pisces.html",
         updated=datetime.datetime(2013, 7, 9, 12, 00))

print(feed.to_string())
