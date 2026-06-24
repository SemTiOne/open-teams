# Performance Review Rules

> These rules are checked during every code review. Flag violations with their severity level.

---

## 🔴 High (Likely Production Impact)

- **PERF-001:** N+1 query pattern — database queries inside loops. Use eager loading, batch queries, or data loaders.
- **PERF-002:** Missing database index on frequently queried columns (foreign keys, `WHERE` clauses, `ORDER BY` fields)
- **PERF-003:** Blocking I/O on the main/event loop in Node.js, Python asyncio, or similar — use async variants or offload to worker threads
- **PERF-004:** Unbounded queries without pagination or `LIMIT` — `SELECT * FROM large_table` will OOM under load

---

## 🟡 Medium (Degrades Under Load)

- **PERF-005:** Missing cache headers (`Cache-Control`, `ETag`) on static or infrequently-changing responses
- **PERF-006:** Large payload sizes — API responses >100KB without pagination or compression. Consider gzip/brotli and field filtering
- **PERF-007:** Repeated computation in hot paths — memoize or pre-compute values that don't change per-request
- **PERF-008:** Missing connection pooling for database clients — check pool `min`/`max` settings
- **PERF-009:** Synchronous heavy computation on request thread — CPU-intensive work (>50ms) should be queued or offloaded

---

## 🟢 Low (Optimization)

- **PERF-010:** Unnecessary re-renders in frontend code — missing `React.memo`, `useMemo`, or computed properties
- **PERF-011:** Large bundle sizes — imports pulling entire libraries when only one function is needed (e.g., `import _ from 'lodash'` → `import debounce from 'lodash/debounce'`)
- **PERF-012:** Images not optimized — no WebP/AVIF conversion, no responsive `srcset`, missing lazy loading
- **PERF-013:** Excessive API calls from frontend — consider batching requests or using a BFF (Backend For Frontend) pattern
- **PERF-014:** Missing debounce/throttle on user input handlers (search, resize, scroll)

---

## How to Add Team-Specific Rules

Add your own rules below using the same format:

```
- **PERF-XXX:** Rule description — guidance for fixing
```
