import igraph as ig
import matplotlib.pyplot as plt

agencies = ["os", "cdc", "nih", "ahrq", "ihs", "ogc", "hrsa", "samhsa", "acf", "cms", "fda"]
reported_density = [0.5, 0.7, 0.58, 0.83, 1, 1, 1, 0, 1, 1, 1]
data_density = []

for agency in agencies:
    graph = ig.load(f"data/{agency}_cluster.gml")
    density = graph.density()
    data_density.append(density)
    print(f"{agency}:", density)


# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# First subplot for reported densities
axs[0].bar(agencies, data_density, color='black')
axs[0].set_title('Data Densities')
axs[0].set_ylabel('Densities')
axs[0].set_ylim([0, 1.2])

# Second subplot for real densities
axs[1].bar(agencies, reported_density, color='black')
axs[1].set_title('Reported Densities')
axs[1].set_ylabel('Densities')
axs[1].set_ylim([0, 1.2])

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

