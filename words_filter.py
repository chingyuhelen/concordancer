from collections import defaultdict


def is_head(token, pos, head, size, head_pos):
    if head in token and len(token) <= size and pos.startswith(head_pos):
        return True


def check_head(texts, head, size, head_pos):
    head_sents = defaultdict(list)
    for words in texts:
        for token, pos in words:
            if is_head(token, pos, head, size, head_pos) and words not in head_sents[token]:
                head_sents[token].append(words)
    return head_sents


def is_coll(word_pos, coll_pos):
    _, pos = word_pos
    if not coll_pos or pos.startswith(coll_pos):
        return True


def check_colls(head, sents, coll_pos=None, dist=1):
    coll_sents = defaultdict(list)
    for tokens in sents:
        for head_pos, word_pos in zip(tokens, tokens[dist:]):
            if head_pos[0] == head and is_coll(word_pos, coll_pos):
                coll_sents[word_pos[0]].append(tokens)
    return coll_sents
