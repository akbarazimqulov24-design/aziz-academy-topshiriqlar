res = sorted(set(input().strip()))
print("{" + ", ".join(f"'{x}'" for x in res) + "}")