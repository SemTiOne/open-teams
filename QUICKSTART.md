# 快速上手

这份指南只解决一件事：把 `open-teams` 变成你自己项目可用的 AI 协作工作空间。先跑通最小路径，再按需要补治理资产。

## 5 分钟最小可用

适合先把工作空间跑起来，不一次性理解全部目录。

1. 复制模板到你的业务工作空间目录。
2. 打开 `workspace-config/code-sources.yaml`，把示例仓库替换成真实项目路径。
3. 按团队实际情况改 `AGENTS.md` 的工作约束。
4. 运行：

```bash
python3 scripts/validate_template_layout.py .
```

做到这一步后，AI 已经能从 `workspace-assets-index.md` 找到工作空间入口，并能知道真实源码在哪里。

## 30 分钟推荐增强

适合让 AI 更稳定地理解你的项目。

1. 在 `docs/projects/<project>/` 下补一个项目入口说明，写清项目职责、主要模块和源码位置。
2. 运行 `scripts/init_project_skills.py` 初始化项目场景 skill：

```bash
python3 scripts/init_project_skills.py . <project_slug>
```

3. 在 `skills/<project>/README.md` 和关键场景 `SKILL.md` 中补充真实路径、验证命令和常见边界。
4. 在 `workspace-assets-index.md` 的推荐阅读路径中登记你的项目入口。

做到这一步后，AI 不只知道“代码在哪里”，也知道“这个项目怎么读、怎么改、怎么验”。

## 持续治理闭环

适合团队长期使用。

1. 用 `task-plans/` 记录已确认方案、实施计划和节点状态。
2. 用 `task-completion-checklist.md` 约束每次任务完成前的验证、风险说明和用户确认。
3. 用 `change-history/` 记录已完成任务的背景、改动、验证、复盘和资料同步。
4. 用 `workspace-config/workspace-version.yaml` 和 `CHANGELOG.md` 跟踪模板能力升级。

做到这一步后，工作空间会随着真实任务持续长出可复用资产，而不是只留下一串聊天记录。

## 第一次修改哪些文件

| 文件 | 必改程度 | 修改目标 |
| --- | --- | --- |
| `workspace-config/code-sources.yaml` | 必改 | 替换示例仓库，指向真实源码 |
| `AGENTS.md` | 必改 | 写入团队自己的协作边界、分支规则和验收要求 |
| `workspace-config/workspace-version.yaml` | 推荐 | 标记采用方式、源码策略和本地定制说明 |
| `docs/projects/<project>/` | 推荐 | 补项目入口和源码说明 |
| `skills/<project>/` | 推荐 | 补项目级执行场景、验证方式和常见约束 |
| `references/` | 按需 | 放接口、环境、数据字典、报文等外围事实 |

## 第一次不用读什么

- 不需要先读完所有 `skills/_workflow/`，任务触发到对应阶段时再按需读取。
- 不需要先补齐所有项目文档，优先补当前最常改或最常排查的项目。
- 不需要先整理完整历史任务，`change-history/` 只记录采用模板后的已完成任务。
- 不需要把真实源码提交进模板仓库；如果使用 `sources/`，默认只保留 `sources/README.md`。
