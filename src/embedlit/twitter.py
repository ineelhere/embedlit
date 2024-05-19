import streamlit as st
import streamlit.components.v1 as components
import requests

def get_twitter_embed_html(tweet_url):
    # Generate the HTML for embedding the tweet
    response = requests.get(f"https://publish.twitter.com/oembed?url={tweet_url}")
    if response.status_code == 200:
        data = response.json()
        return data['html']
    else:
        return "Error: Unable to fetch tweet"

def tweet_embed(tweet_url, height=600, alignment='center'):
    twitter_embed_html = get_twitter_embed_html(tweet_url)
    if "Error" not in twitter_embed_html:
        # Define the alignment styles
        alignment_styles = {
            'left': 'display: flex; justify-content: flex-start;',
            'center': 'display: flex; justify-content: center;',
            'right': 'display: flex; justify-content: flex-end;'
        }
        # Embed the tweet with the specified alignment
        components.html(
            f'<div style="height:{height}px; overflow-y: scroll; {alignment_styles[alignment]}">{twitter_embed_html}</div>',
            height=height
        )
    else:
        st.error(twitter_embed_html)

# # Streamlit app
# st.title("Embed Twitter Video in Streamlit")

# # User input for Twitter URL, height, and alignment
# tweet_url = st.text_input("Enter the Twitter URL:")
# height = st.number_input("Enter the height of the container:", min_value=200, max_value=1200, value=600)
# alignment = st.selectbox("Choose the alignment of the container:", ('left', 'center', 'right'))

# if tweet_url:
#     tweet_embed(tweet_url, height, alignment)
