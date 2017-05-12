---
title: Intro to C 
date: 2017-05-11
post-id: intro-to-c 
---

As promised, the first post in my C tutorial series is here!

# C (and Why You Should Learn It)

The biggest reason I believe any programmer should have C under their belt, is
mostly for the fact that they might not deal with assembly as much as
programmers from the past did.

Sure this is a good thing, but it has developed a generation of programmers
willing to give up efficient programming over compiler optimizations. This works
for the most part, but it provides a false confidence that can be serious if not
looked after. Programmers from the past had to be conscious about every line of 
code they created.

They had very limited resources (time, storage, accessibility) and usually had 
to make sure they got things right the first time. This skill is invaluable and
quickly fading away.

### So Why C?

It's as close to assembly as you can get without learning assembly. It still
does a lot of things for you, but it won't manage intricacies. You must manage
your own memory, be conscious of bound checking, looking for undefined
behavior (that the compiler won't tell you about) and various other pains.

However, it's high-level enough to _not be_ so much of a pain. You'll learn alot
about how higher-level languages handle their memory, and why they suffer
from performance lost in comparison to C. It might even show you why sometimes
C is an efficient enough answer. It is a language that is very simple, yet very
effective at what it does. 

Does it really keep up with modern times? Yes and no. Let's consider golang for
this. Golang is a language invented by Google a good while back. It borrows
heavily from C's nature of simplicity, but with some modern goodies to make your
life simpler. Over the years, Go has become extremely popular not only with its
original intended audience, but with a greater more general populace.

This is only one example of how C has influenced other languages. Sometimes
other languages try to take a jack hammer to a problem, and C's simplicity is
just enough.

### But Enough Talk

It's about time we get our hands dirty!

# Anatomy of a C Program

<script src="https://gist.github.com/wolfchase/2b0ddec1c2440ff8a437700da3c93ace.js"></script>

A small down-to-the-ground barebones C program. Before we go off compiling this,
let's talk about the *everything*.

### CPP Directives

Before anything happens during compilation of a C program, the bare text of it
is filtered through the C preprocessor (CPP). It looks for preprocessor
directives; these are lines starting with a '#.' I bet you've found the
_include_ directive already!

This does what it sounds like it does. Namely, it finds the file you specify; 
takes the text (or source code) from that file and inserts it into your program
directly (just like copying and pasting). Don't worry, it doesn't take in the
_whole_ source code, just things needed for things to be referenced. We'll talk
about this referencing stuff in more detail in the next few posts.

So for now, __#include__ just includes some stuff from the __stdio.h__ file.
This file is part of the C standard library (found somewhere on your computer).
This file will be found by the compiler-it'll know where it is I promise! Again,
more details in future posts.

### Hey Look! A Function?

Not just a function, its the _main_ function. As you could guess as well, it 
returns an _int_, an integer. What's this void thing mean? Basically its just a
fancy way to tell the compiler that this function doesn't take in any functions.

What's so special about a _main_ function? There can only ever _be one_ and no
more. This is how the compiler knows where the program starts from.

### printf (You're gonna be best friends)

Ah, the almighty printf function. It has friends too, but we won't cover those
until a good while. It does what it seems like, prints a given line. However, 
the f at the end definitely means something, __format__. It takes in a string
that can be _formatted_. There's also things called format specifiers to alter
and modify output, but we'll get to those next time around.

For now its worth keeping in mind that you have to put your own new line
character, '\\n,' unless of course you want everything printed on one line!

### Finally, we Return

The __return statement__ tells C that this function is now exiting and returning
the stated constant __0__. Usually returning a number from the main function has
big significance. It is conventional to return 0 upon a _successful_ completion
of a program. Anything else (most commonly 1) means the program encountered an
error at some point in execution.

### How to Compile

You'll need to have a compiler installed. If you're on Linux or some equivalent,
you might already have __gcc__ installed. But for the time being, we'll just
stick to using ideone.com, an online compiler. As a matter of fact, the program
is online ready for editing and compiling [here](http://ideone.com/FTzSy9). Play
around with it if you want and get accustommed to ideone as well.

# Well That's it (For Now)

I'll be creating what I call _specials_. These will be posts that talk about
things that might be too much to talk about in the tutorial series, but
definitely worth checking out. The first one will be coming around sooner than
later and will involve installing a C compiler on your system.

I also hope that this becomes a do-and-learn experience. I'll do my best to
increase the quality of these posts as much as I can! With that I let you all be
and hope that you'll continue to join me on one hell of an adventure.




