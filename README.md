# Price-Tracker

A simple price tracker that notifies when the price of a particular item drops.
This is implemented in Python using requests, beautiful soup, os and time. 
It uses a timer to automatically check for price drops in a certain interval. 
The os package lets us create a custom notification using script editor in Mac. 
Beautiful soup clears through the excess data produced by the website. 
We can also add the functionality of mail alerts using the send_mail().
Draw backs: Some websites don’t allow automated requests so as to prevent 
the servers from getting overloaded. Some sites that do allow this 
price tracker: Amazon, Flipkart, ZARA, Myntra. Works only on OSX.
