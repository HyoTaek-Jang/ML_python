#  이걸 실제로 쓸 일은 없고 countvectorizer 이런 클래스 잘 되있음 ㅎㅎ...  sklearn 모듈에서..ㅎ
import operator
import os


# 폴더명을 입력하면 파일명 리스트를 가져옴
def get_file_list(dir_name):
    return os.listdir(dir_name)


# 파일별로 내용읽기
def get_content(file_list):
    # 80개의 파일에서 야구에 관한건지 축구에 관한건지 0,1이 몇갠지 적음
    y_class = []
    x_text = []
    class_dict = {
        # 1~4 야구, 5~8 축구
        1: '0', 2: '0', 3: '0', 4: '0', 5: '1', 6: '1', 7: '1', 8: '1'
    }

    for file_name in file_list:
        try:
            # cp949윈도우즈파일, utf8 맥이나 리눅스파일
            f = open(file_name, 'r', encoding='cp949')
            # os.sep '\ or /'을 뜻함
            # 경로에서 파일명을 가져오고 파일명을 _로 나눠서 앞에 번호를 가져옴
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
            #x_test에는 내용, y_class 는 야군지 축군지
    return x_text,y_class

# 하나의 단어가 들어오면 의미없는 문장부호를 제거하는것
def get_cleaned_text(word):
    import re
    # 패턴에 일치되는 문자열을 다른 문자열로 바꿔주는 것
    text = re.sub('\W+','',word.lower())
    return text

def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleaned_words = [get_cleaned_text(word) for words in text for word in words]

    from _collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i
    return corpus_dict

def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    # 각 문서에서 똑같은 방식으로 단어를 불러와서 우리가 만든 corpus에 몇번째 단어인지 쭉 리스트로 나열함. 이걸 80개 만듬. 즉 투 디멘셔널 리스트
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]

    # for에서 _는 사용안하겠다. 이 코드는 총 도큐먼트 갯수와 단어장의 갯수로 만든 백터를 0으로 채움 투 디멘셔널.
    x_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]

    for i, text in enumerate(word_number_list):
        for word_number in text:
            x_vector[i][word_number] +=1
    return x_vector

# 두 문서를 비교하는것. 아래 식을 코드로 나타냄
import math
def get_cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def get_similarity_score(X_vector, source):
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list

# 메인함수
if __name__ == "__main__":
    dir_name = 'data'
    file_list = get_file_list(dir_name)
    # 경로를 파일명과 폴더를 이어줌. 조인을 '\'로 해도 되지만 맥과 윈도우는 폴더를 연결하는 문자가 달라서 os.path를 사용함
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]

    x_text, y_class = get_content(file_list)

    # 총 문서에 나온 단어가 4024이기에 백터는 4024개다 보통 의미없는 단어나 너무 적은거는 제거함 여기선 패스.
    corpus = get_corpus_dict(x_text)

    # 각 문서마다 corpus에 단어가 몇개가 있냐
    x_vector = get_count_vector(x_text, corpus)

    selectNum = 38

    compare_value = {i:v for i,v in enumerate(get_similarity_score(x_vector, selectNum))}
    sorted_dict = sorted(compare_value.items(), reverse=True,key=operator.itemgetter(1))


    print(sorted_dict)

    list = []
    baseball = 0
    soccer = 0

    for i in range(1,11):
        if(sorted_dict[i][0] > 39):
            soccer+=1
        else:
            baseball+=1

    print("select Num : {} // baseball : {baseball}, soccer : {soccer}".format(selectNum, baseball=baseball, soccer=soccer))