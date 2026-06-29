# 示例

以下示例说明如何在实际对话中触发项目 Scoped Skill：

**示例 1 — 代码审查场景：**

> "用 `code-review` skill 审查最近一次提交，重点关注安全问题和 N+1 查询。"

**示例 2 — API 设计审查场景：**

> "用 `api-design-review` skill 审查新的 `/orders` 接口设计，确认分页、认证和幂等性。"

**示例 3 — 架构决策场景：**

> "用 `architecture-review` skill 审查引入 Redis 缓存层的方案，重点关注故障模式和成本影响。"

---

*更多场景示例可在实际使用中积累。将 `scene-template/` 复制为你的项目场景（如 `my-project/bugfix`），再按实际需求填写触发条件和工作流。*