# 3D Simulator

A small 3D wireframe renderer written from scratch in pure Python. It projects 3D quadrilaterals ("carrés") onto a 2D plane through a pinhole camera placed at the origin, handles occlusion between faces, and draws the result with Python's built-in `turtle` module. No third-party dependencies.

The code and comments are in French (`donne_...` = "gives ...").

## How it works

1. **Scene**: objects are built from `point`, `vecteur`, `ligne`, `plan` and `carre` (a quadrilateral face made of 4 points).
2. **Projection**: the camera sits at `(0, 0, 0)` looking along +Z. Each edge is projected onto the screen plane `z = 0.1` by intersecting the line camera → point with that plane.
3. **Hidden lines**: for each edge, the program checks which other faces intersect the line of sight and cuts/removes the hidden parts (`donne_ligne_transformer`).
4. **Drawing**: the visible segments are drawn with `turtle` (scaled by 50000) and the frame is refreshed with `turtle.update()`.
5. **Animation**: `carre.donne_rotation_carre(centre, alpha)` rotates a face around a point, which is used for the spinning demo.

## Files

| File | Description |
|------|-------------|
| `object_3d.py` / `definition_3d.py` | First version: basic classes and vector math (dot/cross product, distances, line-plane intersection, face occlusion). Static scene. |
| `object_3d_2.py` / `definition_3d_2.py` | Second version: classes with rotation methods, improved visibility computation and `turtle` rendering (`affichage_liste`). |
| `execution.py` | Demo for version 1: draws a square and a line cut by it. |
| `execution_2.py` | Demo for version 2: an animated, rotating 3D object made of 5 faces. |
| `test25.py` | Scratch test file. |

## Requirements

- Python 3.9+
- `tkinter` (needed by `turtle`; bundled with most Python installs, on Debian/Ubuntu: `sudo apt install python3-tk`)

## Usage

```bash
git clone https://github.com/mazaiez001/3d_simulator.git
cd 3d_simulator-main

python execution_2.py   # animated rotating object (version 2)
python execution.py     # static demo (version 1)
```

Close the turtle window or press `Ctrl+C` to stop the animation.

## Main API (version 2)

```python
from object_3d_2 import *
from definition_3d_2 import *

# a face from 4 points
face = carre(point(-3, 0.5, 25), point(3, 0.5, 25),
             point(3, -0.5, 25), point(-3, -0.5, 25))

# rotate it by an angle (radians) around a point
face.donne_rotation_carre(point(0, 5, 26), 0.3)

# render a list of faces (with hidden-line removal)
affichage_liste([face])
```

Useful helpers in `definition_3d_2.py`: `donne_vecteur`, `donne_produit_scalaire`, `donne_produit_vectoriel`, `donne_distance_entre_points`, `donne_inter_ligne_plan`, `donne_ver_point_dans_triangle`, `donne_intersection_ligne_carre`, `donne_ligne_transformer`.

## Notes

- Objects must lie in front of the camera (positive `z`).
- Rendering is CPU-only and slow for many faces; it is a learning project, not a production engine.
