import spacy
import sys
import os

# https://note.com/npaka/n/n6fa359ac611c
# システム辞書のパス
sys_dic_path = ''
for path in sys.path:
    path = path+'/sudachidict_core/resources/system.dic'
    if os.path.exists(path):
        sys_dic_path = path
        break
print('sys_dic_path:', sys_dic_path)

# ユーザー辞書のパス
user_dic_path = os.getcwd()+'/user.dic'
print('user_dic_path:', user_dic_path)

# sudahci.jsonのパス
sudachi_path = None
for path in sys.path:
    path = path+'/sudachipy/resources/sudachi.json'
    if os.path.exists(path):
        sudachi_path = path
        break
print('sudachi_path:', sudachi_path)

# userDictの追加
if sudachi_path != None:
    lines = []
    with open(sudachi_path,'r',encoding='utf-8') as f:
        lines = f.readlines()
    for i in range(len(lines)-1):
        if lines[i].find('"characterDefinitionFile"') >= 0 and lines[i+1].find('"userDict"') < 0:
            lines.insert(i+1,'    "userDict" : ["'+user_dic_path.replace("\\","\\\\").replace("/","\\\\")+'"],\n')
            with open(sudachi_path, 'w', encoding='utf-8', newline='\n') as f:
                f.writelines(lines)
            print('update')
            break

nlp = spacy.load('ja_ginza')
doc = nlp('となりのゆゆこのグルメ')
for sent in doc.sents:
    for token in sent:
        print(token.i)
    print('EOS')

