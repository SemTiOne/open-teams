# 模板采用清理指南

本指南用于 AI 把 `open-teams` 模板复制成业务工作空间时，避免把模板仓库自身的迭代记录、任务计划和历史事实带入业务项目。

## 清理原则

1. 保留模板能力，清理模板事实。
2. 保留目录结构和模板文件，清理 `open-teams` 自身任务记录。
3. AI 必须先确认目标目录和用户授权，再复制模板。
4. 清理动作只针对新业务工作空间副本，不用于清理 `open-teams` 模板仓库本身。

## 建议处理方式

| 资产 | 处理方式 | 原因 |
| --- | --- | --- |
| `task-plans/TEMPLATE.md` | 保留 | 后续任务方案与实施计划模板 |
| `task-plans/README.md` | 保留 | 目录说明 |
| `task-plans/YYYY-*.md` | 清理 | 这些是模板自身已确认方案和实施计划 |
| `change-history/TEMPLATE.md` | 保留 | 后续任务变更记录模板 |
| `change-history/README.md` | 保留 | 目录说明 |
| `change-history/open-teams/` | 清理 | 这是模板自身任务历史，不是业务项目事实 |
| `CHANGELOG.md` | 保留并改写 | 可作为模板版本基线记录，但应补充业务工作空间自己的版本记录 |
| `workspace-config/workspace-version.yaml` | 保留并改写 | 应更新采用方式、源码策略和本地定制说明 |
| `workspace-config/code-sources.yaml` | 必须改写 | 示例仓库必须替换为真实项目源码 |
| `AGENTS.md` | 必须改写 | 业务线约束、分支策略和验收规则需要与团队实际一致 |

## AI 推荐执行方式

优先让 AI 使用一条采用脚本完成复制、清理、源码映射写入和校验：

```bash
python3 scripts/adopt_workspace.py \
  --template-root . \
  --target <目标工作空间路径> \
  --project-slug <项目标识> \
  --project-name <项目名称> \
  --source-path <真实源码路径或仓库地址> \
  --default-branch <默认分支>
```

该脚本会调用清理逻辑，删除业务工作空间副本中的模板自身历史记录。

## 单独清理命令

先预览会清理什么：

```bash
python3 scripts/prepare_clean_workspace.py .
```

确认无误后再执行：

```bash
python3 scripts/prepare_clean_workspace.py . --apply
```

脚本只会清理模板自身历史记录，并保留目录说明和模板文件。执行后仍需让 AI 结合用户输入改写 `AGENTS.md`、`workspace-config/code-sources.yaml` 和 `workspace-config/workspace-version.yaml`。

## 清理后 AI 必做

1. 替换 `workspace-config/code-sources.yaml` 中的示例仓库。
2. 调整 `workspace-config/workspace-version.yaml` 中的采用方式、源码策略和本地定制说明。
3. 与用户确认后调整 `AGENTS.md` 中的业务线专属约束。
4. 按当前项目创建 `docs/projects/<project>/` 和 `skills/<project>/`。
5. 运行：

```bash
python3 scripts/validate_template_layout.py .
```

## 不建议清理

- 不建议删除 `skills/_workflow/`，这是模板的核心流程能力。
- 不建议删除 `skills/_templates/`，这是后续生成项目场景 skill 的模板。
- 不建议删除 `task-completion-checklist.md`，这是任务收口检查入口。
- 不建议删除 `workspace-assets-index.md`，这是 AI 首读入口。
