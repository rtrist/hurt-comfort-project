import pytumblr
import datetime
import time
import csv


# d = datetime.date(2017, 1, 18)


client = pytumblr.TumblrRestClient(
    consumer_key='obrmgyoM7wivqNS8o93awu0H8DSxnk4OQBb3r0MfaXEt7IRPhI',
    consumer_secret='HDESANs5b1sjIjeyh2IMBZc5QrkiXJWfov1VxAiIOPCEhf84A7',
    oauth_token='S4yUuN3yzNReXYGoSaPz50D6pvZhewv6njwYpWttEmQ311DLnw',
    oauth_secret='8lMNg6CmY3FrfrGm51p4vsuhHcjmNrADOklYq7bkoHcWVWqBwa'
)
offset = 0

with open('tumblr_tags.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['date','tags'])

before = 0

for i in range(50000):
    response = client.tagged(tag="hurt/comfort", limit=20, before=before)
    amount_of_results = len(response)
    before = response[amount_of_results-1]['timestamp']
    print(before)
    time.sleep(5)



    with open('tumblr_tags.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    

                    for post in response:
                        date = post['date']
                        tags = post.get('tags', [])

                    
                        csv_writer.writerow([date, ', '.join(tags)])