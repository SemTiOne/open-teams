# TASKS.md — Task Progress Board

轻量任务看板。只做索引，细节一律在 `task-plans/`。

## Why This, Not That

| 本文件存什么 | 不存什么（去 task-plans/） |
|-------------|--------------------------|
| 谁在做什么、卡在哪、下一步 | 完整方案、节点拆解、验收记录 |
| 一行 = 一个任务 | 一个任务 = 一个独立 plan 文件 |
| 本周归档快照 | 实施细节、验证结果 |

## Active Tasks

| Task | Owner | Status | Plan | Next Action |
|------|-------|--------|------|-------------|
| TEAM.md + TASKS.md 新增 | AI (ot-ops) | 待确认 | — | 老板审阅后确认收口 |

**Status:** `进行中` / `阻塞` / `待确认`

## Done This Week

| Task | Owner | Completed | Notes |
|------|-------|-----------|-------|
| 工作空间版本记录机制 | struggling-bird | 2026-06-27 | 节点 1+2 均验收，免复盘 → change-history |

*(周日归档到 monthly summary)*

## Blockers

| Blocker | Affects | Since | Resolution |
|---------|---------|-------|------------|
| — | | | |

## Maintenance

1. **任务创建** → Active Tasks 加一行，Status `进行中`。L1+ 任务创建 `task-plans/`。
2. **状态变更** → 更新 Status 列。阻塞加 Blockers 表。
3. **任务完成** → 移入 Done This Week，标注日期。
4. **周清理（周日）** → Done This Week 归档；检查 Active 中超 14 天无更新 → 标过期。
5. **阻塞 7 天** → 升级通知老板。

---

*细节去 `task-plans/`，流程看 `task-completion-checklist.md`。AI 通过对话维护。*