title: PyCon 2017

## Highlights from PyCon 2017

May 22, 2017

I just got back from my first [PyCon](https://us.pycon.org/2017). It was
fast-paced and a little overwhelming, but mostly really great.
I more or less signed up to drink from the proverbial fire hose of Python knowledge,
and PyCon certainly delivered. And I got to meet some nice (and very smart)
people doing some very cool things like building the PyCharm debugger (my hero!).

It's pretty amazing how quickly the organizers upload videos of
all of the talks (which are generally 30-40 minutes) and tutorials (3+ hours). [The whole conference is already up on YouTube](http://youtube.com/pycon2017)! I thought
I'd highlight a few of my favorites from this weekend.

#### Talks

Raymond Hettinger's talk, ["Modern Python Dictionaries: A confluence of a dozen great ideas"](https://www.youtube.com/watch?v=npw4s1QTmPg),
was probably the hottest ticket of the whole event; lots of unhappy conference-goers not
able to see this in person. This was a fun and clearly presented history
of some of the design decisions and algorithms underlying the Python dictionary,
and the various ways they've been able to improve its performance over time.
Dictionaries in 3.6 are awesome. Sound like a fun talk? It actually really is.

Andrew Baker live-deployed a Flask "Hello World" app in five different ways in
[this talk](https://www.youtube.com/watch?v=vGphzPLemZE), and gave pros and cons of each method. Impressive to watch
the app go from local to live on the cloud five times in 30 minutes.
The deployment options discussed were:
[ngrok](https://ngrok.com/), Heroku, "serverless" (e.g. AWS Lambda),
a normal VM, and Docker. [Slides here.](https://speakerdeck.com/pycon2017/andrew-t-baker-5-ways-to-deploy-your-python-web-app-in-2017)
[@mxmoss](https://twitter.com/mxmoss/status/865703669110497280)
tweeted a nice sketch:

![deployment](https://pbs.twimg.com/media/DAOY5hPUIAcMEJk.jpg)

[Matthew Rocklin's demo of Dask](https://www.youtube.com/watch?v=RA_2qdipVng)
was mind-blowing. Live demonstration of distributed computation
in numpy and Pandas, with some nice visualization of execution time
shared among many computing cores.

I loved [this talk](https://www.youtube.com/watch?v=azf6yzuJt54) on documentation
by Daniele Procida: a clear, structured explanation
of how you should document your software projects. It starts with the basic but important idea that
documentation is not one thing, but many different types of writing that have
different functions and audiences: see below. [Related blog post here](https://www.divio.com/en/blog/documentation/).

![docs](https://pbs.twimg.com/media/DASp6ypV0AIj-z0.jpg)

And so much more:

* [Flavio Juvenal](https://www.youtube.com/watch?v=4mkFfce46zE) ([slides](https://docs.google.com/presentation/d/1_yTCAiAdWlSZdVgaXlm7qjBiG-Jpi592KgnI5eRZREQ/edit?usp=sharing)) and
[Mali Akmanalp](https://www.youtube.com/watch?v=W8Rxd9OPblI) ([slides](https://speakerdeck.com/pycon2017/mali-akmanalp-library-ux-using-abstraction-towards-friendlier-apis))
gave back-to-back talks on API design and both included examples of
some of the great open source codebases we use, the use cases you should
design for, how to think about helpful levels of abstraction, etc.
* Jake Vanderplas gave a [great breakdown](https://www.youtube.com/watch?v=FytuB8nFHPQ) of the many, many visualization libraries
available in Python today, with a special overview of Altair and Vega-Lite,
a couple of great tools that we're using at UrbanSim.
* James Saryerwinnie taught me a few new testing tricks/strategies in
[his talk](https://www.youtube.com/watch?v=jmsk1QZQEvQ). Excited to try out
[hypothesis](https://github.com/HypothesisWorks/hypothesis-python) for property-based testing.
* Sofia Heisler went over how to [make sure your Pandas code is fast](https://www.youtube.com/watch?v=HN5d490_KKk).
Thankfully we're already doing all of this at UrbanSim. ([Slides here.](https://github.com/sversh/pycon2017-optimizing-pandas))
* A [helpful review](https://www.youtube.com/watch?v=7m5JA3XaZ4k)
of unicode, strings, decoding, encoding, etc. And a good reminder that
"all your code to process text should be using the `unicode` string type.
Using `bytes` for text is a bug." ([Slides here.](http://langa.pl/random/talks/unicode.pdf))

#### Keynotes

I actually didn't go to many keynotes, but I was inspired by [this one](https://www.youtube.com/watch?v=ZyjCqQEUa8o) by Jake Vanderplas
on using Python for science and how far it's helped us get, particularly
in making statistical analysis fully reproducible. Also, best jokes of PyCon.

#### What I'm excited to watch next

Some talks:

* [Readability Counts by Trey Hunner](https://youtu.be/knMg6G9_XCg)
* [Jukka Lehtosalo, David Fisher on Static Types](https://www.youtube.com/watch?v=7ZbwZgrXnwY)
* [The Dictionary Even Mightier by Brandon Rhodes](https://www.youtube.com/watch?v=66P5FMkWoVU)
* [Kelsey Hightower's Keynote](https://www.youtube.com/watch?v=u_iAXzy3xBA)

And more tutorials that I could ever catch up with, including:

* [Asynchronous Python for the Complete Beginner by Miguel Grinberg](https://www.youtube.com/watch?v=iG6fr81xHKA)
* [Python Epiphanies by Stuart Williams](https://www.youtube.com/watch?v=oQca6eDcjA8)
