import tkinter as tk
import openai
import requests
from PIL import Image
from io import BytesIO
from moviepy.editor import *

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

def search_images(query):
    # Search for images using Bing API
    url = f'https://api.bing.microsoft.com/v7.0/images/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
    params = {'q': query, 'count': 5}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return [image['contentUrl'] for image in data['value']]

def generate_video(images):
    # Generate a video from the given images
    clips = []
    for image_url in images:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        clips.append(ImageClip(image).set_duration(1))  # Each image displayed for 1 second

    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile('output.mp4', codec='mpeg4')

    return True

def summarize_and_generate_video():
    # Retrieve user's text input
    text_input = text_entry.get("1.0", tk.END).strip()

    # Generate a summary using ChatGPT
    summary = ask_chatgpt(text_input)

    # Search for related images using Bing API
    images = search_images(summary)

    if images:
        # Generate the video from the downloaded images
        if generate_video(images):
            # Display a success message
            status_label.config(text="Video generation complete!")
        else:
            # Display an error message if video generation fails
            status_label.config(text="Error generating video.")
    else:
        # Display a message if no images are found
        status_label.config(text="No images found for the given summary.")

# Create the GUI window
window = tk.Tk()
window.title("Video Summarization Tool")

# Create and arrange GUI elements
text_label = tk.Label(window, text="Enter the text to summarize:")
text_label.pack()

text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

generate_button = tk.Button(window, text="Generate Video", command=summarize_and_generate_video)
generate_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Run the GUI event loop
window.mainloop()
