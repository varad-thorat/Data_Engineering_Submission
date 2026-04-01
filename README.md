# Glynac Data Engineer - Family Tree Challenge

A Python solution to model and query King Arthur's family tree.

## Requirements
- Python 3.x

## How to Run
```
python main.py input.txt
```

## Input Format
```
ADD_CHILD <Mother's-Name> <Child's-Name> <Gender>
GET_RELATIONSHIP <Name> <Relationship>
```

## Supported Relationships
`Siblings`, `Son`, `Daughter`, `Maternal-Aunt`, `Paternal-Aunt`, `Maternal-Uncle`, `Paternal-Uncle`, `Sister-In-Law`, `Brother-In-Law`

## Output
- `CHILD_ADDED` — child successfully added
- `CHILD_ADDITION_FAILED` — mother is Male or has no spouse
- `PERSON_NOT_FOUND` — name does not exist in the tree
- `NONE` — no results found for the relationship

## Sample Input
```
ADD_CHILD Flora Minerva Female
GET_RELATIONSHIP Remus Maternal-Aunt
GET_RELATIONSHIP Minerva Siblings
```

## Sample Output
```
CHILD_ADDED
Dominique Minerva
Victoire Dominique Louis
```

## Assumptions
- Children can only be added through the mother
- Mother must exist, be Female, and have a spouse
- Names are case-sensitive
- No persistence — tree resets on each run
