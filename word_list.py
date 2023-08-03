from action import Word
def action(text):
    document = text
    #add list acording to to our need
    action_list = ["issue","ticket","due","jira","github","Action Item","submit","assign","i want you","will be","need to","Let's"," to do","work on"]
    decision_list = ["tomorrow","tonight","Decision","goal","let's stick to it"]
    callout_list = ["take note","competitor","Callout","let's summarize","summary","important","risk","deadline"]
    #pass document and action list
    d = Word.word_check(document,action_list)

    return d
