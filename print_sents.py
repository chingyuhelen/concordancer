import json


def tuple_to_string(token_poses):
    return '\u3000'.join('('.join(token_pos)+')' for token_pos in token_poses)


def get_set(data):
    sents = []
    for _, texts in data.items():
        for token_poses in texts:
            sents.append(tuple_to_string(token_poses))
    return set(sents)


def to_txt(data, filename):
    sents = get_set(data)
    with open(f"{filename}.txt", 'w') as f:
        for sent in sents:
            print(sent, file=f)


def main(head):
    cna_data = json.load(open(f"{head}_cna.json"))
    udn_data = json.load(open(f"{head}_udn.json"))
    to_txt(cna_data, f"{head}_cna")
    to_txt(udn_data, f"{head}_udn")


if __name__ == '__main__':
    import sys
    head = sys.argv[1]
    main(head)

# python print_sents.py 擦
