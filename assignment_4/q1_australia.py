from CSP import solve_csp

vars = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
doms = {v: ['Red', 'Green', 'Blue'] for v in vars}

nbrs = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

if __name__ == "__main__":
    ans = solve_csp(vars, doms, nbrs)

    print("Australia Map Coloring:")
    for area, color in ans.items():
        print(f"{area:<4}-> {color}")
