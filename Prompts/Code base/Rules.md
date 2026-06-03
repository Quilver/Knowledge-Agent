# Directory Layout

- `LLM/wiki/index.md` — Master catalog. Every wiki page must appear here.
- `LLM/wiki/tags.md` — List of tags and categories. 
- `LLM/wiki/log.md` — Append-only activity log.
- `LLM/wiki/summaries/` — One summary page per document.
- `LLM/wiki/UML/` — Describe relationships between code base.
- `LLM/wiki/interfaces/` — Interfaces pages (role, functions, datatypes).
- `LLM/wiki/datatypes/` — describe a custom type of data in use.
- `LLM/wiki/functions/` — function with desccription, arguments, outputs, and examples.

# File Naming

- All lowercase, hyphens for word separation: `concept-name.md`
- No spaces, no special characters, no uppercase
- Name should match the page title slug



## Required Sections by Page Type

**Summary pages** (`wiki/summaries/`):
- `## Key Points` — Bulleted list of main claims/ideas
- `## Relevant Concepts` — Links to concept pages this source touches
- `## Source Metadata` — Type of source, author/speaker, date, URL or identifier

**Interface pages** (`wiki/concepts/`):
- `## Definition` — One-paragraph plain-English definition
- `## When To Use` — Situations and contexts where this interface applies
- `## Key Parameters` — Wiki links to related interfaces, data types and functions.
- `## Sources` — Which raw sources inform this page

**Function pages** (`wiki/concepts/`):
- `## Definition` — One-paragraph plain-English definition and link to owning interface
- `## Key Parameters` — List of input parameters and ouputs with Wiki links to custom data types and functions in use.
- `## When To Use` — Examples of situations and contexts where this function is used and resulting output
- `## Sources` — Which raw sources inform this page

**Data type pages** (`wiki/entities/`):
- `## Overview` — What this entity is
- `## Characteristics` — Key properties, attributes, structure
- `## Related Entities` — Links to related interface, Data type, function, and UML pages

**UML pages** (`wiki/syntheses/`):
- `## Comparison` — Table or structured comparison
- `## Analysis` — Cross-cutting insights
- `## Risks & Pitfalls` — Known failure modes, common mistakes, limitations
- `## Recommendations` — When to prefer which approach
- `## Pages Compared` — Links to all pages involved

# Linking Conventions

- Use Obsidian-style wiki links: `[[concepts/concept-name]]`
- Always use relative paths from wiki root
- Every page must link to at least one other page (no orphans)
- When mentioning a concept that has a page, always link it

# Tagging Taxonomy

- Have up to 8 categories
- Each category should have 3-8 specific tags. 

# Confidence Levels

- **high** — Well-established idea, multiple corroborating sources, demonstrated with concrete examples
- **medium** — Supported by sources but limited examples or single-source
- **low** — Single mention, anecdotal, or speculative

# Rules

- Prefer updating existing pages over creating duplicates
- When in doubt about a claim, set confidence to "low" and note the uncertainty
- Keep pages focused — one concept per page, split if a page gets too long
- Use plain English — define jargon on first use in each page
- When a source provides specific examples, include them with concrete details
