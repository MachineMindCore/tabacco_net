import igraph as ig
import matplotlib.pyplot as plt

agencies = ["OS", "CDC", "NIH", "AHRQ", "IHS", "OGC", "HRSA", "SAMHSA", "ACF", "CMS", "FDA"]
reported_nodes = [3, 12, 16, 4, 2, 3, 3, 3, 2, 2, 2]
data_nodes = []

graph = ig.load(f"data/dhhs.gml")
for agency in agencies:
    nodes = len(graph.vs.select(lambda vertex: agency in vertex.attributes()["vertexnames"]))
    data_nodes.append(nodes)
    print(f"{agency}:", nodes)


# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# First subplot for reported densities
axs[0].bar(agencies, data_nodes, color='black')
axs[0].set_title('Data Nodes')
axs[0].set_ylabel('Nodes')

# Second subplot for real densities
axs[1].bar(agencies, reported_nodes, color='black')
axs[1].set_title('Reported Nodes')
axs[1].set_ylabel('Nodes')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
