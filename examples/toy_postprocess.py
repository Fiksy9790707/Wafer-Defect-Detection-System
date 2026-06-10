from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Detection:
    x1: float
    y1: float
    x2: float
    y2: float
    score: float
    label: str = "defect"


def shift_detection(box: Detection, *, offset_x: float, offset_y: float) -> Detection:
    return Detection(
        x1=box.x1 + offset_x,
        y1=box.y1 + offset_y,
        x2=box.x2 + offset_x,
        y2=box.y2 + offset_y,
        score=box.score,
        label=box.label,
    )


def iou(a: Detection, b: Detection) -> float:
    inter_x1 = max(a.x1, b.x1)
    inter_y1 = max(a.y1, b.y1)
    inter_x2 = min(a.x2, b.x2)
    inter_y2 = min(a.y2, b.y2)
    inter_w = max(0.0, inter_x2 - inter_x1)
    inter_h = max(0.0, inter_y2 - inter_y1)
    intersection = inter_w * inter_h

    area_a = max(0.0, a.x2 - a.x1) * max(0.0, a.y2 - a.y1)
    area_b = max(0.0, b.x2 - b.x1) * max(0.0, b.y2 - b.y1)
    union = area_a + area_b - intersection
    return 0.0 if union == 0 else intersection / union


def nms(detections: list[Detection], *, iou_threshold: float = 0.45) -> list[Detection]:
    remaining = sorted(detections, key=lambda item: item.score, reverse=True)
    kept: list[Detection] = []

    while remaining:
        current = remaining.pop(0)
        kept.append(current)
        remaining = [
            item
            for item in remaining
            if item.label != current.label or iou(current, item) < iou_threshold
        ]

    return kept


def demo() -> None:
    tile_a = Detection(40, 35, 88, 80, 0.91)
    tile_b_duplicate = Detection(8, 35, 56, 80, 0.84)
    tile_c = Detection(120, 50, 146, 79, 0.77)

    merged = [
        shift_detection(tile_a, offset_x=0, offset_y=0),
        shift_detection(tile_b_duplicate, offset_x=32, offset_y=0),
        shift_detection(tile_c, offset_x=0, offset_y=0),
    ]

    print("Before NMS:")
    for item in merged:
        print(item)

    print("\nAfter NMS:")
    for item in nms(merged):
        print(item)


if __name__ == "__main__":
    demo()
