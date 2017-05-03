---
title: Upcoming 
date: 2017-04-30
post-id: upcoming 
---

In my previous post, I mentioned work that I'd be doing on the website. However
I failed to pinpoint exactly what I'd be up to immediately, so I'm here to
remedy that.

The Website
-----------

### Tags on Top of the Priority List

The next thing I want to implement on the site is post tagging. This will allow
me to categorize my posts so that they are easier to find and read. This ground
work will allow for other cool features I am wanting to implement (we'll get
to those soon). However, this brings up the question of how to implement post
ids for my disqus integration.

Currently, each post has a hand crafted id. There are several problems that will
arise from this if I implement post tags. Firstly, and the biggest issue, is
keeping post ids from colliding. A side effect of post tagging I'd like to have
is having equivalent post names but with different tags. With the current system
of post identifying, this would result in post id collision in disqus.

The other problem is, keeping track of post ids by hand. It will be become quite
arduous at some point to maintain the ids by hand.

Gladly, solving these issues can probably be done with one stone. Namely, I can
have the haskell post compiler generate a post id that is a combination of the
post's name and tag. This would be a very clean solution, but I am hesitant to
enable it for embedded categorization. If I find the need to tag tagged posts,
I will consider this in the future. So far, I have no need for it yet.

Let's talk about those other features!

### Next/Previous Post Buttons

This one is a no brainer; who doesn't want next or previous buttons for
sequential post reading! The problem is finding a way to sort posts, especially
when they are categorized. I don't want to goof off on this feature in case I do
implement embedded tags, I can already tell it'll be a pain to rework this
feature.

### Category Based Searching

Searching for posts with tags should help readers to better pinpoint posts. The
only problem is, the website is static. We can't post request for a search so
I'll have to get creative with my javascript-fu. What comes to mind is
generating pages for specific tags, and including all the posts associated. Then
we can have a search bar with a javascript frontend that will scrape away
non-matching posts from the page. These will be kept in a vector, so they can be
placed back onto the page when the user 'cancels' the current query.

Maybe its time to bring out that vue.js again.

Other Projects (that are not the website)
-----------------------------------------

I haven't exactly worked on any pet projects recently. This has been due mostly
to a lack of motivation. I will do my best to change that this quarter and this
upcoming summer.

There are three things I want to accomplish (if possible). I want to learn Rust,
more OS dev, learn to manage bigger projects and have fun. I'm not sure how
I'll accomplish these things, but I have currently set out a few things to do
for myself in the meantime.

### Rain (my old IRC project)

This project was a blast to work on. Sadly, I just didn't find the time on IRC
to find much motivation near the end before the project went stale. I want to
change that by moving the project to the Discord world.

I will keep much of the current structure the same, but I will repurpose the 
plugin system to something that I believe to be pretty cool.

I'll be doing my best to keep my golang skills sharp as I go along. Especially
my goroutine habits, they need a lot of work still.

### ARDeTS

I wouldn't do a web development based project, but this one is a little special
to me. Based off the work I did for a class, I want to plunge this idea into the
wild. I have a working prototype (and I mean prototype), but it currently uses
python and the web2py framework. I'm not too keen on using python, but if I have
to, I'd be willing to try out Django.

I'm also currently looking at Elixir/Phoenix or Go/Revel. But it might end up
being Python/Django. Whatever happens in the end, I'll probably post about it.

And no I'm not using Haskell/Yesod.

I Still Have to College Though
------------------------------

Sadly, I'm still in college and my time is limited. So don't go off expecting
anything big soon, maybe the tags. And also maybe the first C post tutorial for
that C tutorial series. Other than that, I have midterms to study for.

Have a day! (I'm starving and grumpy)