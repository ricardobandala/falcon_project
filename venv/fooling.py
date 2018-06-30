from collections import Counter


def triple_double(num1: int, num2: int):

    def has_frequency(value: int, frequency: int):
        # convert to list, get the top most_common, get the last parameter compare with the given frequency
        return Counter(list(str(value))).most_common(1)[0][-1] >= frequency

    return has_frequency(value=num1, frequency=3) & has_frequency(value=num2, frequency=2)


# print(triple_double(451999277, 41177722899) == 1)
# print(triple_double(1222345, 12345) == 0)
# print(triple_double(12345, 12345) == 0)
# print(triple_double(666789, 12345667) == 1)
# print(triple_double(10560002, 100) == 1)


def to_camel_case(text: str):

    words = text.replace('_', ' ').replace('-', ' ').split()

    # for index, word in enumerate(words):
    #     if index > 0:
    #         words[index] = word[0].upper() + word[1:]

    words = words[0] + ''.join([word[0].upper() + word[1:] for index, word in enumerate(words) if index > 0]) if len(words) > 1 else words

    words = ''.join(words)

    print(words)

to_camel_case("opopPPo--ss")


# # print({x for x in set(str(value)) if x.isdigit()})
# counter = Counter()
#
# wala = Counter([x for x in list(str(value)) if x.isdigit()]).most_common(1).pop()[-1]
# print(wala)
