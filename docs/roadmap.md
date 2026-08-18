# Mom's Canning Timer — Roadmap

Known gaps, observed from the code. Limitations, not a schedule. Concrete defects with
suggested fixes are in [`internal/known-issues.md`](./internal/known-issues.md).

## Gaps

**Nothing persists.** Timer state is in memory, so closing the window loses everything. For a
kitchen tool that is mostly fine, and it does mean an accidental close during a long process
cannot be recovered.

**Minutes only.** The input takes whole minutes, which suits canning and rules out anything
shorter.

**Four burners, fixed.** The 2x2 grid matches a stove top and is not configurable, so a fifth
concurrent timer is not possible.

**No labels.** Burners are positional, so remembering which is the tomatoes and which is the
beans is on you.

**Accuracy is event-loop bound.** Fine for a kitchen timer, not exact.

## Non-goals

- **Being a food-safety reference.** Processing times come from a recipe or a canning guide.
  This counts down; it does not advise.
- **Third-party dependencies.** Installing with no compiler and no network is a feature worth
  more than most things a dependency would buy.
- **Saving or syncing.** A timer that outlives the window is a different program.
