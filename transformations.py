import igraph as ig

def agency_families(tobacco_graph):
    # Dictionary to store accumulated nodes by agency family
    new_g = ig.Graph(directed=tobacco_graph.is_directed())
    accumulated_nodes = {}

    # Iterate over nodes to accumulate by agency family id
    node_id = 0
    for node in tobacco_graph.vs:
        agency_family_id = int(node['agency'])
        agency_name = node['vertexnames'].split("-")[0]
        if agency_family_id not in accumulated_nodes:
            accumulated_nodes[agency_family_id] = []
            new_g.add_vertex(
                id=node_id,
                agency=agency_family_id,
                vertexnames=agency_name,
            )
            node_id += 1
        accumulated_nodes[agency_family_id].append(node.index)


    # Accumulate collab values for edges between agencies
    collab_accumulator = {}
    for edge in tobacco_graph.es:
        source_agency = int(tobacco_graph.vs[edge.source]['agency'])
        target_agency = int(tobacco_graph.vs[edge.target]['agency'])
        collab = edge['collab']
        if (source_agency, target_agency) not in collab_accumulator:
            collab_accumulator[(source_agency, target_agency)] = 0
        collab_accumulator[(source_agency, target_agency)] += collab

    # Add edges to the new graph
    for (source_agency, target_agency), collab in collab_accumulator.items():
        new_g.add_edge(source_agency, target_agency, collab=collab)

    return new_g


def agency_families_gpt(tobacco_graph):
    # Dictionary to store accumulated nodes by agency family
    new_g = ig.Graph(directed=tobacco_graph.is_directed())
    accumulated_nodes = {}

    # Iterate over nodes to accumulate by agency family id
    node_id = 0
    for node in tobacco_graph.vs:
        agency_family_id = int(node['agency'])
        agency_name = node['vertexnames'].split("-")[0]
        if agency_family_id not in accumulated_nodes:
            accumulated_nodes[agency_family_id] = []
            new_g.add_vertex(
                id=node_id,
                agency=agency_family_id,
                vertexnames=agency_name,
                collab_accumulated=0,  # Initialize accumulation for this agency family
                num_agencies=1  # Initialize number of agencies for this agency family
            )
            node_id += 1
        else:
            new_g.vs.find(agency=agency_family_id)['num_agencies'] += 1
        accumulated_nodes[agency_family_id].append(node.index)

    # Accumulate collab values for edges between agencies
    collab_accumulator = {}
    for edge in tobacco_graph.es:
        source_agency = int(tobacco_graph.vs[edge.source]['agency'])
        target_agency = int(tobacco_graph.vs[edge.target]['agency'])
        collab = edge['collab']
        if (source_agency, target_agency) not in collab_accumulator:
            collab_accumulator[(source_agency, target_agency)] = 0
        collab_accumulator[(source_agency, target_agency)] += collab

    # Add edges to the new graph
    for (source_agency, target_agency), collab in collab_accumulator.items():
        new_g.add_edge(source_agency, target_agency, collab=collab)

    # Accumulate collaboration for each node
    for node_id, node in enumerate(new_g.vs):
        agency_family_id = node['agency']
        collab_accumulated = sum([collab_accumulator.get((agency_family_id, neighbor), 0) for neighbor in new_g.neighbors(node_id)])
        node['collab_accumulated'] = collab_accumulated

    return new_g