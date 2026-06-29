# 工作空间版本记录机制 — 变更历史

- **任务类型：** feature-refactor
- **日期：** 2026-05-26 — 2026-06-27
- **项目：** open-teams
- **计划文档：** `task-plans/2026-05-26-feature-refactor-version-records.md`

## 背景

在已有 `workspace-version.yaml`（偏机器可读）和 `change-history/`（偏任务过程）的基础上，需要补齐面向用户的版本说明入口，让使用者能直接感知每个模板版本的变化。

## 节点 1：版本记录资产与校验接入（2026-05-26）

### 实施内容
- 新增 `CHANGELOG.md` 作为用户可读版本记录
- 新增 `docs/development-specs/workspace-versioning.md` 说明版本号规则和记录关系
- 更新 `workspace-version.yaml` 补充版本记录路径和当前版本说明
- 更新 `README.md`、`docs/development-specs/README.md`、`workspace-assets-index.md` 补充版本记录入口
- 更新 `scripts/validate_template_layout.py` 检查版本记录资产存在

### 验证
- 模板校验通过
- 删除 CHANGELOG.md 后校验脚本正确报错

## 节点 2：版本迁移指南（2026-06-27）

### 实施内容
- 新增 `docs/development-specs/workspace-migration-guide.md`，覆盖：
  - 版本体系速览（MAJOR/MINOR/PATCH 风险分级）
  - 升级前检查（版本确认 + 本地定制盘点）
  - 三步标准升级流程（触发检查 → 确认方案 → 逐节点验收）
  - 3 个常见迁移场景（v0.4.2→v0.4.3 / v0.4.3→v0.4.4 / v0.3→v0.4）
  - 本地定制保护矩阵（12 个文件/目录的保护级别）
  - 故障回退（git stash / reset / revert + 预防措施）
  - FAQ（fork 升级、跳跃升级、按能力粒度升级）
- 更新 `docs/development-specs/README.md` 添加入口链接
- 更新 `task-plans/` 和 `TASKS.md` 标记任务完成

### 验证
- 模板校验通过
- README 入口链接可跳转

## 复盘

免复盘。理由：纯文档任务，无代码变更，无生产影响。内容已通过模板校验和入口链接验证。

## 资料同步

| 资产 | 是否同步 | 说明 |
|------|---------|------|
| `docs/` | ✅ | 新增 development-specs 文件，已更新 README 入口 |
| `skills/` | N/A | 无 Skill 变更 |
| `references/` | N/A | 无参考材料变更 |
| `change-history/` | ✅ | 本文档 |