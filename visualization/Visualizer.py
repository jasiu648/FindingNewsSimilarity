import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
from wordcloud import WordCloud
from collections import Counter
from nltk.tokenize import word_tokenize

class Visualizer():

    @staticmethod
    def generate_wordcloud(text):
         # Generate a word cloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        # Display the generated word cloud using matplotlib
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Turn off axis labels
        plt.show()
        return wordcloud

        
    def generate_bar_plot(tokens):
        tokens = word_tokenize(text)
        text_list = Counter(tokens)

        unique_words = list(text_list.keys())
        frequencies = list(text_list.values())

        sorted_indices = sorted(range(len(frequencies)), key=lambda k: frequencies[k], reverse=True)
        sorted_indices = sorted_indices[:10]
        unique_words = [unique_words[i] for i in sorted_indices]
        frequencies = [frequencies[i] for i in sorted_indices]

        # Plot the bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(unique_words)), frequencies, tick_label=unique_words, color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Word Frequency Bar Plot')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def generate_visual_results(result):

        data = {
            'percentage': [result, 1 - result],
            'label'     : ['70%','30%'],
            'color'     : ['blue','lightgray']
        }

        df = pd.DataFrame(data)

        chart = alt.Chart(df).mark_arc(
            innerRadius=100,
            outerRadius=150
        ).encode( 
            theta='percentage',
            color=alt.Color('color', scale=None),
            tooltip='label'
        ).properties(
            width=300,
            height=300
        )

        text = alt.Chart(df.head(1)).mark_text(
            align='center',
            baseline='middle',
            fontSize=60,
            fontWeight='bold',
            color='black'
        ).encode(
            text='label',
            color=alt.Color('color', scale=None)
        ).properties(
            width=300,
            height=300
        )

        chart = (chart + text
        ).configure_view(
            strokeWidth=0
        )
        return chart

    def generate_ner_comparsion(entities1, entities2):
        all_entities = set(entities1 + entities2)
        
        # Extract common named entities
        common_entities = set(entities1) & set(entities2)

        # Count the occurrences of each entity for setting the width
        entity_counts = Counter(entities1 + entities2)

        # Visualize all named entities
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.barh([str(entity) for entity in all_entities], [entity_counts[entity] for entity in all_entities], color='lightblue')
        plt.xlabel('Frequency')
        plt.ylabel('Named Entities')
        plt.title('All Named Entities')

        # Visualize common named entities
        plt.subplot(1, 2, 2)
        plt.barh([str(entity) for entity in common_entities], [entity_counts[entity] for entity in common_entities], color='orange')
        plt.xlabel('Frequency')
        plt.ylabel('Named Entities')
        plt.title('Common Named Entities')

        plt.tight_layout()
        plt.show()