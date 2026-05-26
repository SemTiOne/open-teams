# 工作空间配置入口模板

本目录用于存放机器可读或半机器可读的工作空间配置资产。

建议至少包含：

- `code-sources.yaml`
- `workspace-version.yaml`
- 本地服务栈说明
- 包管理或制品仓配置模板

当前通用配置：

- [workspace-version.yaml](./workspace-version.yaml)：记录模板身份、版本修订、已应用能力、升级策略和本地定制说明，用于支持 AI 提示词驱动的按需升级。
