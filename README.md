# Queue Garden

## The line is part of the decision

A community desk can publish fair criteria and still reorder people invisibly. Queue Garden makes the line itself inspectable. A steward opens a bounded service window, names an independent reviewer, and freezes both a public policy and an ordered rule list. Applicants plant separately hosted request records.

The reviewer triggers GenLayer consensus. Validators fetch policy and request bytes, preserve both digests, partition every rule, and return only `BLOOM`, `STANDARD`, or `WAITLIST`. A blocker can never produce an eligible priority. The steward's `serve_next` call cannot choose a favorite: contract code selects the highest eligible priority, then the oldest filing sequence.

Waitlisted applicants get one same-authority revision. If the desk expires, anyone can close it and mark unfinished tickets honestly instead of leaving an apparently active queue.

## Live service window

App: https://queue-garden.pages.dev/

The StudioNet contract is `0xa19768D05bE8b4B7A4981699cF4c6e78Da22D343`, deployed by transaction `0x44a07a36f68d56acba3654597040f52a2ca52a3245b36f01d7990c45236e4f01`. The live garden `GARDEN-1791125017` remains open for new requests. Its recorded demo ticket, `PRINT-1791125017`, was independently ranked `BLOOM` and served by transaction `0x8805ac0187375f1bfc7209425809bb1d26c9a664fe56e7ab44396c2222172efc`.

The paper-ticket interface supports applicant filing, reviewer ranking, and deterministic steward service. It reports submission separately from finalization and refreshes the visible queue only after a finalized receipt.

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

Exact deployment and lifecycle receipts are recorded in `deployment.json` and `network-run.json`.
