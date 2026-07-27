# SOP Writing Standard

**Owner:** PM · Joel accountable · **Trigger:** A new SOP is needed, or an existing one is revised · **Cadence:** As needed; all SOPs reviewed quarterly · **Last reviewed:** 2026-07-26

## Purpose

Every SOP in this OS looks the same, so a contractor learns the shape once and can
then read any of them at speed. Consistency of form is what makes a body of
documents feel like a system rather than a folder.

What breaks without it: documents drift in format, people stop knowing where to
look for decision rights, and the OS becomes a place where information is stored
rather than found.

## When an SOP is warranted

Write one when **all three** are true:

1. It happens more than once
2. Getting it wrong costs real money, time, or a relationship
3. Someone other than the author will do it

If any is false, it is a checklist item or a note, not an SOP. **The most common
failure mode of an operations OS is documenting things that never needed
documenting**, which buries the documents that mattered.

A useful trigger: the third time someone asks the same question, write the SOP.

## The required header

Every SOP starts with exactly this:

```markdown
# [Name]

**Owner:** [role] · **Trigger:** [what starts this] · **Cadence:** [when] · **Last reviewed:** [YYYY-MM-DD]
```

**Owner is a role, never a person.** People change; roles persist. "Owner: Joel"
is acceptable only because Joel is the Principal role.

## The required sections, in order

### Purpose
One paragraph. **What breaks if this does not happen** — not what the document is
about. The reader needs the stake, not a summary.

### Steps
Numbered, imperative, executable. The test: **can someone new do this without
asking a question?** If not, rewrite it.
- Checklists for anything performed repeatedly
- Prose only for the "why"
- Name the tool, the field, the exact wording where exactness matters

### Decision rights
- Who decides alone
- What escalates, and at what threshold
- Thresholds are numbers, not adjectives. "Significant" is not a threshold.

### Definition of done
How you know it worked. Observable, not a feeling.

### Related
Links to other OS documents. Relative paths that actually resolve.

### Assumptions
Anything inferred rather than told. **This section is not optional and is rarely
empty.** It is what lets a wrong assumption be corrected in a minute rather than
discovered in a quarter.

## Writing rules

- **Specific over generic.** "Follow up promptly" is useless. "Day 2: value-add
  reply referencing their stated constraint; Day 5: case study; Day 12: breakup" is
  an SOP.
- **Delete any sentence that would survive being about a different company.** If it
  would read identically for a dental practice, cut it.
- **No filler.** Nothing about fast-paced landscapes.
- **Numbers, not adjectives.** "Two revision rounds", "$500", "5 business days".
- **Say the uncomfortable part.** The SOP that omits "this is why we stop work" is
  the one nobody follows under pressure.
- **One source of truth per fact.** If payment terms appear in four documents, three
  of them link to `../03-finance/invoicing-policy.md` instead of restating.

## Reviewing

- Every SOP is reviewed **quarterly**; bump `Last reviewed` even when unchanged
- An SOP not followed twice is wrong — fix the SOP, do not blame the person
- An SOP nobody has read in six months is a candidate for deletion

**A stale OS is worse than no OS**, because people follow it out of habit after it
stopped describing reality.

## Decision rights

- **PM decides alone:** writing a new SOP, editing an existing one for clarity.
- **Joel decides alone:** anything that changes a policy, threshold, or price.
- **Escalate when:** an SOP contradicts another. Both get fixed together, in one
  change, or the contradiction just moves.

## Definition of done

The SOP has the required header and all six sections, every link resolves, every
threshold is a number, and someone who has never done the task could execute it.

## Related

- [Knowledge base map](knowledge-base-map.md)
- [Decision log](decision-log.md)
- [Operating charter](../00-charter/operating-charter.md)

## Assumptions

- Assumes markdown files in a repo, edited in Obsidian or an editor. Consistent
  with the stated stack.
- **Assumes the PM archetype can write.** Not universally true across the four
  archetypes; Joel may need to edit, which is a real cost worth naming.
