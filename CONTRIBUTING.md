# Contributing to food-ordering-system

This project is being built by a beginner team. The goal of this guide is to make collaboration predictable, safe, and easy to follow.

## Core Rules

- Never push unfinished work directly to `main`.
- One task = one branch = one pull request.
- Keep pull requests small and focused.
- Explain what changed and how you tested it.
- Ask for review before merging.

## Project Flow

1. Pick a task from GitHub Issues or agree on one with the team.
2. Fork the repository to your own GitHub account.
3. Clone your fork to your computer.
4. Create a new branch from the latest `main`.
5. Make your changes.
6. Test your changes locally.
7. Commit with a clear message.
8. Push the branch to your fork.
9. Open a pull request to `Abyssinia-Devs/food-ordering-system`.
10. Address review comments.
11. Merge only after approval.

## How to Fork

1. Open `https://github.com/Abyssinia-Devs/food-ordering-system`.
2. Click the `Fork` button on GitHub.
3. Create the fork under your own account.

## How to Clone Your Fork

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/food-ordering-system.git
cd food-ordering-system
git remote add upstream https://github.com/Abyssinia-Devs/food-ordering-system.git
git remote -v
```

`origin` should point to your fork. `upstream` should point to the team repository.

## How to Create a Branch

Always branch from updated `main`.

```bash
git checkout main
git pull upstream main
git checkout -b feature/short-task-name
```

Use one of these branch name patterns:

- `feature/add-order-validation`
- `fix/phone-number-check`
- `docs/update-readme`
- `test/add-payment-tests`

## How to Work on a Task

- Make one logical change at a time.
- Do not mix unrelated fixes in one branch.
- If you need help, ask before changing another teammate's area.
- Pull from `upstream/main` before starting a new task.

## How to Commit

Commit messages should be short, specific, and written in the imperative style.

Good examples:

- `Add phone number validation`
- `Fix menu total calculation`
- `Update owner workflow docs`

Avoid vague messages like:

- `update`
- `changes`
- `fix stuff`

Example:

```bash
git add .
git commit -m "Add cart review step"
```

## How to Push

```bash
git push origin feature/short-task-name
```

## How to Open a Pull Request

1. Go to your fork on GitHub.
2. Click `Compare & pull request`.
3. Set the base repository to `Abyssinia-Devs/food-ordering-system`.
4. Set the base branch to `main`.
5. Add a clear title and description.
6. Link the related issue if there is one.
7. Ask at least one teammate to review.

Your pull request should answer:

- What changed?
- Why was it needed?
- How was it tested?
- Are there any risks or unfinished parts?

## Review and Merge Rules

- At least one teammate should review before merge.
- The author should not merge without review unless the whole team agrees.
- Resolve all comments before merging.
- If the pull request changes behavior, test it again after updates.

## Keeping Your Fork Updated

```bash
git checkout main
git pull upstream main
git push origin main
```

If your branch is behind `main`, update it before opening or merging the pull request.

## Suggested Team Roles

- Member 1: User flow and input validation
- Member 2: Owner/admin flow
- Member 3: Core application flow and integration

These are ownership areas, not hard limits. Teammates can help each other, but major cross-module changes should be discussed first.

## Definition of Done

A task is done only when:

- The code works locally.
- The related README or docs are updated if behavior changed.
- The branch contains only task-related changes.
- The pull request description is complete.
- Another teammate has reviewed it.

## When You Are Stuck

Do this in order:

1. Re-read the issue or requirement.
2. Pull the latest `main`.
3. Check whether another teammate is already working on the same area.
4. Ask in the team chat and include your branch name, problem, and error message.

## First Team Recommendation

For your first few tasks, keep pull requests very small. Examples:

- Add a single validation rule
- Build one menu function
- Improve one screen/output
- Write one small test file

Small PRs are easier to review, merge, and debug.
