for pstack -> tstack migration:

* do small steps, I commit each step after a review manually
* if some steps require later work to fully migrate add notes to TODO.md, don't add it to changelog
* when removing/changing something please double check that other parts using relying on this are adapted: possible places are playbooks, guides, other skills
* don't regenerate harness manually, it makes it harder to review changes
* when changing, deleting a skill, fix hierarchy file, add changelog entry, progress entry
