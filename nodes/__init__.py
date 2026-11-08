"""Node modules of the pack. Each module exposes a ``NODES`` list."""

import importlib
import importlib.util

_MODULES = (
    "model_nodes",
    "keyer_advanced",
    "refine_nodes",
    "hint_nodes",
    "save_transparent_video",
)

_REQUIRED_NODE_IDS = {
    "CorridorKey2Advanced",
    "CorridorKey2ChromaHint",
    "CorridorKey2Despill",
    "CorridorKey2MatteRefine",
    "CorridorKey2ModelLoader",
    "SaveTransparentVideo",
}


def all_nodes():
    nodes = []
    for name in _MODULES:
        if importlib.util.find_spec(f"{__name__}.{name}") is None:
            continue
        module = importlib.import_module(f"{__name__}.{name}")
        for node_class in module.NODES:
            if node_class.define_schema().node_id in _REQUIRED_NODE_IDS:
                nodes.append(node_class)
    return nodes
