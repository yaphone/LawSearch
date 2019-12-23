#coding=utf-8
import io
import re
import json


class LawSearch:
  def __init__(self):
    self.lawArr = []
    self.lawJson = {}
  def main(self): 
    fs = io.open('C:/Users/zhouy/Desktop/Github/wechat-miniapp/LawSearch/py/xianfa/xianfa.txt', mode='r', encoding='utf-8')
    lawStr = fs.read()
    self.process(lawStr)

  def process(self, lawStr):
    pattern = re.compile('\\n第\\w+条')
    m = pattern.search(lawStr)
    while (m != None):
      index1 = m.span()[0]
      m2 = pattern.search(lawStr, index1 + 1)
      if (m2 == None):
        break
      index2 = m2.span()[0]
      self.lawArr.append(lawStr[index1 + 1 : index2])
      lawStr = lawStr[index2:]
      m = pattern.search(lawStr)
    for law in self.lawArr:
      index1 = law.index('条')
      key = law[:index1 + 1]
      value = law[index1 + 1:]
      self.lawJson[key] = value
    ret = json.dumps(self.lawJson, ensure_ascii=False).replace('\\n', '')
    fs = io.open('C:/Users/zhouy/Desktop/Github/wechat-miniapp/LawSearch/py/xianfa/xianfa_process.txt', mode='w', encoding='utf-8')
    fs.write(ret)  

if __name__ == '__main__':
  lawSearch = LawSearch()
  lawSearch.main()