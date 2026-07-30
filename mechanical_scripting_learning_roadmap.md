# Learning Mechanical Scripting — Roadmap for the Bolted-Connection Automation

## 0. Orientation — what you're actually learning

"Mechanical scripting" = the built-in **Scripting** view inside Ansys Mechanical
(Automation tab → Scripting). Historically IronPython, newer releases are adding native
Python support. It exposes the same object model as PyMechanical: `Model`, `DataModel`,
`Model.Connections`, `Model.NamedSelections`, `ExtAPI`, etc.

**Practical consequence for you:** learn using PyMechanical's *embedded* mode on any
machine with a licensed Mechanical install (even your own laptop once you get access) —
write and test there, where you get real Python error messages and can iterate fast in
a normal script/notebook. Once a block works, strip the `from ansys.mechanical.core
import App` / `App(globals=globals())` lines and paste the rest directly into
Mechanical's Scripting pane. This is an explicitly supported workflow, not a hack.

## 1. Free resources, roughly in the order to use them

| Resource | What it's good for |
|---|---|
| **Ansys Developer Portal — "Scripting for Mechanical Engineers"** (developer.ansys.com/blog/scripting-mechanical-engineers) | The best first read — untangles the buzzword soup (ACT, PyAnsys, DPF, Python Objects) and tells you what's actually relevant to you |
| **Scripting in Mechanical Guide** (official PDF via Ansys Help, search "Scripting in Mechanical Guide") | The canonical reference for the object model, tree navigation, looping patterns |
| **PyMechanical embedding examples gallery** (mechanical.docs.pyansys.com → Examples → Basic examples: Embedding mode) | Full worked, runnable examples — **the "Bolt pretension" example is almost exactly your Steps 5–7**: contact setup, `ContactFormulation`, bolt pretension load, preload values |
| **PyMechanical/Mechanical API stubs** (scripting.mechanical.docs.pyansys.com) | Searchable reference for every class/property — use this when you know roughly what you want (e.g. "beam connection") and need the exact property names |
| **LEAP Australia free training** ("Free Training: Scripting for Ansys Mechanical" on their blog) | Recorded 2-day intro course, good if you prefer video over docs |
| **"Automate the Boring Stuff in Ansys Mechanical"** (community tutorial site) | Practical IronPython-specific quirks (the `clr` module, .NET interop) that official docs gloss over |
| **Ansys Learning Forum / Innovation Space** | For when you're stuck on something specific — active community, Ansys staff participate |

## 2. Staged build plan, mapped to your spec

Don't try to write the whole script at once — each stage below is a runnable milestone.

### Stage A — Read-only tree navigation (learn the shape of the data)
Goal: get comfortable with `Model`, `DataModel`, looping, and printing — before changing
anything.
```python
model = app.Model  # or just `Model` if using globals injection
connections = model.Connections
for c in connections.Children:
    print(c.Name, c.DataModelObjectCategory)
```
This alone teaches you the tree structure your later steps depend on.

### Stage B — Step 2/3: bulk contact type changes
Loop over existing auto-detected contact regions and set `.ContactType`. This is where
you'll learn the `ContactRegion` object and enums (`ContactType.Bonded`,
`ContactType.Frictionless`, `ContactType.Frictional`).

**Design decision worth making before coding, not after:** distinguishing "contacts with
bolt holes" from "contacts without" by pure geometry (detecting circular edges of a
given diameter) is a real geometry-processing problem, not a quick scripting one. A far
more learnable first version: rely on **named selections** your CAD/mesh setup already
creates (or that you add manually as a convention) to mark which contact pairs are
bolted, and script against those names. You can graduate to geometric hole-detection
later once the simpler version works end-to-end.

### Stage C — Step 5: frictional contact settings
This is directly modeled by the Bolt Pretension example: setting
`FrictionCoefficient`, `ContactFormulation.AugmentedLagrange`, and stiffness/update
settings on a `ContactRegion`. Copy that example's `advanced_contact_settings()`
pattern almost verbatim as your starting point.

### Stage D — Step 6: idealized bolts as beam connections
`Model.Connections` has an `AddBeam()`-style method for exactly this (beam connecting
two faces/named selections, with reference/mobile scoping and a radius). This is the
one place I'd explicitly recommend searching the API stubs site for the current exact
property names (reference/mobile location, pinball scoping, radius) rather than trusting
any single example verbatim — beam connection property names have shifted across
releases, so confirm against your installed version's docs once you have access.

### Stage E — Step 7: bolt preload
The Bolt Pretension example again is your template — `AddBoltPretension()` on the
analysis, then setting the preload value. Computing preload as a fraction of yield
(cross-sectional area × yield strength × 2/3) is just Python arithmetic feeding into
that same API call — no new Ansys concept needed here, just wiring your formula's
output into `bolt_presentation.Preload...`.

### Stage F — Wrap it into your requested workflow shape
Only after A–E work individually: add the "stop here" option (a simple input/prompt or
a script parameter) between Steps 4 and 5, and make friction coefficient, pinball
multiplier, and preload fraction into named variables at the top of the script rather
than hardcoded — since you flagged all three as "things a user might want to change."

## 3. Where free learning will *not* fully get you there

Be honest with the stakeholder meeting about this one: **programmatically detecting
"which contacts have bolt holes larger than M4" from geometry alone** is the hardest
single piece of this spec, and it's more of a CAD-geometry-processing problem than a
"learn Mechanical scripting" problem. The tutorials/examples above will teach you
everything about *acting on* a contact or hole once identified — very few free resources
cover robust automatic hole-size detection from arbitrary geometry. Flagging this early
lets you propose the named-selection-convention approach (Stage B's note) as the
practical Phase 1 scope, with true geometric auto-detection as a stretch goal.
