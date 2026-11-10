# Resource Exhaustion / DoS

Goal: make the server keep consuming resources after the client has given up. No streaming to
abort — the issue is blocking calls and temp files that never get cleaned up.

Confirmed live (RE-001): `attack/modules/re001_disk_leak.py` — `/tmp` in the loader container
grows with every async upload and never shrinks.

Success: monotonic RAM/disk growth with no drop after abort, or LLM calls that keep running
after a client disconnect.
