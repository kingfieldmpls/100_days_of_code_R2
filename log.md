## #100daysofcode Round 2

### R2D1 | Sunday, June 16th 2019

**Today's Progress**

* Finished reading my log from the last round of 100 days of code
* Setup a 100 days of code tracker on the PyBites platform
* Installed VS Code
* Watched Corey Schaefer's VS Code video

**Thoughts**

* In some ways it seems I've come so far, and in others it seems like I knew things then that I don't remember anymore, or questions I had then are still questions I have now
* Still super motivated and excited
* Still need to focus and not try to take on machine learning, visualization, IoT and a million other directions

---

* You can see the brain dump above, but basically my focus this time is to work on web development
* Here are my main goals:
 * Complete the Talk Python training #100daysofcode course
 * Complete the Talk Python training #100daysofweb course
 * Complete Intermediate PyBites challenges
 * Code using VS Code
 * Get a Martin app to functioning status on a web platform
 * Improve Git knowledge and efficiency

**Links**

* [Corey's VS Code Vid](https://www.youtube.com/watch?v=06I63_p-2A4)

### R2D2 | Monday, June 17th 2019

**Today's Progress**

* Completed bite 47 using VS code
* Reviewing where I left off in Talk Python #100daysofcode training
 * Github api introduced some foggy concepts
  * requests-cache
  * pdb
  * Jupyter notebooks

**Thoughts**

* It took me a second to rememeber vs code concepts from last night. Practice will be good. Could rewatch Corey's video and of course reviewing the documentation would be great.
* I should just start at day 61 again because I think I missed some crucial steps
* There are 71 more intermedite bites, so I have my work cut out for me to complete all of thos alongside my other goals

**Questions**

**Links**

* [Pybites pdb article](https://pybit.es/requests-cache.html)
* [Pybites requests-cache article](https://pybit.es/pdb-debugger.html)

### R2D3 | Wednesday, June 19th 2019

**Today's Progress**

* Completed the first day of #100daysofcode Github API
* Re-famaliarized myself with Jupyter and it's shortcuts
* Setup environment variables for pipenv through a .env file
* Setup specific kernels in Jupyter
* Gained a better conception of how use pdb can help you discover the output of an API interactively

**Thoughts**

* The hours still absolutely whip by

**Questions**

* Why did Jupyter have access to my pipenv modules even when I was just in the regular python3 kernel?

**Links**

### R2D4 | Saturday, June 22nd 2019

**Today's Progress**

* Some partial updates from (unmarked) Thursday morning progress
 * Finished #10daysofcode Github videos
 * Setup bottle in pipenv (took forever to lock)
 * Started reading bottle documentation
* Prepping to make a github something in bottle
* Read an article on using __main__.py in a directory instead of if __name__ == "__main__"
* Got a good sense of working with the Github API - great examples
* Completed bite 48
* Watched days 64-66 on #100daysofcode on smtplib and sending emails
* Setting up my environment to use the Google API, which will still involve learning how to write MIME emails

**Thoughts**

* Forgot that I was going to make a twitter something in Flask at the end of the last challenege, but basically walked away from the because I realized it was going to take me a long time
* I'm going to give up on this Bottle GitHub app for now because I think it's going to lead me down the wrong path. I'm just going to read about Heroku, play with Bottle, play with the Github api, do a code challenge and call it a night
* Still having some issues with vs code like test discovery and figuring out how to use debugging instead of print statements
* I really need to figute out a quicker way to run the code via shortcut
* Man is this a clever way to return a value using True:
 * `book_icon = 'python' in prev_line.lower() and PY_BOOK or OTHER_BOOK`

**Questions**

* What's the advantage of static v. dynamic web pages?
* What are some good templates I should consider to speed up web development?
* Why does the VS Code run code button not work like just launching in the terminal
 * Because that was a code runner extension and I thin my vs code settings are by project so they weren't configured for pybites? I don't really understand where my settings live yet.
* How do I view the git commands again?

**Links**

* [Not the article I read](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/)
* [pygithub examples](https://pygithub.readthedocs.io/en/latest/examples/MainClass.html#get-current-user)

### R2D5 | Sunday, June 23rd 2019

**Today's Progress**

* Completed bite of py 49 - bs4 stuff. Each time I come back to a library I have a better understanding and an easier time working through the documentation
* Completed bite of py 51 - simple time delta stuff - less than 10 minutes start to finish\
* Completed bit of py 57 - definitely my best and deepest understanding of argparse yet. Tutorial linked below was pretty ace
* Completed bite 59 - I got stuck on this one for a sec trying to figure out dimensionality in Python lists. Ultimatetly I'm happy with my solution, but will be curious to see the suggested solution. 
* Completed bite 62 - easy to make the code run faster. Helpful to be reminded about deque and other non-list data structures

**Thoughts**

* Today was a super fun day. Just got to sit around with the kiddos and cross of bites. This is my NYT crossword. I'm going to be devestated when I complete the bites.

**Questions**

* Now I feel like flake8 isn't working again
 * I messed up some of the flake8 args

**Links**

* [Simple argparse tutorial](https://docs.python.org/3.7/howto/argparse.html#id1)
* [Full argparse docs](https://docs.python.org/3.7/library/argparse.html#module-argparse)

### R2D6 | Monday, June 24th 2019

**Today's Progress**

* Completed bite 70 - create your own iterator, pretty quick
* Completed bite 71 - use __call__ to store state. I eventually got there, but it took me a second to work out the scope of variables. Also, not that much info on the web.
* Quickly authenticated my Gmail app - that work flow from before really paid off. Now I just need to figure out how to put together a message.
* Sent an email with a donut

**Thoughts**

* I basically logic'd the syntax for iterators, but it wasn't incrementing properly, so clearly I did something wrong.
* Well, sendgrid just showed up again. Next step would be to give their service a try, because man howdy does that look way simpler to manage.
* Goals for tomorrow
 * Review some things with emaillike sending attachments, images and adding multiple recipients to email.
 * Figure out how to make more complex message bodies
 * 2 bites
 * Martin finance stuff
 * Back to #100days vids

**Questions**

**Links**

* [This D Bader article helped with iterators](https://dbader.org/blog/python-iterators)
* [sendgrid API client](https://sendgrid.com/solutions/email-api/)

### R2D7 | Wednesday, June 26th 2019

**Today's Progress**

* Completed bite 72 by just reading the itertools documentation and finding takewhile
* Beat my head against 73 this morning. I had to relearn how tuple (or list) unpacking works in function arguments - the main takeaway is that you need the star both to allow for multiple entires in the definition and to unpack the actual object when your calling the function.I also briefly forgot how multiple ifs is different than elifs - man back to basics. I also feel like I got a really solid understanding of pytz - convert everything to UTC and then go from there.
* I got bite 78 to work quickly with a for loop - which just felt wrong. It's funny, for loops feel un-Pythonic now. Ultimately I was reminded of set.intersection() which just checkings everything all at once.
* Bite 79 took me too long because I forgot some critical things, like:
 * What to do with CSV you get from Requests
 * How to decode requests content
 * How to use DictReader
 * How to parse the Requests response
 * How to work with a Counter object (it's just a dictionary /facepalm)
 * How to use the format specific mini-language
* Partly I think I'm just tired, but it is a little discouraing to forget so many basics. I sort of know how to solve everything now, but it just seems like I'm really, really slow. Maybe I need to think more about the process before writing any code and then write the code more slowly rather than just mash buttons and then test the code.
* Learned a _little_ bit more about the format specification mini-language. For he first time ever reading the documentation made sense to me. I still don't really understand the ::= stying though. 

**Thoughts**

* It would be good to learn a bit more about how template code is represented in the Python documentation, for example [] usually means optional
* Another two day thing where I did probably an hour the yesterday morning but it didn't meet my standard for proper effort, so then I just built off of that work today

**Questions**

* I tried to use the VS Code debug features when my pytz test were failing. I did not know how to inspect the steps along the way, It's going to take a little bit of concentration to figure that one out.

**Links**

### R2D8 | Thursday, June 27th 2019

**Today's Progress**

* Worked on refactoring the Martin Finance app
* Spent some time writing out stories for both the short term Google Sheet experience and the long term web app dream
* Read in some detail about Kanban v. scrum from the Atlassian help articles and setup a Trello board to try to project manage this Martin Finance app using the Kanban framework
* Read The Hitchhiker's Guide to Python section on structuring a project
 * Read more about __init__.py - I think namespaces and importing and project structure are starting to take on a little more shape in my head
* Setup a private GitHub repo for the app, but still need to do some refactoring before the initial push

**Thoughts**

* Ultimately very little code written today, but that's OK. I feel like a made some major progress on my knowledge of coding just by thinking more carefully about some frameworks and concepts that were confusing to me in the past.

**Questions**

**Links**

* [Kanban v Scrum](https://www.atlassian.com/agile/kanban/kanban-vs-scrum_)
* [Structuring a Project](https://docs.python-guide.org/writing/structure/)

### R2D9 | Friday, June 28th 2019

**Today's Progress**

* Mega Martin Finance progress
 * Started a runner script - budget.py
 * Refactored the YNAB API mish mash into ynab_api.py which uses actual functions

**Thoughts**

* Almost gave up before I started but then I just took a walk, drank some water and powered through

**Questions**

* What's the best time a place to import packages? Do I want to import anything twice?
 * I think I can mostly handle variables and db stuff from budget.py
* Is it better to pass around a db cursor or keep creating them?
* Am I using the sqlite context manager in a sensible way?
* What's my logging strategy here?

**Links**

### R2D10 | Saturday, June 29th 2019

**Today's Progress**

* Just worked on adding more structure to the Martin Finance App. I should probably get to the part where I actually make it useful


**Thoughts**

* I'm continuing to move along at an OK pace, but I think more thought and less code would still go a long way
* I went down a total rabbit hole trying to figure out how to interface with the right parser for the right report. At first I tried to abstract out just a couple of lines, which made everything much more complicated. I think I took DRY too seriously.
* App to watch REI garage availability

**Questions**

* VS Code can't handle .env files? The what?
 * Handled it by turning off the auto loading on the env in the terminal
* Why do I have two Martin budget environments?

**Links**

### R2D11 | Sunday,  June 30th 2019

**Today's Progress**

* Just cranked away on the Martin Finance App again. I think I'm probably one to two more sessions away from having it up and running at least. Then it's just a matter of running it whenever and adding features and enhancements as time and need allow.

**Thoughts**

* Better appreciation for namespaces. They run all of their code so you can access variables specific to that namespace and everything within that module understands it's own namespace.
* Once I finish this bit with the Martin Finance App - let's maybe put a timeline of post 4th of July break - it's back to pushing hard on #100DaysofCode curriculum.

**Questions**

* How to MySQL placeholders actually work to stop SQL injection attacks? What if I wrote some sort of DROP TABLE into a variable that was the placeholder variable?

**Links**

### R2D12 | Monday, July 1st 2019

**Today's Progress**

* This is feeling like another one of those days where the progress just wasn't "good enough" to count so I'm going to run it across two days for reasons of self-flagellation. Update: I'm pushing through - mnorning and night
* Holy cow, I got the Martin finance app to work without too much fuss. There are still a lot of missing pieces like automated running, tests, docstrings, logging, etc, but it's in a pretty good shape. The functions more or less seems sensible.
* Completed SendGrid tutorial - at first I was confused about where my messages were, they were in spam

**Thoughts**

**Questions**

* Where is my pipenv dependency mismatch?
* How to I prevent SendGrid and just gmail_app emails from having nasty malware banners?
 * I got SendGrid out of spam - it was there because I sent too many emails
 * I'm not really sure how to get rid of the phishing banner from gmail_app just yet


**Links**

### R2D13 | Tuesday, July 2nd 2019

**Today's Progress**

* Watched #100days of code videos for pyperclip

**Thoughts**

* I have an idea for my "challenge" portion of the days. I want to build a script where I can copy the previous logs days header and the script outputs the whole template for the next day. Then I want to explore the MacOS automator tool to create a quick action in my touch bar that will do that for me! That seems suitably awesome.
* I've been doing things in phases - pushing hard on bites of pie, the Martin finance app and now back to #100days of code. If I were to do 3 days in 1 day, I could finish the course in 11 days. Considering some of what's coming up is perfect primer for the #100daysofweb, which I expect to be more challening, that may be a tall order. I have a solid stretch of 5 days here, I think I'll see where I can get from now until then and then reassess.

**Questions**

* How do I get spellcheck into my markdown?

**Links**


### R2D14 | Wednesday, July 3rd 2019

**Today's Progress**

* Read the June VS Code update
* Finished listening to the Talk Python to Me episode on VS Code
* Listened to two Python Bytes podcasts while mowing
* Freakin' did it. Added a custom touch bar button that creates the template for my next day of 100 days of code log when I copy the title from the previous day. Freakin' amazing.
* It took me over an hour to write a simple script and then get the automator piece figure out, but by god it worked. I'm legitimately excited to keep using that button in the future, and also to not have to look up what day it is anymore

**Thoughts**

**Questions**

* Did something break in my user settings? Also, why does the gutter look different?

**Links**

* The one guy who is still working with Automator (https://macosxautomation.com/automator/services/index.html)

### R2D15 | Friday, July 5th 2019

**Today's Progress**

* Watched videos on openpyxl
* Spent some time playing around with openpyxl - it works just fine with Numbers since the format is support. I'm not really sure when this library is something I would want to use over just regular dictwriter or pandas.
 * Apparently this library has support for Pandas and Numpy, maybe I shouldn't have dismissed it so quickly
* Watched Selenium videos
* So the good news is I fixed the up arrow scrolling through commands in the interactive python shell by upgrading Python through homebrew. The bad news is that I also broke all of my virtual environments. 

**Thoughts**

* I think I wrote this as a thought before, but I need to clean out my Python installs and review my brews in general
* Top priority is old versions of Python cleaned up and reviewing symlinks and makim not spawnng multiple virtual env environments and figuring out where my virtual envs are for goodness sake.

**Questions**

* Can I save the right kind of file and will the library work with Numbers?
* Well shit. I broke some stuff in VS Code. It can't find my linters and I have multiple virtual environments.

**Links**

### R2D16 | Saturday, July 6th 2019

**Today's Progress**

* I think I mostly cleaned up my brew and python environments. There's still one pesky usr/local/opt interpreter hanging out.
* I'm going nuts trying to figure out how to load my .env file in VS Code
 * When I enter the debugger, it looks like the values are actually populating, but there it pukes on finding the server_knowledge
  * I give up for now
  * I fixed it. It was a problem where depending on where the file was run from the relative path to the db was different
  * There was also an issue where I wasn't properly catching len 0 reports with diff server knowledge
* Finished Selenium videos
* Learning about using pytest and selenium
* Got my first pytest/selenium test setup! Woot. Don't understand it all, but was able to troubleshoot without much trouble and I feel like this is a good primer for the Okken doc.

**Thoughts**

* For my day 3 activity I'm going to write a thing that scapes the Netflix site below and populates a list of what's released by day
* I need to get back to Brian Okken's book and the GoF book!

**Questions**

* Can I exclude a path from Path without negating a whole branch of the tree?

**Links**

* [Helpful Youtube vid on Selenium and Pytest](https://www.youtube.com/watch?v=cG9iymSS3II)
* [Netflix site I plan to use for day 3](https://www.whats-on-netflix.com)


### R2D17 | Sunday, July 7th 2019

**Today's Progress**

* Completed writing all of the selenium tests for the pybites sample web app. It was pretty trivial stuff, but it felt like I was moving really quickly thorugh all of the requirements.  I still don't totally understan the yield in the fixture of the class structure or the request object which is set to class scope and then gets the driver attribute assigned to it. It's nice to have seen this once and I hope Brian's book explains the rest.

**Thoughts**

**Questions**

**Links**

### R2D18 | Thursday, July 11th 2019

**Today's Progress**

* Project is to grab all of the Netflix new releases titles from this website that tracks that stuff. Problem is that the structure is totally flat
* Worked on figuring out how to select tags between two tags in Selenium. I think what I figured out is this:
 * Grab all of the h4 tags
 * Within each of those starting points check to see if there are title-name class objects nearby
 * If there are, grab them until you hit another h4 using the h4 ~ .title-name:not(h4) syntax
 * That didn't work. Get number of children and then loop through a CSS selector for each of the children
* Hooray! I've done it. The script opens the Netflix updates page, closes a pop-up using an explicit wait in the Selenium library - goes through the flat structure. They solution turned out to be super simple, just a CSS selector like this "h4, h5" and then the for loop writes the 2 dimensional array. You can see the script to run as many pages as you like and then it closes the browser. I think this is an actual useful project I'd like to expand at some point.
* Attended a PyMNtos meeting - last minute car miscommunication so I biked like crazy to The Nerdery
 * One speaker setup a rig to take pics of planes flying over his house - cool bit of Raspberry Pi. Feeds images into OpenCV to crop and mark the planes and hits the OpenSky API to find out what the aircraft is. Ultimate aim is to train a model to just recognize the underside of a plan I guess?
 * Updates on Python 3.8 - focused primarily on positional only arguments

**Thoughts**

* fn + Arrows == Home and End
* I'm really enjoying this iPython style Python interactive window. Huzzah for proper setup of VS Code
* I've been working on today since the 8th. I actually put in the time on the 8th but it didn't meet my arbitrary standards. 9th I stayed up super late working on finance stuff and last night had Coolibar HH and then watched T-Swift Prime Day concert.

**Questions**

**Links**

* netflix.py in day 73-75

### R2D19 | Friday, July 12th 2019

**Today's Progress**

* Watched the Flask videos on the Talk Python training app - actually downloaded onto my phone and watched from mi iPhone. It was really a great experience, other than sometimes it was hard to see some of the code detail on my smaller screen
* Followed along with the day 1 - 3 tasks for Flask which included setting up my environment, reading about 25% of the quick start Flask tutorial, reviewing enough Bootstrap to remind myself what I was doing and then setup a simple web app to show in a nicely formatted table which Netflix movies are released by which date.

**Thoughts**

* Having a ton of fun. I feel like my environments are predictable and VS Code is working exactly like I'd like. I'm getting better with Unix codes to create files and move around the folder hierarchy. It seems like I'll actually be able to put together some sort of Martin app during this challange.
* Start committing my 100 days repo?

**Questions**

* What happens when the Jinja python gets a bit more involved? What does this stuff look like when it gets more complicated?
* Is Bootstrap used in any major applications? What are the frameworks people put on top of Flask to style the html?
* How do you unlink a remote repo again?
 * What happens to the Git history if you remove a connection to a remote repo?


**Links**

### R2D20 | Saturday, July 13th 2019

**Today's Progress**

* Watched Talk Python Training sqlite3 videos
* Watching Plotly videos
* Reviewed Bokeh and Plotly documentation
* For some reason pip installed a pre-release version of Plotly, so I had to uninstall and then reinstall the actual release version since some of the functionality disappeared that they referencing their documentation

**Thoughts**

**Questions**

* Julian recommenads using the conext manager. I remember do that, but thought you couldn't create a cursor for some reason.
* Also not sure why he used contextlib >> contextmanager in his start up a random table script
* What all does dateutil do?
* Remind me again how to clean up virtualenvs and git repos
* Why did pipenv install a pre-release version of Plotly?

**Links**

### R2D21 | Sunday, July 14th 2019

**Today's Progress**

* Successfully plotted my weight over time with Plotly. Works great, but haven't done much in the way of customizations yet.
* Successfully styled my chart. This actually seems pretty awesome now.

**Thoughts**

* This is cool for creating 2 dimensional arrays for plotting:
```
>>> a = [(1,2),(1,3),(1,4)]
>>> b = list(zip(*a))
```

**Questions**

**Links**

### R2D22 | Monday, July 15th 2019

**Today's Progress**

* Watched Anvil videos
* Signed up for Anvil
* Got all of the basic pieces in place for my sample web app

**Thoughts**

* This is cool and I can totally see the advantage of spinning something up really quickly. That being said, I feel like with the cost($50/month) I'd rather just spin something up the "hard" way with Flask.

**Questions**

* Do I just stay the Flask course, or do I venture into Django, Pyramid, Wagtail, WebSauna or other frameworks to really get a sense of the lay of the land? I feel like maybe I just need to stay the course with doing it the piecemeal way and then expand from there.

**Links**

* Saving this link for when I want to do some fuzzy string searching later for the Netflix app, or the shoppign app https://www.datacamp.com/community/tutorials/fuzzy-string-python

### R2D23 | Tuesday, July 16th 2019

**Today's Progress**

* Pretty solid coding day:
 * Watched part of a Py Edinburgh video on using the debugger in VS Code
 * Read a Trey Hunner article on tuple unpacking/ multiple assigment
 * Read a bit of the Anvil documentation
 * Rewatched portions of the Talk Python Anvil training
 * Finished my app to the point of my own satisfaction with basically accomplished:
  * Setting up a plot to view weight over time
  * Added server calls to handle all of the data management for adding weights on future dates
  * Setup validation rules so you have to properly put in the right data
* My thoughts on Anvil:
 * It's really cool that you can just use the language you love to write a whole web app
 * It's neat that they've abstracted away pretty much all of the DevOps tasks
 * I do not enjoy this tool. They way you interact with the database seems extremely limiting unless you upgrade to the paid version which allows you to just bring your own DB
 * Using just their editor means you don't have any of your tooling in place, and you can't test the deployment
 * Even though I'm very impressed with the engineering, it just seems like a worse experience than doing it the "hard" way.
 * It's such a funny thing because I feel like the project is executed so well, but it ultimately feels a bit unnecessary to me. 

**Thoughts**

* Really excited to be moving on to the next thing
* I'm starting to form this idea of putting together something like an accomplishments goal list/trophy case:
 * **Things I've done**
  * Coursera Python Fundamentals
  * Treehouse learning paths
  * Read Python Tricks
  * 100 Days of Code
* **Things I'm doing**
 * Second 100 days of code
 * Talk Python course
 * PyBites and challenges
 * GitHub repo
 * Reading Head First into Design Patterns
 * Reading Design Patterns
 * Reading Fluent Python
* **Things I hope to do**:
 * Complete 100 days of web Talk Python course
 * Read Pragmatic Programmer
 * Read Classic CS Problems - Python
 * Complete Coursera ML course
 * Complete Google Tensorflow course
 * More GitHub
 * Contribute to open source
 * Speak at PyMNtos
 * Attend Pycon

**Questions**

**Links**

* [101 Tips For Being A Great Programmer (& Human)](https://dev.to/emmawedekind/101-tips-for-being-a-great-programmer-human-36nl)
* [Trey Hunner - Multiple Assignment and Tuple Unpacking](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)

### R2D24 | Friday, July 19th 2019

**Today's Progress**

* Watched the home inventory app videos. It helped to think through some of the problems, and also how I would have structured the database as a single table, or setup a second table to house foreign keys for validating room names instead of create new tables. Other than that, I think it's trivial to do all of the work except turning the program into a GUI or web app, which is what I don't really know how to do yet and I think my time would be better spent forging on with that learning path than putting in the busy work for a bunch of CLI stuff I already know how to do.
* Read through the entire SQLAlchemy ORM tutorial, which goes into quite a bit of technical detail.

**Thoughts**

* Another multi-day. Watched home inventory and sqlalchemy vids on Wedensday morning before work. It was a gloriuos way to start the day. I identified a couple of additional tasks I wanted to perform so I put off marking the day as done even though the time was put it. Wanted to watch Corey Schafer vid on sqlalchemy, read the documentation
* Next, try to implement Martin Finance through sqlalchemy.
* Enough with pipenv, time to try out some other solutions.

**Questions**

* Figure out context managers and SQLite3 once and for all. Julian uses contextlib to create a context manager that yields a cursor and then uses a with statement manage that context. I want to see more documentation, and I want to think about atomic transactions. Those are my take aways.
* Not sure how to build the SQLAlchemy db model when the tables are already in place

**Links**

* [Checkout some of these free Grindreel courses, possiblty good for Git](https://grindreel.academy)
* [Corey Schafer SQLalchemy vids](https://www.youtube.com/watch?v=cYWiDiIUxQc)
* [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/13/orm/tutorial.html)

### R2D25 | Saturday, July 20th 2019

**Today's Progress**

* Read about implementing SQLAlchemy on top of an existing db schema
* Converting the Martin db app to use pathlib
* Using the SQLAlchemy ORM for the Martin Budget db
* I fought a good fight, and I won. I refactored the Martin Budget to SQLAlchemy. It wasn't exactly easy, but I learned what I need to learn.

**Thoughts**

**Questions**

* What's a reasonable way to deal with column name changes in SQLAlchemy, especially when you're using the automap structure? Should I just define the classes again in the code?

**Links**

* [SQLAlchemy Automap](https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html)

### R2D26 | Monday, July 29th 2019

**Today's Progress**

* Watched #100daysofcode Gooey videos
* Listened to two Python Bytes podcasts
* Listened to one Talk Python to Me podcast
* Read up on Python packaging

**Thoughts**

* Check out other solutions for creating virtual environments. I'm done with pipenv I think.

**Questions**

* I ultimately wasn't able to get Gooey up and running because of an issue with wxPython. I'm wondering if it has something to do with pipenv. I think I might try with venv tomorrow.

**Links**

* [PyOxidizer - Rust library for packaging Python applications](https://pyoxidizer.readthedocs.io/en/latest/getting_started.html)
* [Plotly 4.0 announcement](https://medium.com/@plotlygraphs/plotly-py-4-0-is-here-offline-only-express-first-displayable-anywhere-fc444e5659ee)
* [fast.ai - Learn the basics of machine learning](https://www.fast.ai)
* [Python Packaging Overview](https://packaging.python.org/overview/)

### R2D27 | Tuesday, July 30th 2019

**Today's Progress**

* I did get Gooey running. Pretty underwhelmed. I think the documentation is really bad, and also I noticed that when you use the dark theme in MacOS it takes on that theme and the elements are really hard to tell apart. Ultimately glad I worked through it but not super inspired. Similar feeling to Anvil. I'd rather just do it the hard way.
* Read more about virtual environments (links below). In light of Kenneth Reitz handing off pipenv, my own experiences with pipenv and my impression of where the community's head it at with pipenv, it just seems like venv is a safer bet.
* Read more about packaging with PyOxidzier and pyinstaller and Poetry

**Thoughts**

**Questions**

**Links**

* [Corey Schafer Virtual Environments](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
* [Realy Python article on virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
* [PyOxidizer Documentation](https://pyoxidizer.readthedocs.io/en/latest/index.html)
* [Pyinstaller Documentation](https://www.pyinstaller.org)
* [Poetry Documentation](https://github.com/sdispater/poetry)
* [Found the neat bash profile Corey Schafer uses](https://github.com/CoreyMSchafer/dotfiles)


### R2D28 | Friday, August 2nd 2019

**Today's Progress**

* Watched "Building JSON APIs" videos
* Spent a lot of time coding at work, whatever it's rare and it totally counts
* Got started reading "Classic Computer Science Problems in Python"

**Thoughts**

* It's exciting to see the shape of creating a data driven web app come together. I think I will put the time in to implement all three days, as these skills seem essential for building a lot of my pet projects.
* Now that I started reading a book, it's gotten me very excited about reading the pytest book as well. Hard to take sensible bites once you get going.
* Few link below to check out regarding the book and type annotations

**Questions**

* I'm still very curious about many of the aspects related to packaging, and application layout. 
 * For example, when should you use __init__.py and __main__.py to setup your application? 
  * How should you think about relative v. explicit imports? 
  * How should you setup your folder hierarchy? 
  * How should you think about running the application directly v. running as modules? 
  * If I were to refactor the RC code, to make the entry points more straight forward, what would I do? 
   * Why is it necessary to write "if __package__ == None"?
* Just application structure and imports. If I could lick that, I would feel much better about life
* When should I be thinking about using enums?
* How should I think about what it put in class attributes v. methods v. the propety decorator

**Links**

* [mypy homepage](http://mypy-lang.org)
* [python typing documentation](https://docs.python.org/3/library/typing.html)
* [book's github repo](https://github.com/davecom/ClassicComputerScienceProblemsInPython)
* [PEP 484](https://www.python.org/dev/peps/pep-0484/)

### R2D30 | Sunday, August 4th 2019

**Today's Progress**

* Read Python documentation on typing
* Read PEP 483 (sorta)
* Read chapter 1 of "Classic Computer Science Problems in Python"

**Thoughts**

* I'm intrigued by the exercises at the end of the chapters. I really want to come back and complete those. I'm also worried that I'm straying quite far from my frontend web-dev designs for this 100 days challenge.
* The writing in this book is excellent. If I have a question on something and he tells me to go to the Python documentation to learn more, sure enough, his examples are written exactly like the examples in the official documentation.
* This book is hurting my brain is such a great way.

**Questions**

* How do get intellisense in VS Code once an object has been renamed or passed from another function? Is that possible?

**Links**

* [Real Python Article on Typing](https://realpython.com/python-type-checking/)
* [mypy Documentation](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

### R2D31 | Saturday, August 10th 2019

**Today's Progress**

* Started reading Brian Okken's Pytest.
* Started watching Armin Ronacher's PyBay 2016 Flask talk
* Listened to Talk Python to Me where Bob and Julian join Michael to discuss lessons learned from putting together the #100daysofweb course
* Completed building the SQLAlchemy model for days 97-99
* Learning more about altering the model once the tables are built and building relationship in SQLAlchemy
  * Basically you either want to use a migration with something like Alembic, or you just want to update the table yourself and then update your model in the code

**Thoughts**

* What to learn more about building relationships with primary and foreign keys as well as cascading updates with SQLAlchemy - https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship

**Questions**

**Links**

* [Ignore single lines for Flake8 violations](http://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html)
* [Understanding SQL indexes](https://use-the-index-luke.com/sql/anatomy/the-leaf-nodes)
* [SO Indexing Answer](https://stackoverflow.com/questions/107132/what-columns-generally-make-good-indexes)

---

## Brain Dump of Ideas

* [git basics](https://git-scm.com/book/en/v1/Getting-Started)
* Finish PyBites #100DaysofCOde
* Start and finish PyBites #100DaysofWeb
* Read Design Patterns
* Read Pragmatic Programmer
* Read Python Testing with Pytest
* Read Eloquent Javascript
* Treehouse Flask course
* Martin App
* FreeCodeCamp
* Setup Linux distro
* Bash proficiency - grep, curl
* PyBites exercises
* PyBites challenges
* vscode proficiency
* Corey Schafer vids
* Real Python articles
* Make the shell prettier
* Python.org tutorial (PSF has them too? Same ones?)
* Probably need to review CSRF if I'm going to focus on web dev
* Read more about storing access tokens
* Build a Slack app
* Build a Trello app
* Clean up various Python installs

## And next time

* Pandas
* Numpy
* TensorFlow
* Natural language processing
* OpenCV
* Right chart for the right data set
* Understanding statistics