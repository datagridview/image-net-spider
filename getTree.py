import requests
import re

class imageNet():
    root_url = 'http://image-net.org/python/tree.py/SubtreeXML?rootid='
    # id_list = []
    # word_list = set([])
    word_set = set([])
    n = 0
    id_weight = 1
    # def __init__(self):
        
    def get_word(self, rootid):
        the_url = self.root_url + str(rootid)
        xml_page = requests.get(the_url)
        m = re.findall(r'synsetid="\d*', xml_page.text) 
        n = re.findall(r'\swords=".*?"',xml_page.text)
        o =re.findall(r'num_children="\d*',xml_page.text)
        for root, text in zip(m,n): 
            individual_dict = {}
            individual_dict[m + ' ' + o] = n
        return individual_dict

    def get_list(self, rootid, layer):
        my_list = []
        R_to_T = self.get_word(rootid)
        if(layer == 0):
            my_list.append(R_to_T[0])
        for R, T in zip(R_to_T.keys, R_to_T.values):
            Rlist = R.split(' ')
            if Rlist[1] != 0:
                my_list.append(T)
                my_list += self.get_list(Rlist[0], layer+1)
            else:
                my_list.append(T)
        return my_list

    def get_tree(self, rootid):
        list = self.getList(dir, 0, op)
        treeList = []
    # def get_rootid(self,rootid):
        # the_url = self.root_url + str(rootid)
        # xml_page = requests.get(the_url)
        # print('正在读取第'+str(self.n)+'个页面')
        # self.n = self.n + 1
        # m = re.findall(r'synsetid="\d*', xml_page.text) 
        # n = re.findall(r'\swords=".*?"',xml_page.text)
        # for synsetid, synsetWord in zip(m,n):
        #     splitId = synsetid.split('\"')
        #     # if rootid != splitId[1]:
        #     #     self.id_list.append(splitId[1])
        #     # else:
        #     #     pass
        #     splitWord = synsetWord.split('\"')
        #     self.word_set.add(splitId[1]+':'+splitWord[1])
        #     # self.word_list.add(splitWord[1])
        # # print(self.word_set)        
        
        # # print(self.word_list)
        # # print(self.id_list)
    
    def cycle_get(self):
        # for word_id in self.word_set:
        #     _id = word_id.split(':')
        #     self.get_rootid(_id[0])
        # print(self.word_set)

    # def write_in_file(self):
    #     sep = '\n'
    #     with open('C:/Users/ziyexing/Desktop/list_whole.txt', 'w') as f:
    #         f.write(sep.join(self.word_list))
    #         f.close()


i = imageNet()
i.get_rootid(82127)
i.cycle_get()
# i.write_in_file()
