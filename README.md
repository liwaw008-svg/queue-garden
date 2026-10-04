# Queue Garden

## The line is part of the decision

A community desk can publish fair criteria and still reorder people invisibly. Queue Garden makes the line itself inspectable. A steward opens a bounded service window, names an independent reviewer, and freezes both a public policy and an ordered rule list. Applicants plant separately hosted request records.

The reviewer triggers GenLayer consensus. Validators fetch policy and request bytes, preserve both digests, partition every rule, and return only `BLOOM`, `STANDARD`, or `WAITLIST`. A blocker can never produce an eligible priority. The steward's `serve_next` call cannot choose a favorite: contract code selects the highest eligible priority, then the oldest filing sequence.

Waitlisted applicants get one same-authority revision. If the desk expires, anyone can close it and mark unfinished tickets honestly instead of leaving an apparently active queue.

## Greenhouse states

```text
FILED -> RANKED -> SERVED
      -> WAITLIST -> FILED (one revision)
OPEN desk -> CLOSED by permissionless expiry
```

## Check the roots

```text
genvm-lint contracts/contract.py
python -m pytest -q
cd frontend
npm install
npm run typecheck
npm run build
```

The demonstration policy and requests are operator-created fixtures. The app is not for medical, emergency, housing, legal, or other high-stakes triage.
