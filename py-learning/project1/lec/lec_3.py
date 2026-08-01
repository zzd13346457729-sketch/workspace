# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 20:04:11 2025

@author: pathouli
"""

from utils import *
import pandas as pd

data_path = "C:/Users/pathouli/Box Sync/myStuff/academia/torhea/fall_2025/data/"

the_data = file_crawler(data_path)

pd_col_cat = the_data["body"].str.cat(sep=" ")

main_w_f = word_freq(pd_col_cat)

the_data["body_sw"] = the_data["body"].apply(rem_sw)

pd_col_cat_sw = the_data["body_sw"].str.cat(sep=" ")

main_w_f_sw = word_freq(pd_col_cat_sw)

#stemming and lemmatization
#PorterStemmer
#http://snowball.tartarus.org/algorithms/porter/stemmer.html

the_data["body_sw_stem"] = the_data["body_sw"].apply(
    lambda x: (stem_fun(x, "ps")))
the_data["body_sw_lemma"] = the_data["body_sw"].apply(
    lambda x: (stem_fun(x, "lemma")))

pd_col_cat_sw_stem = the_data["body_sw_stem"].str.cat(
    sep=" ")
main_w_f_sw_stem = word_freq(pd_col_cat_sw_stem)

pd_col_cat_sw_lemma = the_data["body_sw_lemma"].str.cat(
    sep=" ")
main_w_f_sw_lemma = word_freq(pd_col_cat_sw_lemma)


#t_corp = "fishing hiking walking run fishes"

#test = stem_fun(t_corp, "lemma")

#stopwords
#str_ex = "the fish and the cat"

#test = rem_sw(str_ex)

#list comprehentsion
# n_l = [word for word in str_ex.split() if word not in sw]
# n_l = " ".join(n_l)

#file i/o operations

# test = file_opener("C:/Users/pathouli/Box Sync/myStuff/academia/torhea/fall_2025/" +
#                    "fun.txt")

# str_fun = "the cat jumped over the couch after the mouse last night"
# tok_fun = str_fun.split()
#slice_pd = my_pd[my_pd["len"] >= 5]
# my_pd = pd.DataFrame()
# for word in set(tok_fun):
#     freq_t = tok_fun.count(word)
#     t_len = len(word)
#     t_pd = pd.DataFrame({
#         "word": word, "freq": freq_t, "len": t_len}, index=[0])
#     my_pd = pd.concat([my_pd, t_pd], ignore_index=True)






