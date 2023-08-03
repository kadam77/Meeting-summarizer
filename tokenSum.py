import pickle,createPdf

pipe = pickle.load(open("samsum_summarry_model.pk", 'rb'))



def summary(text):
    # print(len(text))
    generated_summary=""
    if not text:
        return generated_summary
    elif(len(text)<1000):
        prediction = pipe.predict(text)
        generated_summary = prediction[0]["summary_text"]
        return generated_summary
    
    else:
        chunks = split_text(text,500)
        for chunk in chunks:
            # print(len(chunk))
            prediction = pipe.predict(chunk)
            generated_summary = generated_summary+"\n\n"+prediction[0]["summary_text"]+" "
     
    print("summary:",generated_summary)
    return generated_summary




def split_text(text, chunk_size=500):
    """
    Splits a text into chunks of size `chunk_size`.
    """
    words = text.split()
    chunks = []
    chunk = []
    word_count = 0
    totlen=0
    for word in words:
        if totlen<=1010:
            totlen+=len(word)
            if(totlen>=1010):
                break
            chunk.append(word)
            word_count += 1
            # totlen+=len(word)
        
        if word_count >= chunk_size or totlen>=1000:
            print(len(chunk))

            chunks.append(" ".join(chunk))
            chunk = []
            word_count = 0
            totlen=0
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

print("end")