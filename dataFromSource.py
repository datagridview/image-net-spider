from bs4 import BeautifulSoup
import re
import requests

class Image_net:

    def dict_id_to_word(self):
        dict = {}
        file = open('dataSource.xml','r')
        b = BeautifulSoup(file, "xml")
        a = re.findall(r'wnid=\".*?\"\swords=\".*?"',str(b.contents[0]))
        for item in a:  
            value_list = item.split("\"")
            dict[value_list[1]]=value_list[3]
        return dict
    
    def get_mother_wnid_list(self):
        return self.dict_id_to_word().keys()

    def list_of_wnids(self):
        return self.dict_id_to_word().keys()

    def list_one_of_wnids_urls(self, wnid):
        dict = {}
        url = 'http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=' + str(wnid)
        raw_text = requests.get(url)
        raw_text = raw_text.text
        a = re.findall(r'n.*', raw_text)
        for item in a:  
            value_list = item.split(' ')
            dict[value_list[0]]=value_list[1].split('\r')[0]
        return dict
    
    def get_all_wnid_id(self,wnid):
        return self.list_one_of_wnids_urls(wnid).keys()

    def get_all_links(self,wnid):
        return self.list_one_of_wnids_urls(wnid).values()
    
    def download 
    
    


a = Image_net()
for a in a.get_mother_wnid_list():
    print(a)
# print(a.get_all_links('n04344873'))