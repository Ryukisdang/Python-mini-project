import tkinter as tk
import openai
import requests

# Set up API credentials and parameters
openai.api_key = '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'
bing_api_key = 'AqonRfMTLGO1_0yFlX9ATPa1cmiCTBA6KAC8QaQy7RilfT76er7UQmjWAUuFKpRZ'

def ask_chatgpt(question):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def search_movies(query):
    # Search for movies using Bing API
    url = f'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
    params = {'q': query, 'count': 5, 'responseFilter': 'webPages'}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['webPages']['value']

def get_movie_recommendations(genre):
    # Generate movie recommendations using ChatGPT
    prompt = f"Can you recommend any good {genre} movies?"
    response = ask_chatgpt(prompt + '\n')
    return response.split('\n')

def get_movie_details(movie):
    # Fetch additional movie details using Bing search
    query = f"{movie} movie details"
    search_results = search_movies(query)
    return search_results[0]['snippet']

def show_recommendations():
    # Retrieve user's genre preference from the input field
    genre = genre_entry.get()

    # Retrieve movie recommendations
    recommendations = get_movie_recommendations(genre)

    # Display the recommendations
    recommendation_text = ''
    for i, movie in enumerate(recommendations, start=1):
        details = get_movie_details(movie)
        recommendation_text += f"{i}. {movie}\n   {details}\n\n"

    recommendations_label.config(text=recommendation_text)

# Create the GUI window
window = tk.Tk()
window.title("Movie Recommendation Chatbot")

# Create and arrange GUI elements
genre_label = tk.Label(window, text="What genre of movies do you like?")
genre_label.pack()

genre_entry = tk.Entry(window)
genre_entry.pack()

recommend_button = tk.Button(window, text="Get Recommendations", command=show_recommendations)
recommend_button.pack()

recommendations_label = tk.Label(window, text="")
recommendations_label.pack()

# Run the GUI event loop
window.mainloop()
