import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import base64
from openai import OpenAI
import os
from PIL import Image, ImageTk  # Import PIL for image handling

# Import your existing create_and_save_candlestick_chart function
# Ensure 'price_data.py' is in the same directory as this script
from price_data import create_and_save_candlestick_chart as cs
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file; for your safety!
# --- Configuration ---
api_key = os.getenv("API_KEY")
# --- OpenAI Configuration (from your provided code) ---
client = OpenAI(
    api_key=api_key,  # Replace with your actual AvalAI API key
    base_url="https://api.avalai.ir/v1",  # Base URL for AvalAI; This line is for Iranian who are under regional limitations; Remove it if you are not in Iran.
)

# --- Function to encode the image to Base64 (from your provided code) ---
def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Image file not found: {image_path}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error encoding image: {e}")
        return None


def _perform_analysis_task(symbol, timeframe, limit, user_prompt):
    """
    Contains the core logic for generating the chart, encoding it,
    calling the OpenAI API, and displaying the results.
    """
    image_path = "test.png"  # This is where your cs() function saves the image
    if(True):
        # 1. Call your existing cs function to generate the candlestick chart
        # 'kucoin' is hardcoded as in your original script.
        # If you want this user-selectable, add an OptionMenu for it.
        print(symbol,timeframe,limit)
        cs(symbol=symbol, timeframe=timeframe, exchange='kucoin', limit=limit)
        # 2. Display the generated chart in the GUI
        img = Image.open(image_path)

        # Define the exact dimensions you want
        desired_width = 500
        desired_height = 300

        # Use Image.resize() to force the exact dimensions
        # Be aware this will distort the image if its original aspect ratio is not 7:5
        img = img.resize((desired_width, desired_height), Image.LANCZOS)  # Use LANCZOS for good quality
        # 3. Get the Base64 string of the image
        base64_image = encode_image(image_path)
        # 4. Call OpenAI API with the encoded image

        prompt_text = f"""
                    Based on the candlestick chart, considering potential trends, support/resistance levels, and common fractal patterns provide a trading signal.
                    Only list the position type (Long, Short, None), stoploss, takeprofit as below:
                    Position Side:
                    Current Price:
                    StopLoss:
                    StopLoss (Percentage):
                    TakeProfit:
                    TakeProfit (Percentage):
                    Do not add anything more than this structure; only add up to 100 words description about why the signal was generated (After 2 empty lines)!
                    Use accurate values not rounded
                    If trading hint is None, dont print stoploss and take profit, but showing the reason!
                    Also, firstly consider {user_prompt} with higher priority (if is not meaningless).
                    
                    """
        response = client.chat.completions.create(
            model="gpt-4o",  # Or another vision-capable model
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text",
                         "text": prompt_text},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
                    ],
                }
            ],
        )

        # 5. Display the trading hint
        hint = response.choices[0].message.content
        return hint,image_path
    else:
        pass
