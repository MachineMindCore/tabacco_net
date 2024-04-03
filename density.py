import igraph as ig

graph = ig.load("data/dhhs.gml")
density = graph.density()

angency_graph = ig.load("data/agencies.gml")
agency_density = angency_graph.density()

print("Individuals graph density:", density)
print("Agencies graph density:", agency_density)

betweenness = dict()

print(graph.vs.attributes())
measure_bet = graph.betweenness(directed=False)