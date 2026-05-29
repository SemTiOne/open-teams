# 通用工作空间壳工程

## 1. 定位

本目录是一个可跨业务线复用的工作空间壳工程模板，用于快速初始化新的 AI 协作研发工作空间，也用于帮助已有传统工程渐进式转向 AI 协作研发模式。

目标是提供一套可新建、也可逐步接入存量工程的通用骨架，而不是复制当前业务线的现成项目资产；同时将方案确认、实施计划、排错验证与分支边界等高频协作环节沉淀为可复用、可校验的流程资产。

## 2. 适用场景

- 新业务线准备建设 AI 协作工作空间
- 现有传统工程希望在保留原有代码仓库与研发流程基础上，逐步引入 AI 协作文档、skills、源码映射与治理闭环
- 需要统一文档、skills、参考资料、任务计划与变更历史的组织方式
- 需要保留“方案确认 -> 实施计划 -> 节点验收 -> 资料沉淀”的治理闭环
- 需要以通用 workflow skills 约束跨项目任务推进与交付证据

## 3. 不包含内容

- 当前业务线的真实源码
- 当前业务线的项目级文档
- 当前业务线的项目级 skill
- 当前业务线的环境账号、测试地址或数据字典

## 4. 目录结构

- `AGENTS.md`：工作空间级 AI 协作约束模板
- `CHANGELOG.md`：用户可读的模板版本记录
- `workspace-assets-index.md`：非源码资产入口模板
- `task-completion-checklist.md`：任务收尾闭环检查模板
- `docs/`：通用文档入口与占位结构
- `docs/development-specs/workflow-skills-design.md`：流程 skill 与项目场景 skill 的边界及编写规范
- `docs/development-specs/workspace-versioning.md`：版本号规则、版本记录格式与版本资产关系
- `docs/development-specs/workspace-upgrade-model.md`：工作空间版本维护与升级模型
- `docs/development-specs/workspace-upgrade-prompts.md`：可复制的 AI 升级交互提示词
- `skills/_workflow/`：工作空间级通用流程 skill
- `skills/_templates/`：项目场景 skill 模板
- `workspace-config/`：机器可读工作空间配置模板
- `workspace-config/workspace-version.yaml`：模板版本、已应用能力与升级策略元信息
- `references/`：可补充的外围事实模板
- `scripts/`：初始化与自检脚本
- `task-plans/`：已确认方案与实施计划归档目录
- `change-history/`：已完成任务历史归档目录

## 5. 内置工作流程

本模板提供以下工作空间级流程 skill，并与 `AGENTS.md` 的确认和验收约束配套使用：

| 流程 skill | 作用 |
| --- | --- |
| `solution-confirmation` | 在实施前澄清目标、范围、方案与用户授权 |
| `writing-implementation-plan` | 将已确认方案落地为可执行、可验收的节点计划 |
| `systematic-debugging` | 以复现和证据定位异常根因并指导修复验证 |
| `verification-before-completion` | 在报告完成前核对改动范围、验证结果与风险 |
| `branch-and-worktree-workflow` | 明确分支、工作区边界与版本维护门禁 |
| `workspace-upgrade` | 通过 AI 提示词检查、规划和执行工作空间按需升级 |

流程 skill 处理跨项目的推进方法与质量门禁；真实项目的代码入口、接口边界和专项验证要求应继续沉淀到 `skills/<project>/<scene>/`。

## 6. 采用方式

### 新建工作空间

适合新业务线或新工程从一开始即采用统一的 AI 协作资产与治理流程：

1. 复制本目录为业务线工作空间。
2. 按真实工程补齐源码映射、项目文档与场景 skill。
3. 以工作空间流程 skill 约束后续研发任务推进。

### 存量工程渐进式转型

适合已有传统工程在不搬迁原有仓库、不一次性重构研发方式的前提下逐步接入：

1. 先通过 `workspace-config/code-sources.yaml` 维护现有代码仓库映射，或按需将源码纳入 `sources/`。
2. 从高频协作项目或问题场景开始，补齐 `docs/projects/` 与 `skills/<project>/<scene>/` 的最小必要资产。
3. 在实际任务中使用通用 workflow skills 执行方案确认、计划、验证和资料沉淀，让资产随真实工作逐步成长。

## 7. 持续升级方式

本模板支持提示词驱动的工作空间按需升级。业务工作空间可通过 `workspace-config/workspace-version.yaml` 记录当前模板基线和已应用能力，再使用 [工作空间升级提示词](./docs/development-specs/workspace-upgrade-prompts.md) 触发 AI 检查、规划和实施升级。

用户可通过 [CHANGELOG.md](./CHANGELOG.md) 了解每个模板版本新增了什么、升级影响和推荐升级提示词；版本规则见 [工作空间版本规则](./docs/development-specs/workspace-versioning.md)。

升级必须遵循以下边界：

- 先输出升级方案，获得用户确认后再修改文件。
- 先将升级计划写入 `task-plans/`，经用户确认实施计划后再按节点实施。
- 保护业务线本地定制和真实源码映射，不用模板示例覆盖。
- 每个节点完成后等待用户验收。
- 升级完成后运行模板校验，并补充复盘与 `change-history/`。

## 8. 推荐初始化顺序

1. 复制本目录到目标业务线工作空间
2. 按实际业务调整 `AGENTS.md`
3. 补齐 `workspace-config/code-sources.yaml`
4. 确认或调整 `workspace-config/workspace-version.yaml`
5. 按项目创建 `docs/projects/` 与 `skills/<project>/`
6. 用 `scripts/init_project_skills.py` 初始化新项目 skill 骨架
7. 确认通用 workflow skills 是否需要按业务线治理方式补充或收缩
8. 按真实源码持续补齐文档与执行型 skill

## 9. 初始化必做清单

- 将 `AGENTS.md` 中与当前业务线不符的约束、目录说明和协作边界替换为真实内容
- 将 `workspace-config/code-sources.yaml` 中的示例仓库替换为真实仓库映射
- 按当前业务线情况调整 `workspace-config/workspace-version.yaml` 的采用方式、本地定制说明与已应用能力
- 明确当前工作空间采用“`sources/` 同仓托管”还是“外部仓库映射”模式
- 若使用 `sources/` 接入真实业务源码，默认只保留 `sources/README.md`，真实源码目录不提交到模板仓库
- 为首批目标项目补齐 `docs/projects/<project>/` 与 `skills/<project>/`
- 用 `scripts/init_project_skills.py <template_root> <project_slug>` 初始化标准场景 skill
- 首次投入使用前，运行 `scripts/validate_template_layout.py` 校验必需结构、workflow skills、入口登记与模板卫生
- 需要持续升级时，先阅读 `CHANGELOG.md` 判断版本差异，再使用升级提示词触发 AI 检查和规划
- 若任务要求严格节点验收，先确认 `task-plans/TEMPLATE.md` 与 `change-history/TEMPLATE.md` 是否满足本业务线记录要求

## 10. 验收标准

- 可独立作为新工作空间的起点目录
- 不依赖当前业务线专有目录与专有名词
- 目录职责清晰，可按需扩展
- 通用 workflow skills 可从入口定位，且具备触发、产物、验证与退出条件
- 用户可通过 `CHANGELOG.md` 感知每个模板版本的能力变化和升级影响
- `scripts/validate_template_layout.py` 能识别缺失的流程资产、升级资产、入口登记或模板卫生问题
