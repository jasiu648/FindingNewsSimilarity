from sentence_transformers import SentenceTransformer, util
from Model import *

class BertModel(Model):
    
    def Transform(self,text1, text2):
        # Load a pre-trained BERT model
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        # Encode the texts into BERT embeddings
        embeddings = model.encode([text1, text2], convert_to_tensor=True)

        # Calculate cosine similarity between the embeddings
        similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])

        return similarity_score.item()