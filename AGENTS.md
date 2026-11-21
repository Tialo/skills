for pstack -> tstack migration:

* do small steps, I commit each step after a review manually
* if some steps require later work to fully migrate add notes to TODO.md, don't add it to changelog
* when removing/changing something please double check that other parts using relying on this are adapted: possible places are playbooks, guides, other skills
* run `python3 scripts/check-tstack.py` after changing tstack
* when changing, deleting a skill, add changelog entry
* a changelog entry describes how tstack differs from upstream pstack, not how the change was made
* its okay to change adpoted in INITIALIZATION.md