# web-crawler
Requirment
 1.Python
 2.Virtual Environment
 
 1.Most of the system are preintstalled Python,if not run this command in the terminal(ctrl+alt+t)
 sudo add-apt-repository ppa:jonathonf/python-3.6
 
 sudo apt-get update

 sudo apt-get install python3.6
 
 2.Install Virtual Environment
 
 sudo pip install virtualenv
 
Setup and Use Virtualenv
Once you have virtualenv installed, just fire up a shell and create your own
environment.
First create a directory for your new shiny isolated environment

  mkdir ~/virtualenvironment
  
To create a folder for your new app that includes a clean copy of Python,
simply run:
  
  virtualenv ~/virtualenvironment/my_new_app
  
To begin working with your project, you have to cd into your directory (project)
and activate the virtual environment.
  
   cd ~/virtualenvironment/my_new_app/bin
   
Lastly, activate your environment:

   source activate
   
Now install scrapy into this directory.

  pip install scrapy
  
Check that scrapy is installed properly.
   
  scrapy
  
Building a Web Site Crawler (also called a Spider)

Create a file spider.py
 
  touch spider.py
  
 Add these lines into it
     
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)
import scrapy

class spider1(scrapy.Spider):
    name = 'site_name'
    start_urls = ['url']

    def parse(self, response):
       pass
       
save it
We can now run this spider

 scrapy runspider spider1.py

Your web crawler is ready.
 
