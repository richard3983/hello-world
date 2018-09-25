datasets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R']
loaded_data = {}
counter = 0
sentences_dic = []
for data_id in datasets:
    test_set = BeautifulSoup(open("character/LCMC_"+str(data_id)+".xml"))
    words = []
    
    sen = 0
    #firsstrow = soup.find("s", {"n": "0001"})
    for sentences in test_set.find_all("s"):
        words[:] = []
        for word in sentences.find_all(["w", "c"]):
            word = word.string
            words.append(word)
            sentence = "".join(words)

        sentences_dic.append(sentence)
        
