# IUMS-Result-Notifier

So I am a kind of lazy coder! And my university gives our course results in a Integrated University Management System hosted on a website, but without giving any notification
or e-mail. And literally I had to do login multiple times(call it hundreds!) a day to know whether any course result has published or not(XD)!
After learning some basic web scraping, done a small colab script which enter to the site, scrap the selected portion where result always publishes, check whether any changes in it or not, 
then send it to my email if any changes were made.

## Libraries
    % Selenium, Smtplib

## How it works?
    Save the result in a txt file. Updates after each 10 minutes and check the previous txt file with the new one. If find changes, e-mail it to the receiver. 

## Installation
    
## Caution!
    % 1. If IUMS site made any changes, this code will not work. User has to modify by inspecting the site.
    % 2. Works on colab, so you've to make sure colab terminal is always running.
