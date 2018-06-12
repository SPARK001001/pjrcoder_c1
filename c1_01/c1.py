# -*- encoding:utf-8 -*-
import random
import re

import requests
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nihao')


def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    print p1.findall(str)


if __name__ == "__main__":
    # qiushibaike()
    # demo_string()
    # print 5 ^ 3
    # random.seed(1)
    # print 1, int(random.random()*100)
    # print 2, random.randint(0, 200)
    # print 3, random.choice(range(0, 100))
    # print 4, random.sample(range(0, 100), 4)
    # a = [1, 2, 3, 4, 5]
    # random.shuffle(a)
    # print 5, a
    demo_re()