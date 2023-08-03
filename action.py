import nltk
# nltk.download('punkt')

class Word:
    def contains_sub_sentence(sentence, sub_sentence):
        sentence_tokens = nltk.word_tokenize(sentence)
        sub_sentence_tokens = nltk.word_tokenize(sub_sentence)
        try:
            start_index = sentence_tokens.index(sub_sentence_tokens[0])
        except ValueError:
            return False
        end_index = start_index + len(sub_sentence_tokens)
        if sentence_tokens[start_index:end_index] == sub_sentence_tokens:
            return True
        else:
            return False
    def word_check(document,action_list):
        res = []
        for line in document:
            line = line.lower()
            for a in action_list:
                if Word.contains_sub_sentence(line,a):
                   res.append(line)
        d = [*set(res)]    
     
        return d

    

# contains_action(document,sentence)    