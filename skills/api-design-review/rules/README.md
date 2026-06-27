# API Design Review Rules

> 每个规则标注严重级别。代码审查时按级别判断是否阻塞合并。

---

## 🔴 Critical（阻塞合并 · 安全相关）

- **SEC-API-001: 敏感端点必须认证** — 所有涉及用户数据或写操作的公开端点必须验证身份。未认证即可访问的私有数据端点 = 数据泄露。
- **SEC-API-002: 敏感字段禁止出现在响应中** — password、token、secret、private_key 等字段不得返回给客户端。
- **SEC-API-003: 输入验证** — 所有用户输入必须验证类型、长度、范围、格式。禁止信任客户端数据。

---

## 🟠 High（应该修复 · 规范/性能）

- **REST-001: 复数资源名** — 集合端点使用复数名词：`/users`、`/orders`，不使用单数或动词。
- **REST-002: HTTP 方法语义正确** — GET=读、POST=创建、PUT=全量替换、PATCH=部分更新、DELETE=删除。URL 中不出现动词。
- **REST-003: 列表接口必须分页** — 所有返回集合的端点必须支持分页。建议 cursor-based，至少 page/pageSize。必须设置最大限制。
- **REST-004: 一致响应信封** — 成功和错误响应使用统一结构。例如 `{ data: ..., meta: { page, pageSize, total } }` 和 `{ errors: [{ code, message, field }] }`。
- **PERF-API-001: 字段过滤** — 支持 `?fields=id,name` 减少不必要的传输。
- **PERF-API-002: 条件请求** — 对缓存友好的资源支持 ETag / If-None-Match / Last-Modified。

---

## 🟡 Medium（建议修复 · 语义/一致性）

- **SEM-API-001: 幂等性** — PUT 和 DELETE 操作应该是幂等的，多次调用结果相同。
- **SEM-API-002: HATEOAS 可选** — 对于公开 API，考虑在响应中包含相关资源链接。
- **SEM-API-003: 排序支持** — 列表接口支持 `?sort=createdAt&order=desc`。
- **SEM-API-004: 批量操作** — 当常见场景需要多资源操作时，提供批量接口避免 N+1 客户端调用。

---

## 🟢 Low（优化建议 · 体验）

- **DX-API-001: 错误消息可操作** — 不只返回"错误"，返回 code + message + 可选 field 指向具体问题。
- **DX-API-002: 速率限制头** — 在响应中返回 `X-RateLimit-*` 头，让调用方知道剩余配额。
- **DX-API-003: 废弃标记** — 要废弃的字段/端点先标记 deprecated，给 Sun set 时间线，不要突然删除。

---

## 如何添加团队规则

在下方按相同格式添加你的团队专属规则：

```
- **RULE-XXX:** 规则描述 — 修复指引
```

常见团队定制项：
- 错误信封格式（你的团队的 `"error"` vs `"errors"` 约定）
- API 版本策略（URL /v1/ vs Header）
- 认证方式（JWT vs Session vs OAuth2）
- GraphQL 额外规则（N+1 查询、深度限制、复杂度分析）