# PolyglotVancouver

This repository holds a project conducting data analysis and visualization of the 2017 Polyglot Vancouver Un-Conference.



### Motivation

During the very first session that I attended on May 27th, 2017, one particular person immediately started driving the conversation.
Extremely opinionated, confrontational, and dismissive of alternative opinions, people immediately started to check out both mentally and physically.
I could see how much it was affecting the experience that myself and others had paid for and invested in, and I was angry.

### Strategy

But rather than confront directly, I decided to bear witness instead, which may have been the wrong decision, but it is a time honoured one.
On a hunch, I started a markdown file that tracked how many times each person spoke.
The initial results were interesting, so I maintained the strategy for the rest of the sessions that I attended that day.

### Documentation

Aside from the amount of time(s) that someone spoke, I decided to track their gender (which, as you may guess, was a seemingly large factor in how comfortable they were in deciding to speak), as well as whether they arrived on time and/or stayed until the end (which I took to assume that the micro-politics of the room were unpalatable ).

### Analysis

Conducting rudimentary data science methodologies upon the dataset, I attempt to visualize the extent of disparity in the amount of public voice that certain persons and certain demographics were granted or able to affect.

### Conclusions

First of, let me say that in no way am I trying to throw Polyglot under the bus, though I do have some concrete suggestions for them that I will be presenting alongside this data. These include:
  * training more staff / volunteers on hosting / mediation techniques
  * ensuring that there is one volunteer per session that can host / introduce / mediate as needed
  * owning their own data by making visible what demographic breakdown they see before the event
  * creation of a tracking plan - alongside robust ethical guidelines (that i admit i did not adhere to) - to execute during the event
  * reach out to other local and international groups, associations, federations, that have experience doing Un-Conferences and have been trained in horizontal facilitation
  * work with minority groups - along racial, gender, and class lines - as stakeholders in attempting to create the type of event that we all want to see

Second... what is it with some people ? Seriously, this is a case of a few offenders skewing the data so bad that they can almost be classified as outliers. I definitely found that certain types of sessions gave different experiences, and some engendered conversation better than others. And Session 04, which was a presentation, seemed like a welcome respite halfway through the day.

### Files

 * README.md --> this file
 * Polyglot Session Notes.md --> the original notes that I took during the sessions
 * polygot.ipynb --> Interactive Python (Jupyter) Notebook where I perform the primary data analysis
 * data/xxx.csv --> various comma-separated-value files that were created based off of the markdown tables in order to parse the data easier in Python
 * util.py --> Python file that includes utility functions that can be imported in all of the notebooks to allow for easy code re-use
