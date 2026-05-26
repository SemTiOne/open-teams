# 工作空间流程 Skill 设计规范

## 1. 目的

本规范用于指导工作空间建立可复用的通用流程 skill，将 `AGENTS.md` 中的治理约束转换为可按任务阶段调用、可验证产物与可审计退出条件的执行资产。

本规范定义目标结构与编写规则。首批流程 skill 已按本规范落地，实际可用能力仍以 `skills/README.md` 中登记且文件存在的 skill 为准。

## 2. 两类 Skill 的职责边界

| 类型 | 目录约定 | 职责 | 典型内容 |
| --- | --- | --- | --- |
| 工作空间流程 skill | `skills/_workflow/<workflow>/SKILL.md` | 约束跨项目通用的任务阶段、质量门禁和交付证据 | 方案确认、实施计划、系统化排错、完成验证、分支治理 |
| 项目场景 skill | `skills/<project>/<scene>/SKILL.md` | 描述单项目内的技术事实、代码入口和场景处理方法 | 某项目 bugfix、接口重构、性能排查 |

组合规则：

1. 流程 skill 回答“任务应按什么阶段推进、何时必须停下确认、需要留下什么证据”。
2. 项目场景 skill 回答“这个项目具体看哪里、如何实现、如何验证实际行为”。
3. 真实项目任务通常先选流程 skill，再按需叠加一个项目场景 skill；项目 skill 不重复复制工作空间级治理全文。
4. `AGENTS.md` 始终是最高优先级约束；skill 负责把约束转成更具体的动作和产物，不得绕过其确认与验收门禁。

## 3. 首批流程 Skill

| Workflow | 适用时机 | 主要产物 | 关键停止点 |
| --- | --- | --- | --- |
| `solution-confirmation` | 用户提出新增、调整或问题处理诉求，尚未确认实施方案 | 范围、备选方案、推荐结论、待确认事项 | 用户明确同意方案前不得实施 |
| `writing-implementation-plan` | 方案已确认，即将进入修改阶段 | `task-plans/` 方案与节点计划、验收标准 | 计划文档落地前不得实施 |
| `systematic-debugging` | 出现故障、回归、报错或行为异常 | 复现证据、根因判断、修复策略、回归结果 | 根因或验证路径不清时不得直接宣称修复 |
| `verification-before-completion` | 某节点或整体任务准备报告完成 | 变更范围、执行命令、验证结果、风险遗留 | 无新鲜证据不得报告完成 |
| `branch-and-worktree-workflow` | 进入会修改源码或配置的开发任务 | 分支/工作树选择、基线状态、收尾选项 | 用户已有改动冲突风险未澄清前不得推进 |
| `workspace-upgrade` | 用户要求检查、规划或实施工作空间升级 | 升级差异、升级方案、节点计划、升级验证和变更历史 | 用户确认升级方案前不得修改文件 |

## 4. 路由规则

| 任务特征 | 首选流程 skill | 可叠加项目 skill | 必须产生的证据 |
| --- | --- | --- | --- |
| 新功能、功能重构、接口重构 | `solution-confirmation` -> `writing-implementation-plan` -> `verification-before-completion` | 对应项目 `new-feature-dev`、`feature-refactor`、`api-refactor` | 已确认方案、节点计划、验证结果 |
| Bug 修复或问题排查 | `solution-confirmation` -> `systematic-debugging` -> `writing-implementation-plan` -> `verification-before-completion` | 对应项目 `bugfix` | 复现与根因证据、已确认修复计划、修复验证 |
| 性能或安全改造 | `solution-confirmation` -> `writing-implementation-plan` -> `verification-before-completion` | 对应项目 `performance-tuning`、`security-fix` | 风险边界、前后验证 |
| 进入代码修改阶段 | `branch-and-worktree-workflow` | 由任务类型决定 | 分支与工作区状态 |
| 节点验收或任务收口 | `verification-before-completion` | 无需强制叠加 | 完成说明、验证与遗留项 |
| 工作空间升级 | `workspace-upgrade` -> `solution-confirmation` -> `writing-implementation-plan` -> `verification-before-completion` | 按需叠加项目场景 skill | 升级差异、已确认方案、节点计划、验证和变更历史 |

说明：使用流程 skill 时仍必须遵循 `AGENTS.md` 的既有门禁；若两者存在差异，以 `AGENTS.md` 为准。

## 5. `SKILL.md` 必备章节

工作空间流程 skill 与项目场景 skill 均应覆盖以下内容；侧重点可以不同，但不得只有原则性口号。

| 章节 | 必须回答的问题 |
| --- | --- |
| `适用范围` | 该 skill 服务于什么任务、项目或阶段？ |
| `触发条件` | 观察到哪些用户意图或现象时应选用该 skill？ |
| `前置输入` | 开始执行前必须获得哪些文档、源码、环境或确认信息？ |
| `产物与退出条件` | 完成后要留下什么证据，达到什么条件才能退出或移交下一阶段？ |
| `工作流程` | 执行步骤、确认门禁与失败回退路径是什么？ |
| `验证清单` | 如何验证结果是真实有效且与范围一致？ |
| `禁止事项` | 哪些越界行为或常见错误必须避免？ |
| `按需资料` | 哪些 references 或 examples 只在相关场景加载？ |

## 6. 编写与维护原则

1. `SKILL.md` 保持短而可执行；大量事实资料放入同目录 `references/`，使用案例放入 `examples.md`。
2. 触发条件应使用实际任务表述或状态描述，避免“需要时使用”这类无法路由的描述。
3. 步骤中必须写出用户确认、验证证据和退出条件，避免只有实现动作而没有质量门禁。
4. 流程资产新增或调整后，应同步更新 `skills/README.md` 和 `workspace-assets-index.md`；若影响 AI 总体约束，再同步调整 `AGENTS.md`。
5. 后续自动校验应验证流程 skill 的存在性、必备章节和索引登记情况，避免模板只剩目录结构而失去执行内容。
