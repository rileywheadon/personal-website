Every day I get bombarded with more information than I can possibly remember. From lectures to videos to random blog posts I stumble across in my spare time, I estimate that my brain alone can recall maybe 10% of what I consume. Before I started my knowledge management journey, the other 90% would slip away, only to frustrate me later. "I'm pretty sure I learned how to do XYZ before, but I forgot and now I have to Google it" was an all-too-common experience. This bothered me because I hate doing things twice. To keep track of everything I'd learned, I started taking a lot of notes. However, this quickly became messy, so I began developing a way to stay organized--a *knowledge management system*. After a year of effort, this system has grown to hundreds of notes and improved my productivity significantly.

In this post, I will outline exactly *how* and *why* I take notes. Obviously, what I do is tailored to my interests and needs, and it may not work for everyone. At the very least, I hope reading this gives you ideas and motivation for developing your own knowledge management system.

**Philosophy**

As I mentioned previously, my goal is to never have to relearn a piece of information. Every time I learn a mathematical theorem or software library, I create a brief note and jot down any important details. The information that goes into my system comes from a variety of sources, including lectures, books, blogs, podcasts, and videos. You might think that taking notes on a blog is overkill, but hear me out. Taking notes forces you to not just understand the media you're consuming, but also summarize it.

According to Bloom's taxonomy ([source](https://www.valamis.com/hub/blooms-taxonomy)), taking notes moves you from remember/understand to at least apply. If you're being thorough, note-taking helps you deeply analyze what you're reading and find connections with other ideas. Yes, taking notes on a piece of media probably takes 2-3 times longer than just reading it. But this is a trade-off I'm willing to make. I'd rather read one book, learn it well, and have a list of ideas to revisit later than read three books haphazardly in the same time. If I learn something useful, I write it down. It's as simple as that.

When actually taking notes, I live by the rule *one idea, one note* principle. In practice, this means I don't make a note for each piece of media I consume. Instead, I add ideas from what I'm currently reading to related notes I already have. Note length isn't important to me. Some ideas require a lot of justification or context, while others can be as short as 2-3 sentences. I do not create separate notes for examples or practice problems. Instead, I include them under an `Examples` or `Exercises` header within an existing note. I believe that if a note really represents one idea, its title should be short. If I can't think of a concise title for a note, the note probably shouldn't exist.

**Obsidian**

I've found digital note-taking with [Obsidian](https://obsidian.md/) to be the most effective platform for my system. I'm not going to explain how Obsidian works (there's an excellent tutorial [here](https://help.obsidian.md/Home)), but I will outline why I use it. First, Obsidian has an extremely low barrier to entry while also being highly customizable and extensible. The plugin ecosystem for Obsidian is unmatched; it has solutions for every conceivable use case and more. Another advantage of Obsidian is that notes are stored as [Markdown](https://en.wikipedia.org/wiki/Markdown) files, so your notes will remain accessible even if Obsidian were to be deprecated. Since notes are stored locally, Obsidian gives you complete autonomy over your data, unlike cloud-based software such as [Notion](https://www.notion.so/) and Google Drive. Finally, Obsidian lets me edit my notes using [vim-like](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Vim+users) key bindings, which makes editing text *so* much faster. Everyone who spends a lot of time on their computer should learn vim, it's legitimately life-changing.

**File Structure**

The layout of my Obsidian vault is roughly based on the [Johnny Decimal](https://johnnydecimal.com/) system. I like this philosophy for arranging my folders because it places a hard limit on the amount of depth in my file tree. Why is depth bad? When you create a new file in Obsidian, it gets placed in the same folder as the file you currently have open. To avoid moving files around manually, it therefore makes sense to keep your file tree as shallow as possible. Additionally, the breadth of your file tree is no issue since Obsidian allows you to search your entire vault at once. You *could* put every single note and image into the root of your vault and Obsidian would work just fine. The issues start when you need to get all the files related to a certain topic. Then, [tags](https://help.obsidian.md/Editing+and+formatting/Tags) or folders are necessary. In conclusion, I would recommend setting up your vault to use as few folders as possible while still maintaining some semblance of structure.

Since my entire vault contains hundreds of notes, it can help to create maps of content (MOCs), which are notes whose sole purpose is to link to many other notes. I like to prefix my MOCs with the star (⭐️) emoji, which conveniently moves them to the top of the file explorer in the sidebar. If I need nested MOCs, I'll prefix the second layer with the home (🏠) emoji, which places these notes just beneath the starred notes in the file explorer. For an example of what my file structure looks like in practice, here's a snapshot of my "University" folder:

```
/30 University
	/31 UBC
		Schedule.md
		Course Planning.md
		Todo.md
	/32 MATH 320
		/32.01 Notes
			⭐️ MATH 320.md
			Least Upper Bound.md
			...
		/32.02 Resources
			math-320-textbook.pdf
		/32.03 Assignment 1
			main.tex
			...
			main.pdf
	/33 MATH 361
	...
```

**The Fuzzy Finder**

The **Fuzzy Finder** is Obsidian's mechanism for searching a vault, which locates notes by folder and title *simultaneously*. Then, by pressing `CMD + ENTER`, I can effortlessly open the top search result in a new tab. This is extremely useful because it allows me to create, delete, and switch between notes without having to open a file explorer. Because the fuzzy finder displays the file path, it's possible to differentiate notes by both their title *and* their location. Consider the following file tree:

```
/MATH-100
	formula-sheet
/PHYS-131
	formula-sheet
```

If I search for `MATH 100 formula sheet`, the fuzzy finder will only index the file in the MATH 100 folder, which allows me to have many notes with the same title across my vault.

## Plugins and Extensions

**LaTeX Suite**

The [Obsidian LaTeX Suite](https://github.com/artisticat1/obsidian-latex-suite) allows me to rapidly typeset $\LaTeX$ using a set of customizable snippets. I'm not going to elaborate on this plugin's functionality since I wrote a separate guide on it [here](../fast-typesetting/index.qmd).

**Advanced Tables**

Obsidian allows you to edit text in two ways--live preview and source mode. Since I type a lot of $\LaTeX$ in my notes, I prefer using source mode in order to see exactly what I'm typing. Unfortunately, this means I can't use the new [Table Editor ](https://obsidian.md/changelog/2023-12-26-desktop-v1.5.3/), which only works in live preview mode. To get around this problem, I use the [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) plugin, which gives me the functionality I need in source mode. Particularly, I am able to:

- Use `TAB` to cycle through cells.
- Bind hotkeys to insert and delete both rows and columns.
- Automatically align table border characters.
- Add basic Excel-like formulas to my tables.

This plugin only works in source mode, so if you use live preview, I would just stick to the built-in table editor.

**Citations**

I've doing research since May, and this means dealing with *a lot* of sources. I began using [Zotero](https://www.zotero.org/) to keep track of my references, but I wanted to have access to them within my Obsidian vault. The way I added this functionality was with the [Citations](https://github.com/hans/obsidian-citation-plugin) plugin, which automatically imports sources from a Zotero folder. Note that the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) Zotero extension is required for this to work. The Citations plugin also allows me to create "literature notes" containing relevant metadata from any reference in my Zotero folder.

*Update* (10/29/24): I am now using the [Zotero Integration](https://github.com/mgmeyers/obsidian-zotero-integration) plugin, although Citations is perfectly fine as well.

**Excalidraw**

I do not own a drawing tablet, so it's nice to have a way to create quick, informal diagrams. I've found the [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) plugin to work great for this use case. My favourite feature of this plugin is the ability to seamlessly import drawings into my notes without having to worry about exporting images from another piece of software.

**Linter**

The [Obsidian Linter](https://github.com/platers/obsidian-linter) plugin ensures that the markdown files within your vault are formatted consistently. It can do things like add a line break above and below lists, automatically capitalize headings, and remove consecutive empty lines. This normally wouldn't matter to me but Pandoc (see below) can get picky about markdown syntax.

**Pandoc**

The [Pandoc](https://pandoc.org/) CLI application has grown to be an *extremely* important part of my workflow. It allows me to export markdown files from my Obsidian vault to almost any other file type. I find this to be particularly useful when typesetting mathematics since the document formatting syntax in $\LaTeX$ is just awful. I've used Pandoc to produce research reports, assignments, and presentations using [Beamer](https://www.overleaf.com/learn/latex/Beamer). Of course, Pandoc trades control over document formatting for writing speed. Personally, this is a sacrifice I'm willing to make. But if you need to create professional documents, exporting markdown files via Pandoc probably won't provide enough capabilities.

*Update* (10/29/24): Exporting markdown files to PDF proved to be too cumbersome, so I am back to using $\LaTeX$ for more formal writing. 

**Quartz**

[Quartz](https://quartz.jzhao.xyz/) is the incredible software I use to turn my Obsidian vault into a "mini-blog". It seamlessly converts Obsidian-style markdown files to webpages and makes it easy to add links and attachments. My website doesn't have all the features of a real blog, like comments and feeds. But I can quickly push new posts and easily control the layout and style of my website, which is all I need for now. If you're interested in publishing your writing quickly and easily, I would recommend giving Quartz a try. It's even simpler than other lightweight blogging software like [Jekyll](https://jekyllrb.com/).

*Update* (08/01/2024): I've decided to give [Obsidian Publish](https://obsidian.md/publish) a try, and I've found it to be even more straightforward than Quartz. However, Obsidian Publish does require subscription ($8  USD/month or $4.80 USD/month with the student discount).

*Update* (10/19/2024): I've moved the blog over to [Quarto](https://quarto.org/) to improve support for code snippets.

## Conclusion

My Obsidian vault has grown to be more than just a note-taking system. I now use it to make to-do lists, create schedules, journal, and, of course, take notes. Using plugins and external software, I've extended my Obsidian vault to the point where it's the only software I need to produce documents of all kinds. By developing an efficient system for note-taking, I've made it easier to process the enormous amount of information I'm exposed to every day. This has helped me learn faster, write better, and study more effectively. If you're interested in trying something similar, the best time to start is now. All you need to do is start writing.

