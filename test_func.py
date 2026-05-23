def generate_multiplication_table():
    """返回九九乘法表的字符串列表"""
    result = []
    for i in range(1, 10):
        row = []
        for j in range(1, i + 1):
            row.append(f"{j}x{i}={i*j:2d}")
        result.append("  ".join(row))
    return result


if __name__ == "__main__":
    lines = generate_multiplication_table()
    for line in lines:
        print(line)
