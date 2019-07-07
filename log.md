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
* Bash proficiency
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