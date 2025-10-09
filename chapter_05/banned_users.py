# 知识点：使用 in / not in 检查用户是否在黑名单中。

banned_clients = ['late payer', 'unrealistic deadline']
client = 'late payer'

if client not in banned_clients:
    print(f"Scheduling project for {client}.")
else:
    print(f"Cannot accept the project: {client}.")
