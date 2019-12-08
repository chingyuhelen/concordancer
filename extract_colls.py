import json
from words_filter import check_colls
import extract_sents


def extract_coll(data, coll_pos, dist=1):
    for head, sents in data.items():
        coll_sents = check_colls(head, sents, coll_pos, dist)
        data[head] = coll_sents
    return data


def main(head, size, head_pos, dist, coll_pos):
    # data = json.load(open(f"{filename}.json"))
    cna_data, udn_data = extract_sents.main(head, size, head_pos)
    # cna_data = json.load(open(f"{filename}.json"))
    # udn_data = json.load(open(f"{head}))
    cna_coll_sents = extract_coll(cna_data, coll_pos, dist)
    udn_coll_sents = extract_coll(udn_data, coll_pos, dist)

    json.dump(cna_coll_sents, open(f"{head}_coll_sents_cna.json", 'w'))
    json.dump(udn_coll_sents, open(f"{head}_coll_sents_udn.json", 'w'))

    return cna_coll_sents, udn_coll_sents


if __name__ == '__main__':
    from parse_comand import parse_command
    head, size, head_pos, dist, coll_pos = parse_command()

    main(head, size, tuple(head_pos), dist, tuple(coll_pos))

# python extract_colls.py 擦 -s 2 -hp V N -d 3 -cp V N
# python extract_colls.py 目標詞 -s 字數 -hp 目標詞詞性 -d 距離 -cp 搭配詞詞性
