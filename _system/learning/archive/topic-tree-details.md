# Archived topic-tree details

The former detailed topic tree was reduced on 2026-09-27. Its active routing
information remains in the canonical ROADMAP, milestone files, and curriculum
files. This note preserves the ownership decision and the major cross-domain
edges that are easy to lose when the tree is used as a names-only map.

## Ownership

- `Mechatronics/ROADMAP.md` owns active status, deliverables, dependencies,
  keywords, safety, and evidence boundaries.
- `Mechatronics/milestones/*.md` owns acceptance criteria, project detail,
  landmines, and evidence links.
- `_system/learning/curriculum/*.md` owns concept state, review rows, problems,
  misconceptions, active resources, and usage events.
- `_system/learning/topic-tree.md` owns only hierarchy, cross-domain dependency
  edges, and pointers.

## Load-bearing cross-domain edges

- Math foundations feed physics, controls, numerical methods, and simulation.
- Vectors/frames feed statics, kinematics, dynamics, and robot motion.
- Circuit laws and measurement discipline feed power electronics, sensing,
  actuation, and characterization.
- Conservation laws, energy, and uncertainty feed every physical artifact.
- Interface contracts and verification feed mechatronic integration.
- Japanese grammar/output/reading/immersion remain one coordinated language
  system; Anki owns vocabulary.

The detailed worked theory chains, repeated phase lists, and old review notes
were removed from the active tree rather than maintained as a second
curriculum. Git history and the milestone/curriculum files retain provenance.
