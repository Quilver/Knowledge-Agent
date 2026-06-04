from fastmcp import FastMCP
from typing import Any, Dict, Type, List
from enum import Enum
import yaml, os, re
from datetime import datetime
class PageTypes(Enum):
    summaries="summaries"
    UML = "UML"
    interfaces = "interfaces"
    datatypes = "datatypes"
    functions = "functions"
class Confindence(Enum):
    high="high"
    medium="medium"
    low="low"
# FileName
"""
# FileName:
    - All lowercase, hyphens for word separation: `concept-name.md`
    - No spaces, no special characters, no uppercase
    - Name should match the page title slug
"""
# Page Format
"""
# Page Format

Every wiki page uses this frontmatter and structure:

```yaml
---
title: "Page Title"
type: concept | entity | summary | synthesis
tags: [tag1, tag2, tag3]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["raw/filename.txt"]
confidence: high | medium | low
---
```
"""
# Required Sections by Page Type
"""
## Required Sections by Page Type

**Summary pages** (`wiki/summaries/`):
- `## Key Points` — Bulleted list of main claims/ideas
- `## Relevant Concepts` — Links to concept pages this source touches
- `## Source Metadata` — Type of source, author/speaker, date, URL or identifier

**Concept pages** (`wiki/concepts/`):
- `## Definition` — One-paragraph plain-English definition
- `## How It Works` — Mechanics, process, or structure of the concept
- `## Key Parameters` — Important variables, dimensions, or factors
- `## When To Use` — Situations and contexts where this concept applies
- `## Risks & Pitfalls` — Known failure modes, common mistakes, limitations
- `## Related Concepts` — Wiki links to related pages
- `## Sources` — Which raw sources inform this page

**Entity pages** (`wiki/entities/`):
- `## Overview` — What this entity is
- `## Characteristics` — Key properties, attributes, structure
- `## Common Strategies` — Links to concept pages for strategies or methods associated with this entity
- `## Related Entities` — Links to related entity pages

**Synthesis pages** (`wiki/syntheses/`):
- `## Comparison` — Table or structured comparison
- `## Analysis` — Cross-cutting insights
- `## Recommendations` — When to prefer which approach
- `## Pages Compared` — Links to all pages involved
"""

FILE_ROOT = "E:/Obsidian/LLM Guide"
WIKI_ROOT = FILE_ROOT+ "/LLM/wiki"


def updateIndexAndLog(title:str, page_type:PageTypes, tags:List[str]):
    with open(WIKI_ROOT+"/index.md", 'a', encoding='utf-8') as f:
        f.write(f"[[{page_type.value}/{slugify(title)}]]:{tags} \n")
    with open(WIKI_ROOT+"/log.md", 'a', encoding='utf-8') as f:
        f.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Created {page_type.value} page: {title} with tags {tags}")


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


#@mcp.tool
def CreateFile(title: str, page_type: PageTypes, tags: List[str], sources:List[str], confidence:Confindence, content: str)->str:
    """
    Creates a wiki page in the wiki subdirectory.

    Args:
        title: name of the wiki page
        page_type: type of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file
        confidence: high | medium | low
        content: content of wiki page
    Output:
        Result: Success | Failure
    """
    slug = slugify(title)

    frontmatter = yaml.dump({
        "title": title, "type": page_type, "tags": tags,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "sources": sources, "confidence": confidence
    }, sort_keys=False)
    os.makedirs(f"{WIKI_ROOT}/{page_type.value}", exist_ok=True)
    file_path = f"{WIKI_ROOT}/{page_type.value}/{slug}.md"
    frontmatter = yaml.dump({
        "title": title, 
        "type": page_type.value, 
        "tags": tags,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "sources": sources, "confidence": confidence
    }, sort_keys=False)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"---\n{frontmatter}---\n\n{content}")
    updateIndexAndLog(title, page_type, tags)
    return "Success"

