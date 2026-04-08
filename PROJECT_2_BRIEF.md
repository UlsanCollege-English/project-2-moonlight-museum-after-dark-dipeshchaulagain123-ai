# Project 2: Moonlight Museum After Dark

**Course:** Data Structures (Python)  
**Due:** **2026-04-29 at 11:59 PM**  
**Team size:** 3-4 students  
**Allowed tools:** Python 3.11+, stdlib only  
**Graded artifacts:** `.py` code + `pytest` tests + `README.md`

---

## Story
The Moonlight Museum is preparing a secret late-night exhibition of strange objects: cursed mirrors, clockwork birds, whispering maps, glowing keys, and other odd artifacts.

Your team will build a museum system that helps the staff:

- organize strange artifacts
- search the archive quickly
- process restoration requests
- manage an exhibit route
- undo recent mistakes
- generate useful reports

This project is designed to use **all major course skills up to Week 6**.

---

## Learning goals
By completing this project, your team should demonstrate that it can:

- design and implement classes and helper functions in Python
- choose appropriate data structures for different jobs
- use recursion for tree traversal and BST logic
- use stacks, queues, linked lists, dicts, sets, searching, and sorting appropriately
- write meaningful tests with normal cases and edge cases
- explain complexity and design choices clearly in a README

---

## Required repo structure

```text
README.md
src/project.py
tests/test_project.py
```

You may add extra files if needed, but the three files above must exist.

---

## Required features
Your system must include **all** of the following.

### 1) Artifact archive BST
Create an `Artifact` record/class with these fields:

- `artifact_id: int`
- `name: str`
- `category: str`
- `age: int`
- `room: str`

Create an `ArtifactBST` that stores artifacts by `artifact_id`.

Required public behavior:
- insert an artifact
- search for an artifact by ID
- produce preorder, inorder, and postorder traversal output as Python lists of IDs

Required edge cases:
- insert into an empty tree
- search for a missing ID
- traversals on an empty tree
- duplicate IDs

**Duplicate policy for this project:** if the team tries to insert a duplicate `artifact_id`, the BST should **ignore it** and return `False`.

---

### 2) Restoration request queue
Create a `RestorationQueue` using `collections.deque` internally.

Required public behavior:
- add a request
- process the next request
- peek at the next request
- check whether the queue is empty
- report the size

Required edge cases:
- processing an empty queue
- peeking at an empty queue

---

### 3) Archive undo stack
Create an `ArchiveUndoStack` using a Python list internally.

Required public behavior:
- push an action
- undo the most recent action
- peek at the most recent action
- check whether the stack is empty
- report the size

Required edge cases:
- undo on an empty stack
- peek on an empty stack

---

### 4) Exhibit route linked list
Create a **singly linked list** for the guided exhibit route.

Required public behavior:
- add a stop to the end
- remove the first matching stop
- list all stops in order
- count the stops

Required edge cases:
- empty route
- missing stop
- remove first node
- remove middle node
- remove last node
- route with one stop

---

### 5) Museum reports and utility tools
Implement all of the following helper functions:

- `count_artifacts_by_category(artifacts)` -> `dict[str, int]`
- `unique_rooms(artifacts)` -> `set[str]`
- `sort_artifacts_by_age(artifacts, descending=False)` -> `list[Artifact]`
- `linear_search_by_name(artifacts, name)` -> `Artifact | None`

Required edge cases:
- empty artifact list
- repeated categories
- repeated rooms
- missing artifact name
- artifacts with the same age

---

### 6) One integration demo function
Your project must include:

```python
def demo_museum_night() -> None:
    ...
```

This function should show the system working together.

Your demo must:
- create at least 8 artifacts
- add them to the BST
- show at least one traversal result
- search for one existing and one missing ID
- add and process restoration requests
- push and undo archive actions
- build and print an exhibit route
- print category counts and unique rooms

This does **not** need to be a full interactive menu.

---

## README requirements
Your `README.md` must include all of the following sections:

1. Team information
2. Short project summary
3. Feature checklist
4. Design note (150-250 words)
5. Complexity reasoning
6. Edge-case checklist
7. Demo plan / how to run
8. Assistance & sources

---

## Testing requirements
Your `tests/test_project.py` must include:

- tests for all major public features
- at least one empty-case test for each structure
- duplicate-ID BST test
- linked-list removal tests
- queue FIFO tests
- stack LIFO tests
- report/helper tests

Do not write only "function exists" tests. Your tests must check **behavior**.

---

## Grading focus
This project is balanced. Strong work will show:

- correct behavior
- appropriate data structure choices
- clean organization
- meaningful tests
- clear reasoning in the README
- a demo that proves the system works together

---

## Submission notes
- Use stdlib only.
- Notebooks are allowed for practice, but they are **not graded**.
- Push your final code and tests to your team repo before the deadline.
- Make sure `pytest -q` runs successfully.

---

## Suggested work plan
### Week 6
- set up repo
- assign team roles
- agree on artifact theme details
- build class skeletons

### Week 7
- finish BST, queue, stack, and linked list core behavior
- begin tests

### Week 8 (midterm week)
- keep progress alive with small check-ins
- improve tests and README sections

### Final week for this project
- finish demo function
- review edge cases
- clean up README
- run tests one more time
