## Ingest

When the user says "ingest [source]":

1. Read the source 
2. Create a summary of the source with CreateFile tool
3. Identify all concepts, entities, and strategies mentioned and use CreateFile tool to record them
4. Add cross-links in both directions between all touched pages
5. Update `wiki/index.md` — add new entries, update summaries of changed pages
6. Append to `wiki/log.md` with timestamp, source name, pages created/updated
7. Flag any contradictions with existing wiki content
