# Rewrite

**Style & Features**

- Collapsible metadata at the top of each post
- Beautiful, large, serif typography and a minimalist design
- Links coloured but not underlined (except on hover)
- Footnotes with hover previews and return links
- Focus _heavily_ on quality over quantity with _some_ links
- Host small projects (i.e. zetamac-reloaded) in `/projects/...`
- Comments on the bottom of all posts/projects (stored in an sqlite databaes)

**Pages**

- `/` introduction 
- `/about` about me
- `/design` about the site
- `/library` collection of books i've read with reviews
- `/employers` specifically for employers (list of skills, CV, etc.)
- `/projects` list of projects, links to git repo, blog post, etc. 
- `/blog` index of writing with backlinks to projects when necessary

**Metadata**

- audience
- dates
- certainty
- importance
- maturity
- topics

## Design

Store blog posts in `/posts` in Github flavoured markdown.

- Each post gets its own directory
- Store the metadata in a `metadata.json` file (automatic edit times?)
- Store the post in a `post.md` file
- Also store any images and archived websites/documents in the directory

Build the website in `/site`.

- Serve the static pages (listed above) directly from Flask
- Write a Python script to export all the posts to `/site/posts`
- Each post gets embedded in a Jinja template which also applies styles
- The default Jinja template also contains a navbar and footer
- Write another template for automatically adding the metadata element
- Write another template for adding comments on the bottom of posts/projects

Hosting:

- Use https://nginx.org/en/ and https://docs.gunicorn.org/en/latest/index.html
- Deploy to a DigitalOcean droplet with the cheapest plan (\$4/month)

