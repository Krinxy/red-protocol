# Authorization Bypass

Goal: get access that should require a specific role, without having it. `user_roles` comes raw
from the client body on both APIs, no session check (AUTHZ-001/003).

Try: `POST /call_llm` with `"user_roles": ["admin"]`, no login; or hit the Loader API's
debug/admin endpoints directly.

Success: access that would be denied without the forged role.
