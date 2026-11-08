# CorridorKey 2.0 + Transparent MOV: six-node bundle

This upload bundle registers exactly the six node IDs required by
`CorridorKey2_Transparent_MOV.json`:

- `CorridorKey2Advanced`
- `CorridorKey2ChromaHint`
- `CorridorKey2Despill`
- `CorridorKey2MatteRefine`
- `CorridorKey2ModelLoader`
- `SaveTransparentVideo`

Drop the ZIP into the ComfyUI build/custom-node upload area. The ZIP does not
contain model weights. With `auto_download` enabled, the model loader downloads
the CorridorKey 2.0 assets (about 5.1 GB) into the ComfyUI server's model
storage on first use.

The CorridorKey integration is sourced from
https://github.com/marawan206/ComfyUI-CorridorKey2.0 and keeps its original
`LICENSE` and `THIRD_PARTY_NOTICES.md` files. The transparent saver is adapted
from https://github.com/TrentHunter82/TrentNodes and its MIT licence is retained
as `TRENTNODES_LICENSE`.

The saver supports multiple formats because that is how the upstream node is
defined. The supplied workflow selects `mov_prores4444` and is the only output
node in that workflow.
