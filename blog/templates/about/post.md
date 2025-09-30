## About Me

I'm Riley, a fourth year undergraduate student studying mathematics and statistics at the University of British Columbia.
In addition to my studies, I'm passionate about Unix, Vim, and software engineering.
I also enjoy running, [reading](/library), [hiking](/hiking), and playing the piano. 
I am currently working at [SAP Canada](https://www.sap.com/canada/index.html) as a CI/CD intern until April 2026. 

From May to August 2025, I worked with [Dr. Cuauhtémoc T. Vidrio Sahagún](https://profiles.ucalgary.ca/cuauhtemoc-t-vidrio-sahagun) and [Dr. Alain Pietroniro](https://profiles.ucalgary.ca/alain-pietroniro) to implement a [Flood Frequency Analysis Framework](https://www.sciencedirect.com/science/article/pii/S136481522400001X) in the R programming language.
Documentation for the software I created can be found [here](https://rileywheadon.github.io/ffa-framework/).
Before this, I spent a year doing research in mathematical biology.
From April to December 2024, I worked with [Dr. Eric Cytrynbaum](https://personal.math.ubc.ca/~cytryn/index.shtml) to develop a mathematical model of root growth in *A. Thaliana*.
An up-to-date copy of our manuscript can be found [here](https://github.com/rileywheadon/root-modelling/blob/master/paper/main.pdf) and the code for the project can be found [here](https://github.com/rileywheadon/clasp-model).
I also took MATH 462 (Projects in Mathematical Biology), a graduate-level mathematical modelling course at UBC.
For the final project, my group and I explored models of the [Notch signalling pathway](https://en.wikipedia.org/wiki/Notch_signaling_pathway). 
I wrote a brief summary of our work [here](/blog).

I got my first exposure to Vim in 2023 after reading this [excellent blog post](https://castel.dev/post/lecture-notes-1/) by Gilles Castel.
After setting up a similar system using [Vim-bindings in Obsidian](/fast-typesetting), I was hooked.
I gradually started using Vim outside of Obsidian, which piqued my interest in terminal-based workflows using `tmux` and tiling window managers.
In January 2025, I booted Linux for the first time and have been daily-driving it ever since. 
I strongly believe that software should be simple, performant, and reliable.
I hope this mentality is reflected in my work.

## Site Design

I've tried to keep this site as simple as possible.
All of the pages are written in Markdown, which I compile to HTML using [Pandoc](https://pandoc.org/) and a shell script.
Styles are defined globally in a single CSS file.
To host the site, I use [nginx](https://nginx.org/en/) on a [DigitalOcean](https://www.digitalocean.com/) droplet with a post-receive hook that automatically redeploys the site when I push changes.

This site also uses metadata to provide additional context about each post and make it easier to identify out-of-date content.
My implementation of metadata uses the following seven labels:

1. **Created**: The date on which the page was created.
2. **Modified**: The most recent date on which the page was modified.
3. **Topics**: A list of relevant keywords found on the page.
4. **Audience**: A short summary of the intended audience or simply "everyone".
5. **Certainty**: My confidence in the post ("unlikely", "likely", "certain").
6. **Importance**: The utility of the post ("low", "medium", "high").
7. **Status**: My evaluation of completeness ("in progress", "in revisions", "complete"). 
