# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:33:19 2025

@author: pathouli
"""

#user function
def hello_world():
    print ("hello world")

#user function wuth inputs
def jd_fun(c_a, c_b):
    corp_a_t = set(c_a.split())
    corp_b_t = set(c_b.split())

    the_int_x = corp_b_t.intersection(corp_a_t)
    the_u_x = corp_a_t.union(corp_b_t)

    jd = len(the_int_x) / len(the_u_x)
    return jd

def clean_text(str_in):
    import re
    corp_c_clean = re.sub(
        "[^A-Za-z]+", " ", str_in).strip().lower()
    return corp_c_clean

def word_freq(str_i):
    import collections
    w_f = dict(collections.Counter(str_i.split()))
    return w_f

def file_opener(p_in):
    try:
        the_text = ""
        f = open(p_in, mode="r", encoding="utf-8")
        the_text = clean_text(f.read())
        f.close()
    except:
        print (p_in)
        pass
    return the_text

def file_crawler(path_in):
    import os
    import pandas as pd
    m_pd = pd.DataFrame()
    for root, dirs, files in os.walk(path_in, topdown=False):
       for name in files:
          #print(os.path.join(root, name))
          tmp_txt = file_opener(root + "/" + name)
          if len(tmp_txt) != 0:
              t_pd = pd.DataFrame(
                  {"body": tmp_txt, "label": root.split("/")[-1:][0]},
                   index=[0])
              m_pd = pd.concat([m_pd, t_pd], ignore_index=True)
    return m_pd

def rem_sw(str_in):
    from nltk.corpus import stopwords
    sw = stopwords.words('english')
    str_ex_tok = str_in.split()
    n_l = list()
    for word in str_ex_tok:
        if word not in sw:
            n_l.append(word)
    n_l = " ".join(n_l)
    return n_l

def stem_fun(str_in, sw_in):
    from nltk.stem import PorterStemmer, WordNetLemmatizer
    if sw_in == "ps":
        ps = PorterStemmer()
    else:
        ps = WordNetLemmatizer()
    t_list = list()
    for word in str_in.split():
        if sw_in == "ps":
            t_ps = ps.stem(word)
        else:
            t_ps = ps.lemmatize(word)
        t_list.append(t_ps)
    t_list = " ".join(t_list)
    return t_list