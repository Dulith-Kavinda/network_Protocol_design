from __future__ import annotations

from typing import Any


def simulate_isis(topology) -> dict[str, Any]:
    """
    Lightweight IS-IS like link-state simulator approximation.
    Returns raw summary numbers.
    """
    node_count = len(topology.nodes)
    edge_count = len(topology.edges)

    # IS-IS is similar to OSPF in convergence characteristics in this simulator
    detection = 0.25
    flooding = 0.9 + edge_count * 0.02
    recomputation = 0.65 + node_count * 0.01
    stabilization = 0.25

    messages = max(1, int(edge_count * node_count * 0.6))
    affected_nodes = min(node_count, max(1, int(node_count * 0.5)))
    affected_edges = min(edge_count, max(1, int(edge_count * 0.5)))

    notes = [
        "IS-IS is a link-state protocol similar to OSPF; behavior approximated here.",
        "Efficient flooding and local recomputation retained.",
    ]

    return {
        "name": "IS-IS-like",
        "phases": {"detection": detection, "flooding": flooding, "recomputation": recomputation, "stabilization": stabilization},
        "messages": messages,
        "affected_nodes": affected_nodes,
        "affected_edges": affected_edges,
        "scope": "link-state (simulated)",
        "notes": notes,
    }
