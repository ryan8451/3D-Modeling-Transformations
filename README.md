#  3D Articulated Model Viewer  
*By Ryan Chen with Thomas Quan* as a collaborator

<!-- ![Model Viewer Screenshot](./demo.png)  
*(Replace with your actual screenshot)* -->

##  Features
- **Full joint control** with rotation constraints
- **5 preset poses** (Trigger with 1-5 keys)
- **Multi-select joints** for coordinated movement
- **Real-time OpenGL rendering**
- **Interactive camera controls**

##  Installation
```bash
# 1. Create conda environment
conda env create -n graphics -f environment.yml

# 2. Activate environment
conda activate graphics

# 3. Run the viewer
python Sketch.py
```

##  Controls
###  Keyboard Shortcuts
| Key          | Action                          |
|--------------|---------------------------------|
| `1-5`        | Load preset poses               |
| `Enter`      | Cycle through components        |
| `←`/`→`      | Switch rotation axis (X/Y/Z)    |
| `↑`/`↓`      | Rotate selected joint(s)        |
| `m`          | Toggle multi-selection mode     |
| `S`          | Print current joint angles      |
| `R`          | Reset all rotations             |
| `r`          | Reset camera                    |
| `ESC`        | Clear selection                 |

###  Mouse Controls
| Action               | Function                     |
|----------------------|------------------------------|
| **Left Drag**        | Orbit camera                 |
| **Middle Drag**      | Pan camera                   |
| **Scroll Wheel**     | Zoom in/out                  |

##  Model Hierarchy
```
Root
├── Head
│   ├── Eyes
│   └── Ears
├── Torso
├── Arms
│   ├── Shoulders
│   ├── Elbows
│   └── Hands (with fingers)
└── Legs
    ├── Hips
    ├── Knees
    └── Feet
```

##  Code Structure
```plaintext
src/
├── Sketch.py            # Main viewer/controller
├── ModelLinkage.py      # Model definition
├── Component.py         # Base component class
├── GLUtility.py         # OpenGL helpers
└── environment.yml      # Dependencies
```

##  Preset Poses
1. **X Pose** - Arms and legs outstretched  
   *Key: 1*
2. **Hug Pose** - Arms crossed in front  
   *Key: 2*
3. **Ballet Pose** - One leg extended  
   *Key: 3*
4. **Wave Pose** - One arm raised  
   *Key: 4*
5. **V Pose** - Arms/legs in V formation  
   *Key: 5*

##  Known Issues
```diff
- Multi-select/single-select mode switching has conflicts
- Some joint constraints need refinement
- Camera sensitivity varies by input device
```

##  Academic Note
*Original framework by micou (Zezhou Sun).*  
*Model implementation and pose system developed by Ryan Chen for CASCS480 Assignment 2.*

**Key Contributions:**
- Implemented hierarchical joint system
- Developed pose preset functionality
- Added multi-selection interface
- Enforced joint rotation constraints