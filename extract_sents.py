import glob
import gzip
import json
from words_filter import check_head
from collections import defaultdict
from tqdm import tqdm


def line_to_tuple(line):
    words = line.split('\u3000')
    return [tuple(word_pos[:-1].rsplit('(', 1)) for word_pos in words]


def extract_text(file):
    texts = []
    is_text = False
    for line in gzip.open(file, 'rt').readlines():
        line = line.strip()

        if line == '<TEXT>':
            is_text = True
            continue
        elif line == '</TEXT>':
            is_text = False

        if is_text and not line.startswith(('<', '</')):
            texts.append(line_to_tuple(line))
    return texts


def preprocess(files):
    for file in tqdm(files):
        yield extract_text(file)


def filter_data(files, head, size, head_pos):
    sents = defaultdict(list)
    for texts in preprocess(files):
        text = check_head(texts, head, size, head_pos)
        for word, lines in text.items():
            sents[word].extend([line for line in lines if line not in sents[word]])
    return sents


def main(head, size, head_pos):
    paths = ['/atom/corpus/general/tagged_ch_gigaword/data/cna_sent/*',
             '/atom/corpus/general/UCD/gigaword_format/udn/*']
    cna_files, udn_files = [glob.glob(path) for path in paths]

    cna_data = filter_data(cna_files, head, size, head_pos)
    udn_data = filter_data(udn_files, head, size, head_pos)

    json.dump(cna_data, open(f"{head}_cna.json", 'w'))
    json.dump(udn_data, open(f"{head}_udn.json", 'w'))
    # {'head(pos)':[(word, pos), (word,pos),...], ...}
    return cna_data, udn_data


if __name__ == '__main__':
    from parse_comand import parse_command
    arg = parse_command()
    head, size, head_pos = arg[:3]
    main(head, size, tuple(head_pos))

# python extract_sents.py 擦 -s 2 -hp V N 
