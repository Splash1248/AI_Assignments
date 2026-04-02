vars = ['T', 'W', 'O', 'F', 'U', 'R', 'X1', 'X2', 'X3']
doms = {v: list(range(10)) if len(v) == 1 else [0, 1] for v in vars}



def is_valid(asn):
    letters = [k for k in asn if len(k) == 1]
    vals = [asn[k] for k in letters]
    if len(vals) != len(set(vals)):
        return False

    if 'T' in asn and asn['T'] == 0: return False
    if 'F' in asn and asn['F'] == 0: return False

    if all(k in asn for k in ['O', 'R', 'X1']):
        if asn['O'] + asn['O'] != asn['R'] + 10 * asn['X1']: return False

    if all(k in asn for k in ['W', 'X1', 'U', 'X2']):
        if asn['W'] + asn['W'] + asn['X1'] != asn['U'] + 10 * asn['X2']: return False

    if all(k in asn for k in ['T', 'X2', 'O', 'X3']):
        if asn['T'] + asn['T'] + asn['X2'] != asn['O'] + 10 * asn['X3']: return False

    if all(k in asn for k in ['X3', 'F']):
        if asn['X3'] != asn['F']: return False

    return True



def backtrack(asn):
    if len(asn) == len(vars):
        return asn

    curr = [v for v in vars if v not in asn][0]

    for val in doms[curr]:
        asn[curr] = val
        if is_valid(asn):
            res = backtrack(asn)
            if res:
                return res
        del asn[curr]

    return None

if __name__ == "__main__":
    ans = backtrack({})

    if ans:
        print("TWO + TWO = FOUR\n")
        for k in ['T', 'W', 'O', 'F', 'U', 'R']:
            print(f"{k} = {ans[k]}")

        t_w_o = f"{ans['T']}{ans['W']}{ans['O']}"
        f_o_u_r = f"{ans['F']}{ans['O']}{ans['U']}{ans['R']}"

        print("\nEQUATION CHECK:")
        print(f"  {t_w_o}")
        print(f"+ {t_w_o}")
        print("------")
        print(f" {f_o_u_r}")
    else:
        print("No solution found.")
