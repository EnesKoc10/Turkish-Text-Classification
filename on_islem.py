import pandas as pd
import re
import snowballstemmer

# Sayısal değerlerin kaldırılması
def remove_numeric(value):
    bfr = [item for item in value if not item.isdigit()]
    bfr = "".join(bfr)
    return bfr

# Emojilerin kaldırılması
def remove_emoji(value):
    bfr = re.compile("[\U00010000-\U0010ffff]",flags=re.UNICODE)
    bfr = bfr.sub(r'',value)
    return bfr

# tek karakterli ifadelerin kaldırılması
def remove_single_chracter(value):
    return re.sub(r'(?:^| )\w(?:$| )','',value)

# noktalama işaretlerin kaldırılması
def remove_noktalama(value):
    return re.sub(r'[^\w\s]','',value)

# linlerin kaldırılması
def remove_link(value):
    return re.sub('((www\.[^\s]+)|(https://[^\s]+))','',value)

# hastaglarin kaldırılması
def remove_hashtag(value):
    return re.sub(r'#[^\s]+','',value)

# Kullanıcı adların kaldırılması
def remove_username(value):
    return re.sub('@[^\s]+','',value)

# Kök indirgeme ve stop
def stem_word(value):
    stemmer = snowballstemmer.stemmer("turkish")
    value = value.lower()
    value = stemmer.stemWords(value.split())
    stop_words= ['acaba', 'ama','çok', 'çünkü',
             ' aslında','az', 'bazı', 'belki','biri',
             'birşey','birkaç','da', 'daha', 'de', 'defa',
             'diye','eğer','en', 'gibi', 'hem','her', 'hiç',
             'için', 'ile', 'kez', 'ki', 'kim', 'nasıl',
             'biz', 'bu',' hep','hepsi', 'ne', 'neden',
             'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o',
             'sanki', 'tüm', 've', 'veya', 'ya','bir',
             ' İki', 'dört', 'beş', 'yedi', 'şekiz', 'dokuz','on']
    value = [item for item in value if not item in stop_words]
    value = ' '.join(value)
    return value

def pre_processing(value):
    return [remove_numeric(remove_emoji
                           (remove_single_chracter
                            (remove_noktalama
                             (remove_link
                              (remove_hashtag
                               (remove_username
                                (stem_word(word)))))))) for word in value.split()]

# Boşlukların kaldırılması
def remove_space(value):
    return [item for item in value if item.strip()]
