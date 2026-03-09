# Team Workflow

This document explains how your team should work together on this repository.

## Weekly Working Pattern

1. Break the project into small tasks.
2. Create one GitHub Issue per task.
3. Assign one teammate per issue.
4. Work on separate branches.
5. Open pull requests early.
6. Review and merge one small change at a time.

## Recommended Starting Split

- Member 1: Customer flow
- Member 2: Owner/admin flow
- Member 3: Core system flow, data structures, and integration

## Task Breakdown For Beginners

Use small task sizes like these:

- Create menu display function
- Validate customer name
- Validate phone number
- Add one food item to order
- Calculate order total
- Add owner password check
- Show confirmed orders
- Update README

Avoid assigning one huge task like `build the full system`.

## Branch Workflow

1. Start from updated `main`.
2. Create a task-specific branch.
3. Push the branch early so the team can see it.
4. Open a draft PR if the task is still in progress.
5. Convert the PR to ready-for-review when tested.

## Communication Rules

- Tell the team which issue you picked.
- Say when you start a task.
- Say when a PR is ready for review.
- Say immediately if you are blocked.

Good daily update example:

`I am working on issue #4 on branch feature/phone-validation. Local testing is passing. PR will be ready today.`

## Pull Request Size Rule

Keep PRs small enough that a teammate can review them in 10 to 15 minutes.

If a change feels too big, split it into two or more PRs.

## Merge Safety

- Do not merge your own PR without team visibility.
- Re-check changed files before merging.
- Make sure `main` still represents working code.
- If two PRs touch the same area, merge the simpler one first.

## Conflict Handling

If Git shows a merge conflict:

1. Pull the latest `main`.
2. Merge or rebase `main` into your branch.
3. Resolve conflicts carefully.
4. Run the project again.
5. Push the fixed branch.

If you do not understand the conflict, ask the teammate whose code overlaps.

## Minimum PR Checklist

- The code solves one clear task.
- The branch name matches the task.
- The commit messages are clear.
- The code was run or checked locally.
- The docs were updated if needed.

## First Milestone Suggestion

Build the project in this order:

1. Project structure and shared data model
2. Menu display and item selection
3. Customer validation
4. Order total and payment rule
5. Owner login
6. Owner menu management
7. Confirmed order review
8. Integration cleanup and documentation

## Team Decision Rule

If a change affects shared behavior, do not guess. Agree on it first in the issue, PR, or team chat.

Examples:

- data structure names
- function names
- shared validation rules
- owner password behavior

## What To Avoid

- Working directly on `main`
- Large unreviewed changes
- Silent changes to another teammate's module
- Vague PR titles
- Waiting until the last minute to integrate code
