import sys
import os
from collections import Counter
train_file = "/Users/yuchenlin/Documents/GitHub/neural-symbolic-ner/RuleNER/onto.train.ner.names"
test_file = "/Users/yuchenlin/Documents/GitHub/neural-symbolic-ner/RuleNER/onto.test.ner.names"
train_file = sys.argv[1]
test_file = sys.argv[2]

type_frequence = dict()
most_common_type_dict = dict()

def get_entity_dic(filename):
    train_entity_dic = dict()
    with open(filename, encoding='utf8') as f:
        cur_tag = None
        cur_ent = None
        text = []
        for line in f.readlines():
            line = line.strip()
            if line == "":
                if len(text) > 0:
                    cur_tag = None
                    cur_ent = None
                text = []
                continue
            ls = line.split()
            text.append(ls[0])
            tag = ls[-1]
            if tag.startswith("B"):
                cur_tag = tag[2:]
                cur_ent = ls[0]
            elif tag.startswith("I"):
                cur_ent += " " + ls[0]
            elif tag.startswith("O"):
                if cur_tag is not None and cur_ent is not None:
                    if cur_ent not in train_entity_dic:
                        train_entity_dic[cur_ent] = []
                    train_entity_dic[cur_ent].append(cur_tag)
                    if cur_tag not in type_frequence:
                        type_frequence[cur_tag] = 0
                    type_frequence[cur_tag] += 1
                cur_tag = None
                cur_ent = None

    return train_entity_dic


# print(most_common_type(["PERSON","PERSON","GPE", "GPE", "FAC"]))
def most_common_type(lst):
    cnt = Counter(lst)
    top3 = cnt.most_common(3)
    most_common_type = top3[0][0]
    # deal with tie by global frequency

    if len(top3)>=2 and top3[1][0] == top3[0][0] and type_frequence[top3[1][1]] > type_frequence[most_common_type]:
        most_common_type = top3[1][1]
    if len(top3)>=3 and top3[2][0] == top3[0][0] and type_frequence[top3[2][1]] > type_frequence[most_common_type]:
        most_common_type = top3[2][1]
    return most_common_type



def simple_label(sent, pred, name, tag):

    if name not in " ".join(sent):
        return pred
    name_lst = name.split()
    starts = [i for i, j in enumerate(sent)
              if j == name_lst[0] and sent[i:min(i+len(name_lst), len(sent))] == name_lst]
    for s in starts:
        if len(set(pred[s:s+len(name_lst)])) == 1 and pred[s] == "O":
            pred[s] = "B-" + tag
            for i in range(s+1, s+len(name_lst)):
                pred[i] = "I-" + tag
    return pred

def label_sent(sent, entity_dic):
    pred = ["O"]*len(sent)
    for name in entity_dic:
        #  exactly match the span in the test sentence (case sensitive)
        tag = most_common_type_dict[name]
        pred = simple_label(sent, pred, name, tag)
    return pred

def label_test(testflie, entity_dic):
    result = ""
    with open(testflie, encoding="utf8") as f:
        cur_sent = []
        cur_truth = []
        cur_cnt = 0
        lines = f.readlines()

        corpus = " ".join([l.split()[0] for l in lines if len(l.split()) >= 2])

        # minimize the entity_dic
        print("deleting empty entity; current size: %d"%(len(entity_dic)))
        entity_names = list(entity_dic.keys())
        for name in entity_names:
            if name not in corpus:
                del entity_dic[name]
        print("done deleting current size: %d"%(len(entity_dic)))

        print("building most common type dict")
        for name in entity_dic:
            most_common_type_dict[name] = most_common_type(entity_dic[name])
        print("most common type dict... Done!")


        sents = []
        for l in lines:
            ls = l.strip().split(" ")
            if len(l.split()) >= 2:
                cur_sent.append(ls[0])
            else:
                if len(cur_sent)>0:
                    sents.append(cur_sent)
        len_sents = len((sents))

        cur_sent = []
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                ls = line.split()
                cur_sent.append(ls[0])
                cur_truth.append(ls[-1])
            else:
                assert len(cur_sent) == len(cur_truth)
                if len(cur_sent) > 0:
                    # print(cur_sent)
                    # print(cur_truth)
                    pred = label_sent(cur_sent, entity_dic)
                    assert len(pred) == len(cur_truth)
                    for i in range(len(pred)):
                        result += " ".join([cur_sent[i], cur_truth[i], pred[i]]) + "\n"
                    result += "\n"
                    cur_cnt += 1
                    if cur_cnt % 100 == 0:
                        print("---%d out of %d" % (cur_cnt, len_sents))
                        # if cur_cnt == 500:
                        #     break
                cur_sent = []
                cur_truth = []
                # to process
    return result


print("building entity dictionary")
train_entity_dic = get_entity_dic(train_file)
print("dictionary built")
print("start labeling")
res = label_test(test_file, train_entity_dic)
print("done labeling")

with open("tmp.res", 'w') as f:
    f.write(res)
os.system("./conlleval < tmp.res")
# print(simple_label(["A", "B", "C", "D","E"], pred=["O","O","O","O","B-PER"],name="B C D", tag = "ass"))

