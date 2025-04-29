---
title: "Havoc on the Hill: An Analysis of Canadian Legislation"
date: "2025-03-31"
date-modified: "2025-03-31"
categories: [Python, BeautifulSoup4, pandas, plotly]
---

In January 2023, I did my first data analysis project on the legislative process here in Canada.
I used the [LEGISinfo](https://www.parl.ca/legisinfo/en/overview) database as my primary source of information, which contains a record of all the bills created, read, and passed since 1994.
After I downloaded *literally all* the data from LEGISinfo[^1], I built a web scraper with [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) to get more information about current and former members of parliament (MPs).
This data included their party affiliations, their roles in the government or opposition, and the years they were active.
Then, I used [pandas](https://pandas.pydata.org/) to analyze the data and [plotly](https://plotly.com/) to create some visualizations[^2].
In this post, I'll present $8$ simple charts that contain the results of this analysis.
I hope you find it interesting!

[^1]: There really wasn't that much, since bills don't get written very often.

[^2]: In hindsight, I don't know why I didn't use matplotlib for plotting. It's so much faster than plotly. For some reason, it took like ten minutes to render these graphs. Oh well, you live and you learn.

## Part 1: Making the Bills

In the Canadian Parliament, a *bill* is a proposed law that is introduced for debate before becoming an official *act of parliament*. Bills originate from one of Canada's two legislative chambers, the *House* and the *Senate*. All bills are either *public* (pertaining to all people) or *private* (pertaining to a specific group of people). If a bill is proposed in the House, it must be public. Three groups of people can propose bills: *senators*, *private members*[^4], and the *government*. The government consists of MPs[^5] associated with the ruling party (typically cabinet ministers). MPs not associated with the ruling party are known as private members.

![Figure 1: Bills proposed by type and origin in the Canadian Parliament. The vast majority of bills are proposed by private members in the House of Commons. Government bills are the second largest category, with $1189$ bills. Of the $\approx 700$ bills proposed in the Senate, only $31$ are private bills. Since MPs cannot propose private bills, private bills make up only $\approx 0.5\%$ of all bills.](/templates/havoc-hill/bills-by-type.png)

Canada has three main political parties: the Liberals, the Conservatives, and the NDP. We also have some smaller parties, such as the Bloc Quebecois (focused on Quebec), the Green Party (focused on environmental issues), and the People's Party (~~focused on conspiracy theories~~). The Canadian Alliance was a now-defunct offshoot of the Conservative party that existed from 2000-2003. In Figure 2, the "Independent" category refers to MPs who are not affiliated with any party.

![Figure 2: Bills proposed by party in the House of Commons. Interestingly, the NDP have proposed the most bills, even though they have been consistently relegated to third-party status. The rest of this chart is not so surprising, although it is interesting that independent MPs have proposed more bills than the Green Party, Canadian Alliance, and People's Party combined.](/templates/havoc-hill/bills-by-party.png)

The last aspect of bill creation I investigated was whether the governing party proposed more bills than the official opposition. To answer this question, I compared the number of bills proposed by the Conservative and Liberal parties under Stephen Harper's conservative government and Justin Trudeau's liberal government. The results of this analysis are shown in Figure 3.

![Figure 3: Unsurprisingly, the governing party tends to propose more bills than the official opposition, by a $\approx 25\%$ margin. Honestly, this margin was smaller than I expected. With all the partisanship in today's political climate, it is easy to feel like all the opposition does is complain, but this plot clearly disproves such feelings.](/templates/havoc-hill/bills-by-pm.png)

[^4]: Private *members* and private *bills* are two different things.

[^5]: If you are unfamiliar with Canadian politics, MPs are elected officials who sit in the House of Commons. Their role is roughly equivalent to American congressmen.

## Part 2: Reading the Bills

A productive government should ensure that all proposed bills are read. Whether the government actually passes these bills is more nuanced, but at the very least I would hope the government is reading a couple of bills a day. So here's another plot, which shows the average number of bill readings per day in the past $17$ sessions of the House of Commons. This statistic (and the similar statistic in Figure 8) uses the total number of days that the parliament was in session, not the number of days in which MPs actually met and read bills. Therefore, parliament probably reads $\approx 50\%$ more bills than Figure 4 suggests each time it sits.

![Figure 4: A plot of readings per day in all parliament sessions since 1994. Stephen Harper's minority conservative government between 2007 and 2010 read the most bills. Justin Trudeau's 2015 majority government and 2019 minority governments read far fewer bills per day.](/templates/havoc-hill/readings-per-day.png)

In addition to the *number* of bills read each day, I would also hope that a productive government would either pass or fail the bills in a reasonable amount of time. This can be measured with *deliberation time*, or the length of time between a bill being proposed and its last reading. If a bill fails upon the first reading, its deliberation time will be short. However, the deliberation time remains a useful metric for the bills that make it past the first reading, since the majority of these bills are eventually passed (see Figure 7). Thus, the median deliberation time serves as a proxy for a government's bill-passing speed.

![Figure 5: Boxplot of deliberation times by prime minister. The median deliberation time appears to be approximately constant across the past four prime ministers. However, the 3rd quartile of deliberation times is noticeably higher under the two most recent governments, especially Justin Trudeau's.](/templates/havoc-hill/deliberation-time-pm.png)

![Figure 6: The distribution of all deliberation times in the dataset. As mentioned previously, many bills had deliberation times of $<50$ days, since many bills fail. The vast majority of bills finish deliberation in $<300$ days, although there are a handful of outliers with $>500$ day deliberation times.](/templates/havoc-hill/deliberation-time.png)

## Part 3: Passing the Bills

To become law, a bill must pass $6$ readings ($3$ in the House and $3$ in the Senate) and then receive *royal assent* from the [governor general of Canada](https://en.wikipedia.org/wiki/Governor_General_of_Canada). Royal assent is essentially a formality in Canada; even though the governor general has the power to strike down a bill, no governor general has ever exercised this power. Figure 7 shows the number of bills that pass each reading.

![Figure 7: The number of bills that passed each stage in the legislative process. Most bills fail at the first and second readings. However, a non-negligible portion of the bills also fail at the fourth and fifth readings, after the bill moves to the other legislative chamber. Very few bills fail at the third and sixth readings, and all bills that reach royal assent have been approved.](/templates/havoc-hill/bills-by-stage.png)

Finally, I investigated how many bills were *passed* per day in each session of parliament (recall that we were looking at the number of bills *read* in Figure 4). The results of this analysis are shown in Figure 8.

![Figure 8: Bills passed per day in each session of parliament since 1994. The data show a steady decline in the number of bills passed per day, regardless of which party is in power and whether the government is a minority or a majority. ](/templates/havoc-hill/bills-per-day.png)

## Conclusion

I did a lot of analysis by political party in this blog post. This should go without saying, but *the number of bills read/passed/proposed by a political party should not be taken as a measure of how good (or bad) the party is*. 

With that out of the way, thanks for reading!

I hope you found this interesting. If you want to view my horrendous[^3] two-year-old source code, it's available on my [GitHub](https://github.com/rileywheadon/canadian-legislation-visualisation).

[^3]: I'm not kidding. This project is $4$ really long Jupyter notebooks. I'm not even sure if they work anymore, since I didn't create a virtual environment and I have no idea which versions of Python, pandas, plotly, and BeautifulSoup4 I used. I swear I know better now.
