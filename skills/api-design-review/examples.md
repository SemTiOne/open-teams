# API Design Review — 审查示例

## 示例 1：设计良好的 API（✅ 通过）

### 审查对象：`/api/v1/users` 端点组

- `GET /api/v1/users?page=1&pageSize=20&sort=createdAt&order=desc` → 分页用户列表
- `GET /api/v1/users/:id` → 用户详情
- `POST /api/v1/users` → 创建用户
- `PATCH /api/v1/users/:id` → 更新用户

**审查结论：** ✅ 通过

| 检查项 | 结果 | 说明 |
|--------|------|------|
| 资源命名 | ✅ | 复数 `/users` |
| HTTP 方法 | ✅ | 语义正确，无动词 |
| 分页 | ✅ | page + pageSize，有默认值和最大值 |
| 认证 | ✅ | 所有端点需要 JWT |
| 响应格式 | ✅ | `{ data, meta }` 统一信封 |
| 错误格式 | ✅ | `{ errors: [{ code, message }] }` |
| 敏感字段 | ✅ | 无 password/token 泄露 |

---

## 示例 2：需要改进的 API（⚠️ 有条件通过）

### 审查对象：订单接口设计

```
POST /api/createOrder
GET /api/getOrders?userId=123
GET /api/getOrderById/456
```

**审查结论：** ⚠️ 有条件通过（需修复 3 个问题后重新审查）

| 问题 | 严重级别 | 说明 | 修复 |
|------|---------|------|------|
| URL 含动词 | 🟡 Medium | `/createOrder`、`/getOrders` 不符合 REST 规范 | 改为 `POST /api/v1/orders`、`GET /api/v1/orders` |
| 无分页 | 🟠 High | `GET /api/orders?userId=123` 无分页，用户订单量大时会超时 | 添加 `page`/`pageSize` 参数 |
| 无认证声明 | 🔴 Critical | 创建订单接口未说明认证方式 | 所有写操作需要 JWT 认证 |

---

## 示例 3：严重问题的 API（❌ 不通过）

### 审查对象：用户注册接口

```
POST /api/register
Body: { "username": "test", "password": "mypassword", "email": "test@example.com" }
Response: { "id": 1, "username": "test", "password": "mypassword", "token": "abc" }
```

**审查结论：** ❌ 需要重新设计

| 问题 | 严重级别 | 说明 |
|------|---------|------|
| 密码出现在响应中 | 🔴 Critical | 返回了用户密码明文——严重安全漏洞 |
| 无输入验证 | 🔴 Critical | 未限制 username/email 格式和 password 长度 |
| 无速率限制 | 🟠 High | 注册接口无防暴力破解措施 |
| 响应格式不一致 | 🟡 Medium | 直接返回对象，没有错误信封结构 |

---

*根据你的团队实际情况积累更多审查示例。好的示例让团队成员快速对齐 API 设计标准。*