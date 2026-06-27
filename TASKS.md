# TASKS.md — Task Progress Board

## Purpose

This file provides a single-page view of all active tasks — their current stage, owner, and next action. It bridges the gap between detailed planning documents in `task-plans/` and the three-phase completion checklist in `task-completion-checklist.md`.

Think of it as the team's sprint board in Markdown — lightweight, always current, maintained by AI.

## How to Use

This file is maintained by AI through conversation — **not manually edited**. Every time a task changes phase, status, or receives user confirmation, AI updates this board.

- Read this at the start of every session to know what's in flight
- Check the Blockers section before starting new work
- Move completed tasks to the Done table weekly
- This file is for progress tracking, not detailed plans — details live in `task-plans/`

## Phase Reference

Every task progresses through three phases defined in `task-completion-checklist.md`:

| Phase | Name | Meaning |
|-------|------|---------|
| **Phase 1** | Pre-completion | Requirements → Plan → Implementation → Verification |
| **Phase 2** | User Confirmation | Present results → Explain approach → Get explicit sign-off |
| **Phase 3** | Retrospective | Judge if retro is needed → Run retro if yes → Document lessons |

**Task Status:** A task can be `进行中` (in progress), `阻塞` (blocked), or `待确认` (awaiting confirmation).

## Active Tasks

| Task | Owner | Status | Started | Phase | Stage | Next Action |
|------|-------|--------|---------|-------|-------|-------------|
| 工作空间版本记录机制 | struggling-bird | 已完成 | 2026-05-26 | 阶段一 → 阶段二 → 阶段三 | 已归档 | 节点 1+2 均验收通过 |
| TEAM.md + TASKS.md 新增 | AI (ot-ops) | 进行中 | 2026-06-27 | 阶段一 | 方案设计 | 完成初稿 → 提交 owner review |

### Task Details

#### 工作空间版本记录机制

- **Plan:** `task-plans/2026-05-26-feature-refactor-version-records.md`
- **Phase 1 Status:**
  - `[x]` 需求明确（用户可读版本记录 + 校验接入）
  - `[x]` 方案已确认（CHANGELOG + docs + 校验脚本）
  - `[x]` 节点 1 实施完成并验收通过（版本记录资产与校验接入）
  - `[x]` 节点 2 实施完成并验收通过（版本迁移指南）
- **Phase 2 Status:** 全部确认（节点 1+2 均已验收）
- **Phase 3 Status:** 已归档

#### TEAM.md + TASKS.md 新增

- **Plan:** (待创建 task-plan)
- **Phase 1 Status:**
  - `[x]` 需求明确（团队花名册 + 任务进度板）
  - `[x]` 方案已确认（TEAM.md 参考 MEMORY 风格，TASKS.md 轻量表格驱动）
  - `[x]` 实施完成（两个文件已写入 repo 根目录）
  - `[ ]` 验证与 review
- **Phase 2 Status:** 待提交 owner 确认
- **Phase 3 Status:** 未启动

## Done This Week

| Task | Owner | Completed | Phase Reached | Notes |
|------|-------|-----------|---------------|-------|
| 工作空间版本记录机制 | struggling-bird | 2026-06-27 | 阶段三 | 节点 1（版本记录资产）+ 节点 2（迁移指南）均验收 |
| TEAM.md + TASKS.md 新增 | AI (ot-ops) | 2026-06-27 | 阶段一 | 两个文件已写入 repo 根目录，待 owner 确认 |

*(Previous weeks' completed tasks are archived to monthly summary on Sunday.)*

## Blockers

| Blocker | Affects | Since | Resolution Path |
|---------|---------|-------|-----------------|
| *(No active blockers)* | | | |

## Maintenance Rules

1. **Task created:** Add a row to Active Tasks with status `进行中` and Phase 1 entry
2. **Phase 1 checklist item completed:** Update the `[ ]` → `[x]` in Task Details; advance Stage column
3. **Phase 2 (user confirmed):** Update Status to `待确认`, record confirmation in Task Details, then move to Phase 3 or mark as Done
4. **Task blocked:** Update Status to `阻塞`, add entry to Blockers table with affected task and resolution path
5. **Task completed:** Move row from Active Tasks to Done This Week; include the phase reached
6. **Weekly cleanup (Sunday):** Move Done This Week entries to a monthly archive; review Active Tasks for staleness (>14 days without update → flag to owner)
7. **Status stalemate (>7 days in `阻塞`):** AI escalates in next session with owner
8. **New task before reviewing board:** AI checks Blockers and Active Tasks for conflicts before creating new entries

### State Machine

```
[需求] → [方案] → [实施] → [验证] → [用户确认] → [复盘] → [归档]
  ↓        ↓        ↓        ↓          ↓          ↓
[阻塞]   [阻塞]   [阻塞]   [阻塞]    [待确认]   [免复盘]

任何阶段进入「阻塞」→ 记录到 Blockers 表
「用户确认」通过 → 判断是否需要复盘 → 执行复盘或免复盘 → 归档到 Done
```

---

*TASKS.md is part of the open-teams workspace. Paired with task-plans/ for detail and task-completion-checklist.md for phase rigor. Maintained by AI through conversation.*