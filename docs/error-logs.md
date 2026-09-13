# Error Log

This file records real errors encountered during development and testing,
along with their cause and resolution.

Errors are added here as they occur. This file is NOT pre-populated with
invented errors.

---

## Format

Each entry follows this structure:

```
Date/Time  :
Command    :
Error      :
Cause      :
Fix        :
Verified   :
```

---

## Entries

No development errors encountered during implementation.

All 92 automated tests passed on first run without any code fixes required.
The two warnings visible in the test output ("data/tasks.json is corrupted")
are expected — they are produced by the corrupted-JSON test cases correctly
triggering the application's own warning message. They are not errors.
