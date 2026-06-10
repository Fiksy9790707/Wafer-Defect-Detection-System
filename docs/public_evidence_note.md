# Public Evidence Note

This repository is a public portfolio case study for a wafer / chip defect detection prototype. The original implementation involved private industrial images and internal workflow details, so the public repository intentionally avoids releasing private source code, datasets, model weights, or production validation information.

## What Can Be Publicly Demonstrated

The repository can safely show:

- High-level architecture and workflow diagrams.
- UI direction and portfolio screenshots.
- Dependency and deployment direction.
- Sanitized toy examples of generic post-processing ideas.

## Toy Post-Processing Example

`examples/toy_postprocess.py` demonstrates a small, synthetic version of two ideas used in many tiled object-detection workflows:

1. shifting tile-local detection boxes back into image-level coordinates;
2. applying non-maximum suppression to remove duplicate boxes from overlapping tiles.

This file does not use private data, company images, model weights, or proprietary code. It is only a minimal public illustration of the post-processing concept.

## What Is Not Claimed

The public toy example does not prove production accuracy, industrial robustness, or model performance metrics. Any metrics should only be published later if they can be reproduced with public data or clearly documented sanitized samples.
