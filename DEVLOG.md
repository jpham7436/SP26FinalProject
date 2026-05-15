# Development Log – The Torchbearer

**Student Name:** Jason Pham
**Student ID:** 132526911

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/13/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

My plan is to go through each part one by one. I haven't read through all the parts yet, but the final seems to be set up in a specific order, especially since each part in Assignment.md has a corresponding section in README.md and torchbearer.py. I've just completed part 1.

Part 2 is an implementation of Dijkstra's Algorithm, so that shouldn't be too hard, especially since we are importing a prio queue. I plan to do that first. However, we need to find the shortest path from the start node to the end node while hitting all relic rooms at least once. This seems much harder, so I'll do that afterwards. I'm not exactly sure how to test the last part, but I guess I'll figure it out along the way lol. Maybe I'll just brute force it and compute the  total fuel required for every combination of relics starting at S and ending at T.

---

## Entry 2 – [5/14/2026]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

Completed parts 2 and 3, this is my 2nd commit after my initial commit to set up the project repo. This concludes the Dijkstra's portion of the final, will be moving onto the final planning and implementation part soon.

A bug I ran into was caused by not checking if the new calculated distance was < the previous distance stored in the dict. I made this mistake because previously, continue is called if current_dist > dist[current_node]. Because of this, I assumed that if the program didnt continue, then the current distance is 100% < dist[current_node].

---

## Entry 3 – [5/14/2026]: [Short description]

Completed parts 4-6 for both the README and the torchbearer.py file. This is the 3rd commit and final coding commit. I am going to review everything, delete all the comment blocks, and prepare for final submission now.

---

## Entry 4 – [5/14/2026]: Post-Implementation Reflection

Just removed all comment blocks, added some comments to explain code, and finalized the submission. 

Given more time, I wish I could find a way to optimize the explore function. I ended up optimizng the brute-force approach mentioned earlier by pruning unnecessary branches, but there has to be some actual algorithm that lets us find the optimal route without this optimized brute force technique.

---

## Final Entry – [Date]: Time Estimate

 - Note: these estimates are for how long I actually spent typing/coding. I'm not exactly sure how long it took to actually understand the project because it took me a long time for each section lol.

| Part | Estimated Minutes |
|---|---|
| Part 1: Problem Analysis | 10 |
| Part 2: Precomputation Design | 18 |
| Part 3: Algorithm Correctness | 5 |
| Part 4: Search Design | 8 |
| Part 5: State and Search Space | 15 |
| Part 6: Pruning | 20 |
| Part 7: Implementation | 20 |
| README and DEVLOG writing | 30 |
| **Total** | 126 minutes |
