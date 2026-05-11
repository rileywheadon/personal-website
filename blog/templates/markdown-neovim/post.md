I've recently started doing all my development work and note-taking in Neovim.
It's been great so far, but I've really missed my setup for [Fast Typesetting in Markdown with Obsidian LaTeX Suite](/fast-typesetting).
With summer classes starting today, I decided to stop procrastinating and finally get my snippets up and running in Neovim.
But the process wasn't as easy as I hoped.
In this blog post, I'll give a brief overview of the problems I faced and how I eventually overcame them.

## Introduction

I take all of my course notes in Markdown.
I'm a mathematics major, so these notes contain a lot of formulas and equations.
To typeset these equations, I inline [LaTeX](https://www.latex-project.org/) into my Markdown files.
In the raw Markdown text files, equations look like this:

```markdown
$$
5x^2 + 3x + \int_{0}^{\infty} \frac{1}{x}\,dx
$$
```

But when rendered, the equations look like this:

$$
5x^2 + 3x + \int_{0}^{\infty} \frac{1}{x}\,dx
$$

Inlining LaTeX in Markdown has a lot of advantages.
First, Markdown is much more pleasant to write than LaTeX.
So, by using LaTeX in Markdown (instead of straight LaTeX) you get the lightweight headers, styles and code blocks from Markdown instead of their heavier LaTeX equivalents.
Markdown is also widely used by static site generators, GitHub, and communication tools (e.g. Slack, Discord), so using Markdown makes it easy to share work.

But a LaTeX in Markdown setup also comes with a lot of technical challenges:

1. The user needs a way to preview the rendered equations.
2. Special syntax highlighting rules must be set up for inline LaTeX code.
3. Snippets (like [these ones](/fast-typesetting) I set up in Obsidian) need to be aware of when the user is editing regular Markdown text and when the user is editing LaTeX in Markdown.

## Part 1: Previewing

I am using [selimacerbas/markdown-preview.nvim](https://github.com/selimacerbas/markdown-preview.nvim) with the default configuration to render Markdown and LaTeX in my browser.
I prefer this plugin to the other Markdown preview plugins because it doesn't require any external dependencies like NodeJS.

## Part 2: Syntax Highlighting

Unlike Vim, Neovim has [built-in support for treesitter](https://neovim.io/doc/user/treesitter/).
However, we still need a way to manage which treesitter parsers are installed and a way to enable/disable them.
For this, I use [romus204/tree-sitter-manager.nvim](https://github.com/romus204/tree-sitter-manager.nvim).
I've configured `<leader>tm` to open the TUI using the following Lua code:

```lua
vim.keymap.set(
  "n",
  "<leader>tm",
  ":TSManager<CR>",
  { desc = "Open tree-sitter-manager" }
)
```

In order to get proper syntax highlighting for both Markdown and inline LaTeX, the treesitter grammars for both Markdown and LaTeX must be installed.
While this could be done through the tree-sitter-manager TUI, I have opted to configure tree-sitter-manager to guarantee that the Markdown and latex parsers are installed:

```lua
require("tree-sitter-manager").setup({
  ensure_installed = {
    "markdown",
    "latex"
  }
})
```

In order to confirm that both treesitter grammars are working, you can open a new Markdown file and add inline LaTeX (e.g. `$x^2$`).
Then, run `:InspectTree`.
If the LaTeX parser is working, you should see a node called `inline_formula`.

## Part 3: Snippets

A snippet is simply a sequence of keystrokes that is automatically expanded by Neovim.
For example, when I type `int` (as in "integral") within a LaTeX block, I have a snippet to insert the full LaTeX integral command with bounds: `\int_{<>}^{<>} <>`.
The `<>` characters are tabstops -- when I press tab, Neovim moves my cursor to the next tabstop.

I use [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip) to manage my snippets ([documentation](https://github.com/L3MON4D3/LuaSnip/blob/master/DOC.md)).
This plugin is very powerful, but more complicated than a plugin like [SirVer/UltiSnips](https://github.com/SirVer/ultisnips), which defines snippets using simple `.snippets` files.
The snippet engine (LuaSnip or UltiSnips) also needs a completion engine.
I've been using [Saghen/blink.cmp](https://github.com/Saghen/blink.cmp) with the default configuration.

### Detecting Math Mode

When I'm editing Markdown, I only want my math-related snippets to activate when I'm editing LaTeX.
This is especially important because I make extensive use of LuaSnip's autosnippets feature, which expands snippets immediately after the trigger is typed.
So, if I didn't have a mechanism to conditionally expand snippets, the text `\int_{}^{} ` would be added to my prose every time I typed a word starting with "int", for example.

To check if I'm in a LaTeX block, I use the following Lua function:

```lua
local function in_math()

  -- Get the treesitter node under the cursor
  local node = vim.treesitter.get_node({ignore_injections = false})

  if not node then
    return false
  end

  -- This is a recursive function that traverses up through the AST
  while node do
    local t = node:type()

    -- The node type inline_formula means we are in inline LaTeX ($...$)
    -- The node type displayed_equation means we are in display LaTeX ($$...$$)
    if t == "inline_formula" or t == "displayed_equation" then
      return true
    end

    -- The text_mode node type means we are inside LaTeX but inside a \text{}
    -- tag. We want to be able to type freely, so we disable snippets
    if t == "text_mode" then
      return false
    end

    node = node:parent()
  end

  return false
end
```

### Shorthand for Simpler Snippets

Another thing that I've noticed about the LuaSnip syntax is that it tends to be quite verbose.
For my needs, I just need to define the snippet trigger, the tabstops, and in exceptional cases, the snippet priority (so that if one snippet is a substring of another, I can control which one activates).
To help make my snippet writing experience more straightforward, I wrote three helper functions: `_m` (math-mode autosnippet), `_a` (autosnippet), and `_r` (regular snippet).

```lua
local function md_snippet(trig, type, str, ins, cond, prio)
	prio = prio or 0
  local nodes = {}
  for idx, val in ipairs(ins) do
    nodes[idx] = i(val, "")
  end

  opts = { trig = trig, snippetType = type, wordTrig = false, priority = prio }
  return s(opts, fmta(str, nodes), cond)
end

local function _m(trig, str, ins, prio)
  return md_snippet(trig, "autosnippet", str, ins, { condition = in_math }, prio)
end

local function _a(trig, str, ins)
  return md_snippet(trig, "autosnippet", str, ins, {})
end

local function _r(trig, str, ins)
  return md_snippet(trig, "snippet", str, ins, {})
end
```

These helper functions make my snippet definitions much more concise.
For example,

```lua
-- create a markdown table
_r("table", "| <> | <> |\n|--|--|\n| <> | <> |", {1, 2, 3, 4}),

-- automatically expand a display math environment
_a("dm", "$$\n<>\n$$\n", {1}),

-- write an integral
_m("int", "\\int_{<>}^{<>} <>\\,d", {1, 2, 3}),
```

## Conclusion

I hope you found this interesting and helpful!
See my [dotfiles](https://github.com/rileywheadon/dotfiles) for the complete setup.
