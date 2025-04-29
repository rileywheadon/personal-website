## About Me

I'm Riley, a third year undergraduate student studying mathematics and statistics at the University of British Columbia.
In addition to my studies, I'm passionate about Unix, Vim, and software engineering.
I also enjoy running, [reading](/library), and playing the piano. 
On the [Big Five Personality Traits](https://en.wikipedia.org/wiki/Big_Five_personality_traits) I am high in openness and conscientiousness, roughly average in extroversion and neuroticism, and low in agreeableness.

I have spent much of the last year doing research in mathematical biology.
From April to December 2024, I worked with [Dr. Eric Cytrynbaum](https://personal.math.ubc.ca/~cytryn/index.shtml) to develop a mathematical model of root growth in *A. Thaliana*.
An up-to-date copy of our manuscript can be found [here](https://github.com/rileywheadon/root-modelling/blob/master/paper/main.pdf) and the code for the project can be found [here](https://github.com/rileywheadon/clasp-model).
I also took MATH 462 (Projects in Mathematical Biology), a graduate-level mathematical modelling course at UBC.
For the final project, my group and I explored models of the [Notch signalling pathway](https://en.wikipedia.org/wiki/Notch_signaling_pathway). 
I wrote a brief summary of our work [here](/blog).

I got my first exposure to Vim in 2023 after stumbling across an [excellent blog post](https://castel.dev/post/lecture-notes-1/) by Gilles Castel about using Vim to typeset mathematics.
After setting up a similar system using [Vim-bindings in Obsidian](/), I was hooked.
I gradually started using Vim for coding and writing, which piqued my interest in terminal-based workflows as a whole.
One thing led to the next, and in January 2025, I booted Linux for the first time on a refurbished Thinkpad T480. 
I strongly believe that software should be performant, reliable, and most importantly, [free](https://www.fsf.org/). 
I hope this mentality is reflected in my work.

## My Technology

I am currently running [archlinux](https://archlinux.org/) on a [Thinkpad T480](https://www.thinkwiki.org/wiki/Category:T480#Lenovo_ThinkPad_T480) (i5-7200U processor, 32GB DDR4 memory) as my primary computer. Here's some of the software I use regularly:

- **Compositor**: [Hyprland](https://github.com/hyprwm/Hyprland)
- **Browser**: Firefox with uBlock Origin
- **Terminal**: [kitty](https://github.com/kovidgoyal/kitty)
- **Shell**: `bash`
- **Terminal Multiplexer**: [tmux](https://github.com/tmux/tmux/wiki)
- **Text Editor**: [Vim](https://www.vim.org/)
- **Music Player**: [cmus](https://cmus.github.io/)
- **PDF Viewer**: [zathura](https://pwmt.org/projects/zathura/)
- **Image Viewer**: [imv](https://sr.ht/~exec64/imv/)
- **Password Manager**: [pass](https://www.passwordstore.org/)

## Site Design

The design of this site is inspired by [gwern.net](https://gwern.net/) and [maggieappleton.com](https://maggieappleton.com/), among others.
In particular, I've tried my best to design this site as a constantly evolving repository of my thoughts, as opposed to a set of polished blog posts.
This is the core idea of a [Digital Garden](https://maggieappleton.com/garden-history).
One key feature of digital gardens is *metadata*, which gives readers important information about the text they're about to read. Each page on this site contains the following seven metadata tags:

1. **Created**: The date on which the page was created.
2. **Modified**: The most recent date on which the page was modified.
3. **Topics**: A list of relevant keywords found on the page.
4. **Audience**: A short summary of the intended audience or simply "Everyone".
5. **Certainty**: My confidence in the post ("unlikely", "likely", "certain").
6. **Importance**: The utility of the post ("low", "medium", "high").
7. **Status**: My evaluation of completeness ("in progress", "in revisions", "complete"). If a page changes often, it will be marked as "ongoing".


## Site Implementation

I've built a handful of personal websites over the last two years with varying amounts of success. Now, I think that a good personal website needs to:

1. Showcase my personality and interests.
2. Allow me write blog posts in [Markdown](https://commonmark.org/).
3. Be simple to update and deploy.
4. Load *extremely* quickly.
5. Be inexpensive ($\$5$/month or less).
6. Be compatible with as many browsers and devices as possible.
7. Provide a space for hosting small personal projects.
8. Remain stable for as long as possible (preferably $20+$ years).
9. Use free and open source software.

This site is built with HTML, CSS, and a touch of vanilla Javascript.
As a web server, I am using [Flask](https://flask.palletsprojects.com/en/stable/), which I have found to be simple, minimalist, and powerful.
To minimize deployment costs, this site is hosted on a single [DigitalOcean](https://www.digitalocean.com/) droplet using [nginx](https://nginx.org/en/) as a reverse proxy.
In total, it costs me just $\$58$/year to keep everything running.
All of the technologies I've used to build this site have been around for at least $15$ years. 
The [Lindy Effect](https://en.wikipedia.org/wiki/Lindy_effect) says I can expect these technologies to survive for another $15$ years.
In today's web development environment, I'd say that's pretty good.

All of the pages for this site are written in Markdown, which I compile to HTML using [Pandoc](https://pandoc.org/). 
The styling is done using a single CSS file, which works on the HTML generated by Pandoc without modifications.
By using a custom Vim shortcut, I can compile and preview my blog posts while writing them.
I know this functionality also exists in static site generators such [jekyll](https://jekyllrb.com/) and Obsidian plugins like [quartz](https://quartz.jzhao.xyz/).
However, I've found building this site to be more rewarding (and also easier!) than using these technologies.
