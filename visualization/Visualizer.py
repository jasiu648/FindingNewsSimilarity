from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

class Visualizer():

    @staticmethod
    def generate_wordcloud(text):

    # Generate a word cloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        # Display the generated word cloud using matplotlib
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Turn off axis labels
        
    def generate_bar_plot(tokens):
        pass

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

    def generate_ner_comparsion(ner1, ner2):
        pass