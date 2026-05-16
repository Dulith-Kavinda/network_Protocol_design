from __future__ import annotations

from typing import Any


def simulate_bgp(topology) -> dict[str, Any]:
    """
    Lightweight BGP-like simulator (path-vector behavior approximation).
    Returns a raw dict of summary numbers (no ProtocolResult class to avoid circular imports).
    """
    node_count = len(topology.nodes)
    edge_count = len(topology.edges)

    # heuristics: BGP tends to be slower to converge and uses fewer control messages
    detection = 0.8
    flooding = 1.8 + edge_count * 0.04
    recomputation = 1.6 + node_count * 0.03
    stabilization = 1.0

    messages = max(1, int(edge_count * node_count * 0.15))
    affected_nodes = min(node_count, max(1, int(node_count * 0.6)))
    affected_edges = min(edge_count, max(1, int(edge_count * 0.5)))

    notes = [
        "Path-vector semantics simulated: policy and path attributes not modeled in detail.",
        "Slower convergence but policy-aware in real deployments.",
    ]

    return {
        "name": "BGP-like",
        "phases": {"detection": detection, "flooding": flooding, "recomputation": recomputation, "stabilization": stabilization},
        "messages": messages,
        "affected_nodes": affected_nodes,
        "affected_edges": affected_edges,
        "scope": "inter-domain / path-vector (simulated)",
        "notes": notes,
    }
