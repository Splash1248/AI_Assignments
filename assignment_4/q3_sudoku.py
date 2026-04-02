from CSP import solve_csp

rows = 'ABCDEFGHI'
cols = '123456789'
vars = [r + c for r in rows for c in cols]

grid = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

doms = {}
for i, r in enumerate(rows):
    for j, c in enumerate(cols):
        val = grid[i][j]
        doms[r + c] = [val] if val != 0 else [1, 2, 3, 4, 5, 6, 7, 8, 9]

nbrs = {}
for v in vars:
    r, c = v[0], v[1]
    r_idx, c_idx = rows.index(r), cols.index(c)

    grp = [r + x for x in cols] + [x + c for x in rows] + \
          [rows[i] + cols[j] for i in range((r_idx//3)*3, (r_idx//3)*3 + 3)
                             for j in range((c_idx//3)*3, (c_idx//3)*3 + 3)]

    nbrs[v] = list(set(grp))
    nbrs[v].remove(v)

if __name__ == "__main__":
    ans = solve_csp(vars, doms, nbrs)

    if ans:
        for i, r in enumerate(rows):
            if i % 3 == 0:
                print("+-------+-------+-------+")

            row_str = ""
            for j, c in enumerate(cols):
                if j % 3 == 0:
                    row_str += "| "
                row_str += str(ans[r + c]) + " "
            print(row_str + "|")
        print("+-------+-------+-------+")
    else:
        print("No solution found.")
