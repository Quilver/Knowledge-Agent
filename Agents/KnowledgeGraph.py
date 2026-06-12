import os
from typing import Tuple, List
import cognee
from cognee.infrastructure.databases.graph import get_graph_engine
import asyncio


def export_as_obsidian_vault(nodes, edges, output_dir="cognee_vault"):
    """Creates a local folder where every entity is its own .md file, 
    linking to other entities via [[Wikilinks]]."""
    os.makedirs(output_dir, exist_ok=True)
    
    #nodes = graph_data.get("nodes", [])
    #edges = graph_data.get("edges", [])
    
    # Map out relationships for easy lookup per node
    node_relationships = {node["id"]: [] for node in nodes if "id" in node}
    
    for edge in edges:
        src, tgt, rel = edge.get("source"), edge.get("target"), edge.get("type", "RELATED_TO")
        if src in node_relationships:
            node_relationships[src].append(f"- Extends to [[{tgt}]] via `{rel}`")
        if tgt in node_relationships:
            # Add a backlink for bi-directional context
            node_relationships[tgt].append(f"- Connected from [[{src}]] via `{rel}`")

    # Generate the individual files
    for node in nodes:
        node_id = str(node.get("id"))
        # Sanitize filename safely
        filename = "".join(c for c in node_id if c.isalnum() or c in (" ", "_", "-")).rstrip()
        if not filename:
            continue
            
        file_path = os.path.join(output_dir, f"{filename}.md")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {node_id}\n\n")
            f.write(f"**Type:** `{node.get('type', 'Unknown')}`\n\n")
            
            # Write unique metadata
            other_props = {k: v for k, v in node.items() if k not in ["id", "type"]}
            if other_props:
                f.write("## Properties\n")
                for k, v in other_props.items():
                    f.write(f"- **{k}**: {v}\n")
                f.write("\n")
            
            # Write links
            f.write("## Graph Relationships\n")
            relationships = node_relationships.get(node_id, [])
            if relationships:
                f.write("\n".join(relationships) + "\n")
            else:
                f.write("*No explicit connections indexed.*\n")
                
    print(f"Successfully exported Obsidian vault to: ./{output_dir}/")

async def export_graph_to_markdown():
    # 1. Fetch the underlying active graph engine from Cognee
    graph_engine = await get_graph_engine()
    
    # 2. Extract the raw graph dictionary containing 'nodes' and 'edges'
    nodes,edges = await graph_engine.get_graph_data()
    # 3. Export the graph data into a local folder as markdown files
    cognee_folder = os.getenv("COGNEE_Folder")
    export_as_obsidian_vault(nodes, edges, output_dir=str(cognee_folder))
async def main():
    # Create a clean slate for cognee -- reset data and system state
    await cognee.forget(everything=True)

    # Store content in memory (ingests, builds knowledge graph, enriches)
    text = """
Albert Einstein[a] (14 March 1879 – 18 April 1955) was a German-born theoretical physicist who is best known for developing the theory of relativity. Einstein also made important contributions to quantum mechanics.[1][5] His mass–energy equivalence formula E = mc2, which arises from special relativity, has been called "the world's most famous equation".[6] He received the 1921 Nobel Prize in Physics for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect.[7]

Born in the German Empire, Einstein moved to Switzerland in 1895, forsaking his German citizenship (as a subject of the Kingdom of Württemberg)[note 1] the following year. In 1897, at the age of seventeen, he enrolled in the mathematics and physics teaching diploma program at the Swiss federal polytechnic school in Zurich, graduating in 1900. He acquired Swiss citizenship a year later, which he kept for the rest of his life, and afterwards secured a permanent position at the Swiss Patent Office in Bern. In 1905, he submitted a successful PhD dissertation to the University of Zurich. In 1914, he moved to Berlin to join the Prussian Academy of Sciences and the Humboldt University of Berlin, becoming director of the Kaiser Wilhelm Institute for Physics in 1917; he also became a German citizen again, this time as a subject of the Kingdom of Prussia.[note 1] In 1933, while Einstein was visiting the United States, Adolf Hitler came to power in Germany. Horrified by the Nazi persecution of his fellow Jews,[8] he decided to remain in the US, and was granted American citizenship in 1940.[9] On the eve of World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential German nuclear weapons program and recommending that the US begin similar research.

In 1905, sometimes described as his annus mirabilis (miracle year), he published four groundbreaking papers.[10] In them, he outlined a theory of the photoelectric effect, explained Brownian motion, introduced his special theory of relativity, and demonstrated that if the special theory is correct, mass and energy are equivalent to each other. In 1915, he proposed a general theory of relativity that extended his system of mechanics to incorporate gravitation. A cosmological paper that he published the following year laid out the implications of general relativity for the modeling of the structure and evolution of the universe as a whole.[11][12] In 1917, Einstein wrote a paper which introduced the concepts of spontaneous emission and stimulated emission, the latter of which is the core mechanism behind the laser and maser, and which contained a trove of information that would be beneficial to developments in physics later on, such as quantum electrodynamics and quantum optics.[13]

In the middle part of his career, Einstein made important contributions to statistical mechanics and quantum theory. Especially notable was his work on the quantum physics of radiation, in which light consists of particles, subsequently called photons. With physicist Satyendra Nath Bose, he laid the groundwork for Bose–Einstein statistics. For much of the last phase of his academic life, Einstein worked on two endeavors that ultimately proved unsuccessful. First, he advocated against quantum theory's introduction of fundamental randomness into science's picture of the world, objecting that God does not play dice.[14] Second, he attempted to devise a unified field theory by generalizing his geometric theory of gravitation to include electromagnetism. As a result, he became increasingly isolated from mainstream modern physics.
"""
    await cognee.remember(text)

    # Retrieve from memory
    results = await cognee.recall(
        query_text="What does Cognee do?"
    )

    # Print
    for result in results:
        print(result)

    visualize_graph_path = os.path.join(
    os.path.dirname(__file__), ".artifacts", "graph_after_remember.html"
    )
    await cognee.visualize_graph(visualize_graph_path)
    await export_graph_to_markdown()

if __name__ == '__main__':
    asyncio.run(main())

