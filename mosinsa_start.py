import sys
from PyQt5.QtWidgets import *
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from gensim.models import Word2Vec
from scipy.io import mmread
import pickle
from PyQt5 import uic
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QPixmap
import urllib.request
import webbrowser
import random

form_window = uic.loadUiType('ou_recommendation_2.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.hyperlink = None
        self.hyperlink_pants = None
        self.hyperlink_shoes = None

        self.Tfidf_matrix = mmread('./models/Tfidf_outer_review.mtx').tocsr()
        with open('./models/tfidf_outer.pickle', 'rb') as f:
            self.Tfidf = pickle.load(f)
        self.embedding_model = Word2Vec.load('./models/word2vec_outer.model')
        self.df_reviews = pd.read_csv('./crawling_data/CRO/cleaned_outer_one2.csv')
        self.titles = list(self.df_reviews['titles'])
        self.titles.sort()

        model = QStringListModel()
        model.setStringList(self.titles) # 모델이 titles를 넣어 준다.

        completer = QCompleter()
        completer.setModel(model)
        self.le_keyword.setCompleter(completer)


        self.btn_recommendation.clicked.connect(self.btn_slot)
#####추가####
        self.btn_recommendation_2.clicked.connect(self.btn_slot_outer_2)
        self.le_keyword_2.setCompleter(completer)
#####추가####
        #########링크
        self.pushButton.clicked.connect(self.outer_link)
        self.pushButton_2.clicked.connect(self.pants_link)
        self.pushButton_3.clicked.connect(self.shoes_link)




        ####pants#### 1
        self.Tfidf_matrix_pants = mmread('./models/Tfidf_pants_review.mtx').tocsr()
        with open('./models/tfidf_pants.pickle', 'rb') as f:
            self.Tfidf_pants = pickle.load(f)
        self.embedding_model_pants = Word2Vec.load('./models/word2vec_pants.model')
        self.df_reviews_pants = pd.read_csv('./crawling_data/CRO/cleaned_pants_one2.csv')

        self.titles_pants = list(self.df_reviews_pants['titles'])
        self.titles_pants.sort()


        model_pants = QStringListModel()
        model_pants.setStringList(self.titles_pants) # 모델이 titles를 넣어 준다.

        completer_pants = QCompleter()
        completer_pants.setModel(model_pants)
        self.le_keyword.setCompleter(completer_pants)

        self.btn_recommendation.clicked.connect(self.btn_slot_pants)

######추가########
        self.btn_recommendation_3.clicked.connect(self.btn_slot_pants_2)
        self.le_keyword_3.setCompleter(completer)
######추가#######

        ####shoes#### 1
        self.Tfidf_matrix_shoes = mmread('./models/Tfidf_shoes_review.mtx').tocsr()
        with open('./models/tfidf_shoes.pickle', 'rb') as f:
            self.Tfidf_shoes = pickle.load(f)
        self.embedding_model_shoes = Word2Vec.load('./models/word2vec_shoes.model')
        self.df_reviews_shoes = pd.read_csv('./crawling_data/CRO/cleaned_shose_one2.csv')

        self.titles_shoes = list(self.df_reviews_shoes['titles'])
        self.titles_shoes.sort()


        model_shoes = QStringListModel()
        model_shoes.setStringList(self.titles_shoes) # 모델이 titles를 넣어 준다.

        completer_shoes = QCompleter()
        completer_shoes.setModel(model_shoes)
        self.le_keyword.setCompleter(completer_shoes)

        self.btn_recommendation.clicked.connect(self.btn_slot_shoes)

        ######추가########
        self.btn_recommendation_4.clicked.connect(self.btn_slot_shoes_2) #다시실행
        self.le_keyword_4.setCompleter(completer)

        ######추가#######

        ####shoes####
###outer### 2
    def btn_slot(self):
        key_word = self.le_keyword.text()
        if key_word in self.titles:
            recommendation = self.recommendation_by_outer_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword(key_word)

        if recommendation:
            print('debug01')
            print(recommendation[0])
            self.lbl_recommendation.setText(recommendation[0])


            url = recommendation[1]
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02')
            pixmap = QPixmap()
            print('debug03')
            pixmap.loadFromData(image)
            print('debug04')
# #############################################
            self.lbl_recommendation_2.setPixmap(pixmap)
            print('debug05')

            print(recommendation[2])
            hyperlink = recommendation[2]
            hyperlink = hyperlink.replace(' "', '') #지역
            self.hyperlink = hyperlink.replace('"', '') #전역변수
            print(len(hyperlink))

            print('링크클릭')


    ###outer### 2_2
        ###outer### 2
    def btn_slot_outer_2(self):
        key_word = self.le_keyword_2.text()
        if key_word in self.titles:
            recommendation = self.recommendation_by_outer_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword(key_word)

        if recommendation:
            print('debug01')
            print(recommendation[0])
            self.lbl_recommendation.setText(recommendation[0])


            url = recommendation[1]
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02')
            pixmap = QPixmap()
            print('debug03')
            pixmap.loadFromData(image)
            print('debug04')
            # #############################################
            self.lbl_recommendation_2.setPixmap(pixmap)
            print('debug05')

            print(recommendation[2])
            hyperlink = recommendation[2]
            hyperlink = hyperlink.replace(' "', '')
            self.hyperlink = hyperlink.replace('"', '')




    ###outer### 2




    ####pants#### 2


    def btn_slot_pants(self):
        key_word = self.le_keyword.text()
        if key_word in self.titles_pants:
            recommendation = self.recommendation_by_pants_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword_pants(key_word)

        if recommendation:
            print('debug01_1')
            print(recommendation[0])
            self.lbl_recommendation_3.setText(recommendation[0])
            ####pants####

            ##############################################
            url = recommendation[1]
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02_1')
            pixmap = QPixmap()
            print('debug03_1')
            pixmap.loadFromData(image)
            print('debug04_1')
            # #############################################

            self.lbl_recommendation_5.setPixmap(pixmap)
            print('debug05_1')

            print(recommendation[2])
            hyperlink_pants = recommendation[2]
            hyperlink_pants = hyperlink_pants.replace(' "', '')
            self.hyperlink_pants = hyperlink_pants.replace('"', '')




        # ####pants####

    ####pants#### 2_2

    def btn_slot_pants_2(self):
        key_word = self.le_keyword_3.text()
        if key_word in self.titles_pants:
            recommendation = self.recommendation_by_pants_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword_pants(key_word)

        if recommendation:
            print('debug01_1')
            print(recommendation[0])
            self.lbl_recommendation_3.setText(recommendation[0])
            ####pants####

            ##############################################
            url = recommendation[1]
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02_1')
            pixmap = QPixmap()
            print('debug03_1')
            pixmap.loadFromData(image)
            print('debug04_1')
            # #############################################

            self.lbl_recommendation_5.setPixmap(pixmap)
            print('debug05_1')

            print(recommendation[2])
            hyperlink_pants = recommendation[2]
            hyperlink_pants = hyperlink_pants.replace(' "', '')
            self.hyperlink_pants = hyperlink_pants.replace('"', '')



        ####pants####

        ####pants####2_2

        ####shoes#### 2
    def btn_slot_shoes(self):
        key_word = self.le_keyword.text()
        if key_word in self.titles_shoes:
            recommendation = self.recommendation_by_shoes_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword_shoes(key_word)

        if recommendation:
            print('debug01_1')
            print(recommendation[0])
            self.lbl_recommendation_4.setText(recommendation[0])
            ####pants####

            ##############################################
            url = recommendation[1]
            print(recommendation[1])
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02_1')
            pixmap = QPixmap()
            print('debug03_1')
            pixmap.loadFromData(image)
            print('debug04_1')
            # #############################################

            self.lbl_recommendation_6.setPixmap(pixmap)
            print('debug05_1')

            print(recommendation[2])
            hyperlink_shoes = recommendation[2]
            hyperlink_shoes = hyperlink_shoes.replace(' "', '')
            self.hyperlink_shoes = hyperlink_shoes.replace('"', '')



        ####shoes####

        ####shoes#### 2_2
    def btn_slot_shoes_2(self):
        key_word = self.le_keyword_4.text()
        if key_word in self.titles_shoes:
            recommendation = self.recommendation_by_shoes_title(key_word)

        else:
            recommendation = self.recommendation_by_keyword_shoes(key_word)

        if recommendation:
            print('debug01_1')
            print(recommendation[0])
            self.lbl_recommendation_4.setText(recommendation[0])
            ####pants####

            ##############################################
            url = recommendation[1]
            print(url)
            url = url.replace(" '", '')
            url = url.replace("'", '')
            image = urllib.request.urlopen(url).read()

            print('debug02_1')
            pixmap = QPixmap()
            print('debug03_1')
            pixmap.loadFromData(image)
            print('debug04_1')
            # #############################################

            self.lbl_recommendation_6.setPixmap(pixmap)
            print('debug05_1')
            print(recommendation[2])
            hyperlink_shoes = recommendation[2]
            hyperlink_shoes = hyperlink_shoes.replace(' "', '')
            self.hyperlink_shoes = hyperlink_shoes.replace('"', '')

        ####shoes####2_2

    def getRecommendation(self, cosin_sim):
        # print('debug01')
        simScore = list(enumerate(cosin_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
        simScore = simScore[:11]
        print(len(simScore))
        outerIdx = [i[0] for i in simScore]
        print(outerIdx)
        print(len(outerIdx))
        print('1111')
        recouterList = self.df_reviews.iloc[outerIdx, 0]
        url = self.df_reviews.iloc[outerIdx, 2]
        hyperlink = self.df_reviews.iloc[outerIdx, 3]

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        j = random.choice(numbers)
        recouterList = recouterList[j-1:j]
        url = url[j-1:j]
        hyperlink = hyperlink[j-1:j]



        url = list(url)[0]
        recouterList = list(recouterList)[0]
        hyperlink = list(hyperlink)[0]
        print(recouterList)
        print(hyperlink)

        print('2222')


        return recouterList, url, hyperlink


        ####pants#### 3
    def getRecommendation_pants(self, cosin_sim):
        # print('debug01')
        simScore = list(enumerate(cosin_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
        simScore = simScore[:11]
        pantsIdx = [i[0] for i in simScore]
        print(pantsIdx)
        print('1111_1')
        repantsList = self.df_reviews_pants.iloc[pantsIdx, 0]
        url_pants = self.df_reviews_pants.iloc[pantsIdx, 2]
        hyperlink_pants = self.df_reviews_pants.iloc[pantsIdx, 3]


        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        j = random.choice(numbers)
        repantsList = repantsList[j-1:j]
        url_pants = url_pants[j-1:j]
        hyperlink_pants = hyperlink_pants[j-1:j]



        url_pants = list(url_pants)[0]
        repantsList_pants = list(repantsList)[0]
        hyperlink_pants = list(hyperlink_pants)[0]
        print(repantsList_pants)



        print(hyperlink_pants)

        print('2222_1')


        return repantsList_pants, url_pants, hyperlink_pants

        ####pants####


        ####shoes#### 3
    def getRecommendation_shoes(self, cosin_sim):
        # print('debug01')
        simScore = list(enumerate(cosin_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
        simScore = simScore[:11]
        shoesIdx = [i[0] for i in simScore]
        print(shoesIdx)
        print('1111_3')
        reshoesList = self.df_reviews_shoes.iloc[shoesIdx, 0]
        url_shoes = self.df_reviews_shoes.iloc[shoesIdx, 2]
        hyperlink_shoes = self.df_reviews_shoes.iloc[shoesIdx, 3]

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        j = random.choice(numbers)
        reshoesList = reshoesList[j-1:j]
        url_shoes = url_shoes[j-1:j]
        hyperlink_shoes = hyperlink_shoes[j-1:j]


        url_shoes = list(url_shoes)[0]
        reshoesList_shoes = list(reshoesList)[0]
        hyperlink_shoes = list(hyperlink_shoes)[0]
        print(reshoesList_shoes)
        print(hyperlink_shoes)
        print('2222_3')


        return reshoesList_shoes, url_shoes, hyperlink_shoes

        ####shoes####


    def recommendation_by_outer_title(self, title):
        outer_idx = self.df_reviews[self.df_reviews['titles'] == title].index[0]
        cosine_sim = linear_kernel(self.Tfidf_matrix[outer_idx], self.Tfidf_matrix)

        recommendation = self.getRecommendation(cosine_sim)
        recommendation = '\n'.join(list(recommendation[1:]))

        return recommendation

        ### pants#### 5
    def recommendation_by_pants_title(self, title):
        pants_idx = self.df_reviews_pants[self.df_reviews_pants['titles'] == title].index[0]
        cosine_sim = linear_kernel(self.Tfidf_matrix_pants[pants_idx], self.Tfidf_matrix_pants)

        recommendation = self.getRecommendation_pants(cosine_sim)
        recommendation_pants = '\n'.join(list(recommendation[1:]))

        return recommendation_pants
        ### pants####

        ### shoes#### 5
    def recommendation_by_shoes_title(self, title):
        shoes_idx = self.df_reviews_shoes[self.df_reviews_shoes['titles'] == title].index[0]
        cosine_sim = linear_kernel(self.Tfidf_matrix_shoes[shoes_idx], self.Tfidf_matrix_shoes)

        recommendation = self.getRecommendation_shoes(cosine_sim)
        recommendation_shoes = '\n'.join(list(recommendation[1:]))

        return recommendation_shoes
        ### shoes####


    def recommendation_by_keyword(self, keyword):
        if keyword:
            keyword = keyword.split()[0]
            try:
                sim_word = self.embedding_model.wv.most_similar(keyword, topn=10)
            except:
                self.lbl_recommendation_2.setText('제가 모르는 단어에요 ㅠㅠ')
                return 0
            words = [keyword]
            for word, _ in sim_word:
                words.append(word)
            sentence = []
            count = 10
            for word in words:
                sentence = sentence + [word] * count
                count -= 1
            sentence = ' '.join(sentence)
            print(sentence)
            sentence_vec = self.Tfidf.transform([sentence])
            cosine_sim = linear_kernel(sentence_vec, self.Tfidf_matrix)
            recommendation = self.getRecommendation(cosine_sim)
            # titles = '\n'.join(list(recommendation.loc[:, 'titles']))

            # recommendation = '\n'.join(list(recommendation[:10]))
            print('123')
            return recommendation

        else:
            return 0 # 빈 문자열일 때 0을 리턴한다.

        ### pants#### 6
    def recommendation_by_keyword_pants(self, keyword):
        if keyword:
            keyword = keyword.split()[0]
            try:
                sim_word = self.embedding_model_pants.wv.most_similar(keyword, topn=10)
            except:
                self.lbl_recommendation_5.setText('제가 모르는 단어에요 ㅠㅠ')
                return 0
            words = [keyword]
            for word, _ in sim_word:
                words.append(word)
            sentence = []
            count = 10
            for word in words:
                sentence = sentence + [word] * count
                count -= 1
            sentence = ' '.join(sentence)
            print(sentence)
            sentence_vec = self.Tfidf_pants.transform([sentence])
            cosine_sim = linear_kernel(sentence_vec, self.Tfidf_matrix_pants)
            recommendation_pants = self.getRecommendation_pants(cosine_sim)

            print('123_2')
            return recommendation_pants

        else:
            return 0 # 빈 문자열일 때 0을 리턴한다.
        ### pants####


        ### shoes#### 6
    def recommendation_by_keyword_shoes(self, keyword):
        if keyword:
            keyword = keyword.split()[0]
            try:
                sim_word = self.embedding_model_shoes.wv.most_similar(keyword, topn=10)
            except:
                self.lbl_recommendation_6.setText('제가 모르는 단어에요 ㅠㅠ')
                return 0
            words = [keyword]
            for word, _ in sim_word:
                words.append(word)
            sentence = []
            count = 10
            for word in words:
                sentence = sentence + [word] * count
                count -= 1
            sentence = ' '.join(sentence)
            print(sentence)
            sentence_vec = self.Tfidf_shoes.transform([sentence])
            cosine_sim = linear_kernel(sentence_vec, self.Tfidf_matrix_shoes)
            recommendation_shoes = self.getRecommendation_shoes(cosine_sim)

            print('123_3')
            print(recommendation_shoes)
            return recommendation_shoes


        else:
            return 0 # 빈 문자열일 때 0을 리턴한다.
        ### shoes####

    ####link####
    def outer_link(self):
        if self.hyperlink:
            webbrowser.open('{}'.format(self.hyperlink))

    def pants_link(self):
        if self.hyperlink_pants:
            webbrowser.open('{}'.format(self.hyperlink_pants))

    def shoes_link(self):
        if self.hyperlink_shoes:
            webbrowser.open('{}'.format(self.hyperlink_shoes))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())