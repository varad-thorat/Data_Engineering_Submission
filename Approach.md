# Approach & Design Decisions

## Data Modeling
Each person is modelled as a `Person` object storing `name`, `gender`, `spouse`, `mother`, `father`, and `children`. Relationships are stored as direct object references rather than names, allowing efficient traversal without repeated lookups.

## Data Structure
A dictionary `{name: Person}` is used in `FamilyTree` to store all members, giving O(1) lookup by name. This is critical for `GET_RELATIONSHIP` and `ADD_CHILD` where we frequently search by name.

## OOP Design
Two classes keep responsibilities separate:
- `Person` — represents a single family member
- `FamilyTree` — manages the tree and all operations

Each relationship is its own method (e.g. `maternal_aunt`, `siblings`), making the code easy to read, test, and extend with new relationships in the future.

## ADD_CHILD
Validates three conditions before adding:
1. Mother exists in the tree
2. Mother is Female
3. Mother has a spouse (to assign as father)

## GET_RELATIONSHIP
Looks up the person, then delegates to the appropriate relationship method. Each method returns `NONE` if no results are found, or the relevant error message if the person doesn't exist.

## Extensibility
Adding a new relationship requires only:
1. A new method on `FamilyTree`
2. A new `elif` in `get_relationship`

No other code needs to change.

## Assumptions
- Children can only be added through the mother
- Names are case-sensitive
- Every child has both a mother and father (no single parents)
- No persistence required — tree is initialised fresh on each run
