# API Design Review Checklist

## 设计阶段

- [ ] 资源命名使用复数名词（`/users` 不是 `/getUsers`）
- [ ] URL 路径只含名词，不含动词（创建用 `POST /users`，不是 `POST /createUser`）
- [ ] HTTP 方法语义正确：GET=读、POST=创建、PUT=全量替换、PATCH=部分更新、DELETE=删除
- [ ] API 版本策略已明确（URL 路径 `/v1/`、请求头、还是查询参数）

## 响应设计

- [ ] 响应格式一致（所有成功/错误响应用同一信封结构）
- [ ] 错误响应包含可操作的错误信息（code + message + 可选 field/细节）
- [ ] 列表接口支持分页（至少 page/pageSize，推荐 cursor-based）
- [ ] 支持字段过滤（`?fields=id,name,email`），避免返回不需要的字段

## 安全

- [ ] 所有写操作和涉及用户数据的读操作需要认证
- [ ] 禁止在 URL 中传递敏感数据（token、密码）
- [ ] 输入验证：类型、长度、范围、格式
- [ ] 限流策略已考虑（尤其是登录、注册、密码重置接口）
- [ ] 敏感字段（password、token、密钥）不出现在响应中

## 向后兼容

- [ ] 字段新增是加性的，不删除/改名字段
- [ ] 废弃字段有明确的 sun set 计划（deprecation notice → sunset date）
- [ ] 向后不兼容的变更通过新版本 API 发布

## 性能

- [ ] 列表接口有默认和最大分页限制
- [ ] 考虑是否需要批量接口避免 N+1 调用
- [ ] 支持条件请求（ETag / If-None-Match）减少数据传输
- [ ] 响应体 >100KB 考虑分页或压缩

## 文档

- [ ] OpenAPI/Swagger 文档已更新
- [ ] 每个端点有请求/响应示例
- [ ] 认证方式和错误码有文档说明