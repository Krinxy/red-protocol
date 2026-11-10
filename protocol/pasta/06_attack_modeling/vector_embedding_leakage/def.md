# Vector/Embedding Leakage

Goal: extract knowledge-base content or confirm a document's presence without being allowed to
see it. No confirmed code finding yet — needs direct access to the Chroma config, not only via
the Chain API.

Try: repeated targeted questions for extraction, or answer-confidence for membership inference.

Success: reconstructed content, or a reliable membership claim, vs. a known baseline.
