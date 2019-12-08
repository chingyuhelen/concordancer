def sort_coll(head, coll_sents):
    coll_counts = [[len(sents), coll] for coll, sents in coll_sents.items()]
    return sorted(coll_counts, reverse=True)


def count_head_coll(head, coll_sents):
    head_coll_counts = []
    coll_orders = sort_coll(head, coll_sents)
    head_counts = sum([coll_order[0] for coll_order in coll_orders])

    head_coll_counts.append([head_counts, head])
    head_coll_counts.append(coll_orders)

    return head_coll_counts


def sort_head_coll(iterable):
    head_coll_orders = []
    for head, coll_sents in iterable.items():
        head_coll_counts = count_head_coll(head, coll_sents)
        head_coll_orders.append(head_coll_counts)

    return sorted(head_coll_orders, key=lambda x: x[0][0], reverse=True)
