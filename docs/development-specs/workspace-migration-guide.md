# 工作空间版本迁移指南

从旧版 open-teams 模板升级到新版的操作手册。适用于已 clone 模板并在其上建立了业务项目的工作空间。

## 目录

1. [版本体系速览](#版本体系速览)
2. [升级前检查](#升级前检查)
3. [标准升级流程（三步）](#标准升级流程三步)
4. [常见迁移场景](#常见迁移场景)
5. [本地定制保护](#本地定制保护)
6. [故障回退](#故障回退)
7. [FAQ](#faq)

---

## 版本体系速览

open-teams 采用 `MAJOR.MINOR.PATCH` 版本号：

| 版本号变化 | 含义 | 迁移风险 |
|-----------|------|---------|
| `PATCH`（如 v0.4.2 → v0.4.3） | 文档修正、小范围缺陷修复 | 极低，通常可直接合并 |
| `MINOR`（如 v0.4 → v0.5） | 新增可选能力、workflow skill、模板资产 | 低，按需选择升级项 |
| `MAJOR`（如 v0.x → v1.0） | 目录结构、约束机制或不兼容变化 | 中高，需要完整升级流程 |

**关键原则：你不必追逐每个版本。** 升级是按能力粒度按需选择的，不是盲目覆盖。详见 [工作空间版本规则](./workspace-versioning.md)。

---

## 升级前检查

### 确认当前版本

```bash
cat workspace-config/workspace-version.yaml | head -5
```

或者直接问 AI：

```
"检查当前工作空间版本和已应用能力。"
```

### 确认本地定制

升级前先盘点你的工作空间中有哪些是模板文件、哪些是业务定制：

| 文件/目录 | 通常来源 | 升级时 |
|-----------|---------|--------|
| `AGENTS.md` | 业务定制 | **保护** |
| `MEMORY.md` | 业务定制 | **保护** |
| `TOOLS.md` | 业务定制 | **保护** |
| `workspace-config/code-sources.yaml` | 业务定制 | **保护** |
| `docs/projects/` | 业务定制 | **保护** |
| `skills/<project>/` | 业务定制 | **保护** |
| `skills/_workflow/` | 模板 | 可升级 |
| `skills/code-review/` | 模板 + 可定制 | 谨慎合并 |
| `skills/api-design-review/` | 模板 + 可定制 | 谨慎合并 |
| `docs/development-specs/` | 模板 | 可升级 |
| `scripts/` | 模板 | 可升级 |
| `CHANGELOG.md` | 模板 | 可升级 |

### 查看 CHANGELOG 了解差异

查看 [CHANGELOG.md](../../CHANGELOG.md) 了解当前版本和最新版本之间的差异。重点关注：

- **Added** — 你可能想启用的新能力
- **Changed** — 可能与你本地定制冲突的变更
- **Fixed** — Bug 修复，通常应该合并

---

## 标准升级流程（三步）

### Step 1：触发升级检查

用以下提示词让 AI 检查升级空间：

```
"检查当前工作空间是否需要升级到 open-teams 最新模板能力。

要求：
1. 先读取 workspace-assets-index.md、task-completion-checklist.md 和 workspace-config/workspace-version.yaml。
2. 识别当前工作空间类型、已应用能力、本地定制和潜在风险。
3. 只输出升级差异、可选升级项、推荐方案和风险，不要修改文件。
4. 等我确认方案后再进入实施。"
```

### Step 2：确认方案并生成计划

AI 输出方案后，审阅并确认。然后让 AI 生成可验收的实施计划：

```
"请基于刚才确认的升级方案，生成 task-plans/ 下的实施计划。

要求：
1. 按节点拆分升级内容，每个节点都要有目标、实施步骤、验证方式和验收标准。
2. 明确哪些本地定制不能覆盖。
3. 每个节点验收通过后，需要完成版本维护要求。
4. 计划文档落地后先提交给我确认；我未确认实施计划前不要开始改文件。"
```

### Step 3：逐节点实施与验收

AI 按节点逐步实施。每个节点完成后：

1. AI 输出验证结果
2. 你验收通过
3. AI 提交该节点相关的改动
4. 进入下一节点

**不要跳过节点验收直接全部改完。** 分批验收让问题更早暴露。

---

## 常见迁移场景

### 场景 1：v0.4.2 → v0.4.3（PATCH 升级）

**变更内容：** 首次会话初始化工作口令、契约维护原则、QUICKSTART 重写。

**迁移步骤：**

1. 更新 `workspace-config/workspace-version.yaml` 中的 `template.version` 到 `0.4.3`
2. 不需要修改 AGENTS.md / MEMORY.md（它们是你的业务定制，不是模板）
3. 如果有新成员加入，他们将从新版 QUICKSTART 中获得更好的初始化体验

**风险：** 无。

### 场景 2：v0.4.3 → v0.4.4（PATCH 升级）

**变更内容：** 治理文档全面重写（MEMORY.md 模板、架构/产品/项目入口）、Skill 成熟度加固（api-design-review、architecture-review 补齐 checklist+examples+rules）。

**迁移步骤：**

1. 更新 `workspace-config/workspace-version.yaml` 中的 `template.version` 到 `0.4.4`
2. 替换模板文件（保护你的本地定制）：
   - `skills/api-design-review/` — 替换 SKILL.md、新增 checklist.md/examples.md、合并 rules/
   - `skills/architecture-review/` — 同上
   - `skills/onboarding/SKILL.md` — 替换为模板骨架
   - `docs/overall-architecture/README.md` — 替换
   - `docs/product-knowledge/README.md` — 替换
   - `docs/projects/README.md` — 替换
3. **不替换：** `AGENTS.md`、`MEMORY.md`、`TOOLS.md`、`workspace-config/code-sources.yaml`
4. 对于 `MEMORY.md`，如果当前还是模板占位符，建议替换为新结构骨架

**风险：** 如果你自定义了 Skill rules（在 `rules/README.md` 底部），注意先备份再合并。

### 场景 3：v0.3.x → v0.4.x（MINOR 升级）

**变更内容：** 初始化脚本、CI 校验、Skill registry、versioning 体系。

**迁移步骤：**

1. 先运行空跑检查：

```bash
# 在新的临时目录 clone 最新模板，对比差异
git clone https://github.com/struggling-bird/open-teams.git /tmp/open-teams-latest
diff -rq . /tmp/open-teams-latest --exclude='.git' --exclude='sources' --exclude='AGENTS.md' --exclude='MEMORY.md' --exclude='TOOLS.md'
```

2. 按差异清单逐项评估是否合并。重点关注的目录：
   - `scripts/` — 全部替换（你的项目不会改这些）
   - `skills/_workflow/` — 全部替换
   - `docs/development-specs/` — 有选择地合并
   - `.github/workflows/ci.yml` — 合并（如果有自定义步骤，先备份）

3. 更新 `workspace-config/workspace-version.yaml`

**风险：** 中等。MINOR 升级可能包含新的目录或文件。先用 diff 确认差异范围。

---

## 本地定制保护

升级时必须优先保护以下内容。如果 AI 的升级方案中包含了这些文件的修改，要求 AI 重新输出方案：

- ❌ **绝不覆盖：** `AGENTS.md`、`MEMORY.md`、`TOOLS.md`、`workspace-config/code-sources.yaml`
- ❌ **绝不删除：** `docs/projects/`、`skills/<project>/`、`references/` 中的业务资产
- ⚠️ **谨慎合并：** Skill 的 `rules/README.md`、`checklist.md`（你可能在末尾添加了团队规则）
- ✅ **可以覆盖：** `skills/_workflow/`、`scripts/`、`docs/development-specs/` 中的模板文件

**如果模板新能力与你的本地定制冲突，升级方案应给出三种选项：**

1. **保留本地定制** — 放弃该模板能力
2. **采用模板能力** — 覆盖本地定制
3. **折中合并** — 部分采用模板，保留核心定制

选择权在你，不在 AI。

---

## 故障回退

### 如果升级过程中出错

```bash
# 1. 用 git 回退到升级前的状态
git stash         # 暂存未提交的改动
git log --oneline # 找到升级前的最后一个 commit
git reset --hard <升级前的 commit>

# 2. 如果已经提交了部分节点
# 用 git revert 逐个回退（保留历史）
git revert <升级相关的 commit>
```

### 如果升级后发现问题

```bash
# 检查具体改动
git diff <升级前 commit> HEAD

# 回退特定文件
git checkout <升级前 commit> -- <文件路径>

# 重新提交
git add <文件路径>
git commit -m "revert: 回退有问题的升级节点"
```

### 预防措施

- 升级前确保工作区干净（`git status` 无未提交改动）
- 在独立分支上执行升级：`git checkout -b upgrade-to-v0.x`
- 每节点验收后再合并到主分支
- 升级完成后运行模板校验：`python3 scripts/validate_template_layout.py .`

---

## FAQ

### Q: 我 fork 了仓库而不是 clone，怎么升级？

```
# 将 open-teams 上游添加为 remote
git remote add upstream https://github.com/struggling-bird/open-teams.git

# 拉取最新模板
git fetch upstream

# 在独立分支上合并
git checkout -b upgrade-from-upstream
git merge upstream/main --no-commit

# 手动处理冲突，保护本地定制
git checkout --ours AGENTS.md MEMORY.md TOOLS.md
git checkout --ours workspace-config/code-sources.yaml
```

### Q: 能不能自动升级？

不能。因为你修改过的文件和模板新版一定有差异，有些差异是你的业务定制（要保留），有些是模板改进（要合并）。必须由你（通过 AI 协助）逐项决策。

### Q: 跳过一个版本直接升级到最新版可以吗？

可以。PATCH 和 MINOR 升级兼容跳跃。直接从 v0.4.1 升级到 v0.4.4 不会丢失中间版本的能力。但仍建议先读 CHANGELOG.md 了解所有版本的变化。

### Q: 我只想升级某个 Skill，不想动别的？

可以。按能力粒度升级。例如只升级 `skills/code-review/`：

1. 从最新模板复制该 Skill 目录
2. 对比差异并合并你的团队规则
3. 更新 `workspace-version.yaml` 的 `upgrade_notes`

### Q: 升级后 AI 的行为变了怎么办？

AI 的行为由 `AGENTS.md` + `MEMORY.md` + `Skills` 共同控制。升级不触及 `AGENTS.md` 和 `MEMORY.md`（这两个是你的业务定制，受保护）。只有 Skills 更新可能改变 AI 的具体执行方式。如果觉得新 Skill 不如旧的，可以回退 Skill 目录。

---

## 相关阅读

- [工作空间版本规则](./workspace-versioning.md) — 版本号规则和版本记录职责
- [工作空间版本维护与升级模型](./workspace-upgrade-model.md) — 升级机制设计
- [工作空间升级提示词](./workspace-upgrade-prompts.md) — 可复制的 AI 升级提示词
- [workspace-upgrade Skill](../../skills/_workflow/workspace-upgrade/SKILL.md) — 升级流程 Skill
- [CHANGELOG.md](../../CHANGELOG.md) — 版本变更记录
- [workspace-version.yaml](../../workspace-config/workspace-version.yaml) — 版本元信息