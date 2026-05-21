# 通用工作空间壳工程

## 1. 定位

本目录是一个可跨业务线复用的工作空间壳工程模板，用于快速初始化新的 AI 协作研发工作空间。

目标是提供一套通用骨架，而不是复制当前业务线的现成项目资产。

## 2. 适用场景

- 新业务线准备建设 AI 协作工作空间
- 需要统一文档、skills、参考资料、任务计划与变更历史的组织方式
- 需要保留“方案确认 -> 实施计划 -> 节点验收 -> 资料沉淀”的治理闭环

## 3. 不包含内容

- 当前业务线的真实源码
- 当前业务线的项目级文档
- 当前业务线的项目级 skill
- 当前业务线的环境账号、测试地址或数据字典

## 4. 目录结构

- `AGENTS.md`：工作空间级 AI 协作约束模板
- `workspace-assets-index.md`：非源码资产入口模板
- `task-completion-checklist.md`：任务收尾闭环检查模板
- `docs/`：通用文档入口与占位结构
- `skills/_templates/`：项目场景 skill 模板
- `workspace-config/`：机器可读工作空间配置模板
- `references/`：可补充的外围事实模板
- `scripts/`：初始化与自检脚本
- `task-plans/`：已确认方案与实施计划归档目录
- `change-history/`：已完成任务历史归档目录
- `example-project/`：示例项目资产占位

## 5. 推荐初始化顺序

1. 复制本目录到目标业务线工作空间
2. 按实际业务调整 `AGENTS.md`
3. 补齐 `workspace-config/code-sources.yaml`
4. 按项目创建 `docs/projects/` 与 `skills/<project>/`
5. 用 `scripts/init_project_skills.py` 初始化新项目 skill 骨架
6. 按真实源码持续补齐文档与执行型 skill

## 6. 初始化必做清单

- 将 `AGENTS.md` 中与当前业务线不符的约束、目录说明和协作边界替换为真实内容
- 将 `workspace-config/code-sources.yaml` 中的示例仓库替换为真实仓库映射
- 明确当前工作空间采用“`sources/` 同仓托管”还是“外部仓库映射”模式
- 为首批目标项目补齐 `docs/projects/<project>/` 与 `skills/<project>/`
- 用 `scripts/init_project_skills.py <template_root> <project_slug>` 初始化标准场景 skill
- 首次投入使用前，运行 `scripts/validate_template_layout.py` 做结构校验
- 若任务要求严格节点验收，先确认 `task-plans/TEMPLATE.md` 与 `change-history/TEMPLATE.md` 是否满足本业务线记录要求

## 7. 验收标准

- 可独立作为新工作空间的起点目录
- 不依赖当前业务线专有目录与专有名词
- 目录职责清晰，可按需扩展
