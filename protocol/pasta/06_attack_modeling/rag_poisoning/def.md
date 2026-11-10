# RAG Poisoning

Goal: make retrieval return wrong or no content for a question it should answer correctly.
No confirmed code finding yet — from the literature, needs verification against
`loader/vector_store.py` (chunking/reranking affects whether this works at all).

Try: upload a high-priority "blocker" document, or one with false facts for a specific query.

Success: demonstrably wrong or suppressed answer vs. a known-good baseline.
