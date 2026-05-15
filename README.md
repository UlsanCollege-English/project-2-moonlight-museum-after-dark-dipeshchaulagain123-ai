# Project 2: Moonlight Museum After Dark

**Course:** Data Structures (Python)
**Team member:** Dipesh Chaulagain

---

## 1. Team Information

| Name | GitHub Username |
|------|----------------|
| Dipesh Chaulagain | dipeshchaulagain123-ai|

---

## 2. Project Summary

This project implements a museum management system for the Moonlight Museum's secret late-night exhibition. The system allows staff to organize strange artifacts, search the archive, process restoration requests, manage an exhibit route, undo recent mistakes, and generate reports. All six required features are fully implemented using appropriate data structures covered in the course up to Week 6.

---

## 3. Feature Checklist

- [x] **Artifact Archive BST** — insert, search by ID, inorder/preorder/postorder traversal, duplicate handling
- [x] **Restoration Request Queue** — add, process, peek, is_empty, size
- [x] **Archive Undo Stack** — push, undo, peek, is_empty, size
- [x] **Exhibit Route Linked List** — add stop, remove stop, list stops, count stops
- [x] **Museum Reports & Utilities** — count by category, unique rooms, sort by age, linear search by name
- [x] **Integration Demo** — `demo_museum_night()` showing all features working together

---

## 4. Design Note

The BST was chosen for the artifact archive because it allows efficient search, insert, and sorted traversal all in one structure. Artifacts are keyed by `artifact_id` (an integer), which makes BST comparison straightforward. Duplicate IDs are silently ignored and return `False`, which prevents accidental overwrites of real museum records.

The restoration queue uses `collections.deque` internally because deque provides O(1) append to the right and O(1) pop from the left, making it ideal for FIFO behavior. A plain Python list would work for `append`, but `list.pop(0)` is O(n) due to shifting — deque avoids this entirely.

The undo stack uses a plain Python list because list `append` and `pop` from the end are both O(1), which is exactly what a LIFO stack needs. No extra memory or wrapping is required.

The exhibit route uses a singly linked list because the route is traversed in order and stops can be inserted or removed without shifting elements. Each node holds a stop name and a pointer to the next node. Removal handles three cases: removing the head, a middle node, and the last node.

Helper functions use built-in Python tools: a dict for category counting, a set comprehension for unique rooms, `sorted()` with a lambda key for age sorting, and a simple loop for linear search.

---

## 5. Complexity Reasoning

| Operation | Data Structure | Time Complexity | Reason |
|-----------|---------------|-----------------|--------|
| BST insert | Binary Search Tree | O(h) average | Traverse left/right by ID comparison; h = height |
| BST search | Binary Search Tree | O(h) average | Same traversal logic as insert |
| BST traversal | Binary Search Tree | O(n) | Every node visited exactly once |
| Queue add / process | deque | O(1) | deque append/popleft are constant time |
| Stack push / undo | list | O(1) | list append/pop from end are constant time |
| Linked list add stop | Singly linked list | O(n) | Must walk to the end to append |
| Linked list remove stop | Singly linked list | O(n) | Must walk to find the matching node |
| Count by category | dict | O(n) | Single pass through artifact list |
| Unique rooms | set | O(n) | Single pass using set comprehension |
| Sort by age | sorted() | O(n log n) | Python's Timsort algorithm |
| Linear search by name | list | O(n) | Worst case checks every artifact |

> Note: BST height h = O(log n) for a balanced tree and O(n) worst case for a sorted insertion order.

---

## 6. Edge-Case Checklist

**BST:**
- [x] Insert into empty tree
- [x] Search in empty tree returns None
- [x] Search for missing ID returns None
- [x] Duplicate ID is ignored, returns False, original artifact preserved
- [x] All traversals on empty tree return empty lists

**Restoration Queue:**
- [x] Process on empty queue returns None
- [x] Peek on empty queue returns None
- [x] Peek does not remove the item
- [x] FIFO order confirmed across multiple requests

**Undo Stack:**
- [x] Undo on empty stack returns None
- [x] Peek on empty stack returns None
- [x] Peek does not remove the item
- [x] LIFO order confirmed across multiple actions

**Exhibit Route (Linked List):**
- [x] Empty route returns empty list and count 0
- [x] Remove from empty route returns False
- [x] Remove missing stop returns False
- [x] Remove first (head) node
- [x] Remove middle node
- [x] Remove last node
- [x] Remove only node leaves empty route

**Utility Functions:**
- [x] Empty artifact list returns empty dict / empty set / empty list / None
- [x] Repeated categories counted correctly
- [x] Repeated rooms deduplicated in set
- [x] Artifacts with the same age handled correctly by sort
- [x] Missing name in linear search returns None

---

## 7. Demo Plan / How to Run

### Run the full test suite

Make sure you are inside the project folder, then run:

```bash
python -m pytest -q
```

Expected output:
```
38 passed in 0.XX s
```

### Run the demo function

Open a Python shell from the project folder:

```bash
python -c "from src.project import demo_museum_night; demo_museum_night()"
```

The demo will print BST traversal results, search results, restoration queue processing, undo stack operations, exhibit route management, and category/room reports.

### Requirements

- Python 3.11 or higher
- No third-party packages required (stdlib only)
- `pytest` for running tests (`pip install pytest`)

---

## 8. Assistance & Sources

- Python official documentation: `collections.deque`, `dataclasses`, `sorted()`
- Course lecture notes and slides (Weeks 1–6)
- Project brief: `PROJECT_2_BRIEF.md`
- AI assistant (Claude by Anthropic) used to help implement and verify the code
