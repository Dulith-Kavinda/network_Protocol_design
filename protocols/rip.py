from __future__ import annotations

from typing import Any


def simulate_rip(topology) -> dict[str, Any]:
    """
    Lightweight RIP-like distance-vector simulator approximation.
    Returns raw summary numbers.
    """
    node_count = len(topology.nodes)
    edge_count = len(topology.edges)

    # RIP is slow due to periodic timers and count-to-infinity behavior
    detection = 1.2
    flooding = 0.6 + edge_count * 0.02
    recomputation = 2.4 + node_count * 0.05
    stabilization = 1.5

    messages = max(1, int(edge_count * node_count * 1.2))
    affected_nodes = min(node_count, max(1, int(node_count * 0.8)))
    affected_edges = min(edge_count, max(1, int(edge_count * 0.8)))

    notes = [
        "Distance-vector behavior approximated (hop-count based).",
        "Tends to be slower and can be less scalable in larger domains.",
    ]

    return {
        "name": "RIP-like",
        "phases": {"detection": detection, "flooding": flooding, "recomputation": recomputation, "stabilization": stabilization},
        "messages": messages,
        "affected_nodes": affected_nodes,
        "affected_edges": affected_edges,
        "scope": "distance-vector (simulated)",
        "notes": notes,
    }
