from argparse import ArgumentParser


def parse_command():
    parser = ArgumentParser()
    parser.add_argument("head", help="traget word")
    parser.add_argument("-s", "--size", default=2, type=int,
                        help='head size')
    parser.add_argument("-hp", "--head_pos", nargs='*',
                        help='the pos tags of head')
    # parser.add_argument("-n", "--news_name",
                        # help='the name of the newspaer')
    parser.add_argument("-d", "--dist", default=1, type=int,
                        help='the distance of head and collocates')
    parser.add_argument("-cp", "--coll_pos", nargs='*', 
                        help='the pos tags of the collocates')

    arg = parser.parse_args()
    return arg.head, arg.size, arg.head_pos, arg.dist, arg.coll_pos
