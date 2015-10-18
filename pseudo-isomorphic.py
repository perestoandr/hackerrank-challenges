input_str = raw_input().strip()


def preprocess(_str):
    prev_smbls = dict()
    _a = list()
    for i in range(len(_str)):
        if _str[i] in prev_smbls:
            _a.append(i - prev_smbls[_str[i]])
        else:
            _a.append(i + 1)
        prev_smbls[_str[i]] = i
    return _a, prev_smbls


a, prev_symbols = preprocess(input_str)


class Node:
    def __init__(self, **d):
        self.__dict__ = d


class Edge:
    def __init__(self, **d):
        self.__dict__ = d


root = Node(edges=dict(), depth=0, slink=None)
def_edge = Edge(a=root, b=root, u=0, length=0)
curr_edge = (def_edge, 0, 0)
leaves_counter = 0
result = 0


def convert(_c, depth):
    return -1 if _c > depth else _c


def simplify(_curr_edge):
    edge, u, l = _curr_edge
    while l > edge.length:
        c = convert(a[u + edge.length], edge.a.depth + edge.length)
        edge, u, l = edge.b.edges[c], u + edge.length, l - edge.length
    return edge, u, l


def slink(_curr_edge):
    edge, u, length = _curr_edge
    if edge.a == root:
        assert (edge != def_edge)
        return simplify((def_edge, u + 1, length - 1))
    else:
        edge.a.slink = simplify(edge.a.slink)
        tmp_edge, u1, tmp_length = edge.a.slink
        return simplify((tmp_edge, u - tmp_length, length + tmp_length))


for i in range(len(input_str)):
    while True:
        edge, u, length = curr_edge
        c = convert(a[i], edge.a.depth + length)
        if length == edge.length:
            if c in edge.b.edges:
                break
            leaves_counter += 1
            leaf = Node(depth=-1, slink=None, edges=dict())
            edge.b.edges[c] = Edge(a=edge.b, b=leaf, u=i, length=len(input_str) - i)
        else:
            c1 = convert(a[edge.u + length], edge.a.depth + length)
            if c == c1:
                break
            leaves_counter += 1
            leaf = Node(depth=-1, slink=None, edges=dict())
            branch = Node(edges=dict(), depth=edge.a.depth + length, slink=slink(curr_edge))
            branch.edges[c] = Edge(a=branch, b=leaf, u=i, length=len(input_str) - i)
            branch.edges[c1] = Edge(a=branch, b=edge.b, u=edge.u + length, length=edge.length - length)
            edge.b = branch
            edge.length = length
        if edge == def_edge and length == 0:
            curr_edge = None
            break
        if edge.a == root:
            assert (edge != def_edge)
            curr_edge = simplify((def_edge, u + 1, length - 1))
        else:
            edge.a.slink = simplify(edge.a.slink)
            tmp_edge, tmp_u, tmp_length = edge.a.slink
            curr_edge = simplify((tmp_edge, u - tmp_length, length + tmp_length))
    if curr_edge is None:
        curr_edge = def_edge, i + 1, 0
    else:
        edge, u, length = curr_edge
        assert (u + length == i)
        curr_edge = simplify((edge, u, length + 1))
    result += leaves_counter
    print(result)
