def compute_pairs(m1, m2):
    """Computes a pairs from a 2 pairs of Square matrices.

    returns : sorted list of pairs.
    """

    size = m1.size
    edges = []
    matches = []

    for cursor in range(size):
        # Retrieve columns (first column from both matrices, second etc..)
        # This will create the of matches.
        pairs = m1.retrieve_column(cursor) + m2.retrieve_column(cursor)

        for pair in pairs:
            # If pair is in edges, check if it could be pair.
            if pair in edges:
                for match in matches:
                    # If there is a match in edges (a pair), but that pair
                    # is already taken previously (it exists in matches),
                    # we must remove it from the edges and skip it.
                    if match % 10 == pair % 10 or match // 10 == pair // 10:
                        edges = list(filter((pair).__ne__, edges))
                        break
                else:
                    # We found a pair. We must remove it from edges and add it
                    # to matches.
                    edges = list(filter((pair).__ne__, edges))

                    matches.append(pair)
            else:
                # Just add edge.
                edges.append(pair)

    return sorted(matches)
