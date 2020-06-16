my_tree = {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: {'fin': {0: 'no', 1: 'yes'}}}}, 1: {'warm blooded': {0: {'gill': {0: 'no', 1: {'jaw': {0: 'no', 1: 'yes'}}}}, 1: 'no'}}}}}}

def get_tree_depth(my_tree):
    max_depth = 0
    my_tree = list(my_tree.values())[0]
    for value in my_tree.values():
        this_depth = 1
        if isinstance(value, dict):  # 字典，即节点，需要进行一次递归
            r_max_depth = get_tree_depth(value)
            # print(r_max_depth, this_depth)
            this_depth += r_max_depth
        # print(this_depth, max_depth)
        max_depth = max(this_depth, max_depth)
    # print(max_depth)
    return max_depth

if __name__ == '__main__':
	print(get_tree_depth(my_tree))