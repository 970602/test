import pandas as pd

# 用 pandas 输出九九乘法表
data = {}
for i in range(1, 10):
    col = []
    for j in range(1, 10):
        if j <= i:
            col.append(f"{j}x{i}={i*j}")
        else:
            col.append("")
    data[f"{i}"] = col

df = pd.DataFrame(data, index=[f"{j}" for j in range(1, 10)])
df.index.name = "乘数"
print(df.to_string())
