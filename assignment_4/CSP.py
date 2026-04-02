def solve_csp(vars, doms, nbrs):
    def is_valid(var, val, asn):
        for nbr in nbrs.get(var, []):
            if nbr in asn and asn[nbr] == val:
                return False
        return True

    def backtrack(asn):
        if len(asn) == len(vars):
            return asn

        curr = [v for v in vars if v not in asn][0]

        for val in doms[curr]:
            if is_valid(curr, val, asn):
                asn[curr] = val
                res = backtrack(asn)
                if res:
                    return res
                del asn[curr]

        return None

    return backtrack({})
