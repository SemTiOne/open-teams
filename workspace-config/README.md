# 工作空间配置入口模板

本目录用于存放机器可读或半机器可读的工作空间配置资产。

首次采用模板时，最先修改 `code-sources.yaml`。只要这里能指向真实源码，AI 就能先建立项目入口；其他配置可按 [快速上手](../QUICKSTART.md) 的推荐增强路径逐步补齐。

建议至少包含：

- `code-sources.yaml`
- `workspace-version.yaml`
- 本地服务栈说明
- 包管理或制品仓配置模板

当前通用配置：

- [code-sources.yaml](./code-sources.yaml)：记录真实项目仓库、源码目录、默认分支和代码源策略。初始化新工作空间时必须替换示例仓库。
- [workspace-version.yaml](./workspace-version.yaml)：记录模板身份、版本修订、已应用能力、升级策略和本地定制说明，用于支持 AI 提示词驱动的按需升级。
