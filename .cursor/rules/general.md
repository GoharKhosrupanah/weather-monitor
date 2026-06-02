# Project Rules for Weather Monitor

- Always use UTC datetimes.
- When polling fails, log the city name and error but do NOT crash the poller.
- Event detection must be thoughtful: combine absolute thresholds + contextual changes.
- Keep API responses clean and consistent with the exact contract.
- Use meaningful variable names and add comments for complex logic.
- Deduplication is critical - never store duplicate readings for the same city+timestamp.