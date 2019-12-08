# import json
from sort_dict import sort_head_coll
from print_sents import tuple_to_string
import extract_colls


def print_sents(head, coll, head_coll_sents, f):
    for i, sent in enumerate(head_coll_sents[head][coll], 1):
        print(i, tuple_to_string(sent), file=f)


def print_coll(head, coll_counts, head_coll_sents, f):
    for count, coll in coll_counts:
        print('-'*50, file=f)
        print('搭配詞：', coll, count, '('+head+')', file=f)
        print('-'*50, file=f)
        print_sents(head, coll, head_coll_sents, f)


def print_head_coll(order, head_coll_sents, f):
    count, head = order[0]
    print('='*50, file=f)
    print(head, count, file=f)
    print_coll(head, order[1], head_coll_sents, f)
    print('', file=f)


def print_counts_sents(head_coll_orders, head_coll_sents, head, name):
    with open(f"{head}_coll_sents_{name}.txt", 'w') as f:
        for order in head_coll_orders:
            print_head_coll(order, head_coll_sents, f)


def main(head, size, head_pos, dist, coll_pos):
    # head_coll_sents = json.load(open(f"{filename}.json"))
    cna_data, udn_data = extract_colls.main(head, size, head_pos, dist, coll_pos)
    cna_orders = sort_head_coll(cna_data)
    udn_orders = sort_head_coll(udn_data)

    print_counts_sents(cna_orders, cna_data, head, 'cna')
    print_counts_sents(udn_orders, udn_data, head, 'udn')


if __name__ == '__main__':
    from parse_comand import parse_command
    head, size, head_pos, dist, coll_pos = parse_command()

    main(head, size, tuple(head_pos), dist, tuple(coll_pos))

# python print_freq_sents.py 擦 -s 2 -hp V -d 1 -cp V N D
# python print_freq_sents.py 目標詞 -s 字數 -hp 目標詞詞性 -d 距離 -cp 搭配詞詞性
