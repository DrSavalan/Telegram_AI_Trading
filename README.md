# Telegram AI Trading Bot
![image](https://github.com/user-attachments/assets/e0145e4c-5ccf-4032-9af9-61adca44ee98)
![image](https://github.com/user-attachments/assets/abdfbda3-0e8e-4b1a-8e7c-a94ec6253e92)
![image](https://github.com/user-attachments/assets/af5c2ce3-963a-442e-ae92-4c5c51674e2b)
![image](https://github.com/user-attachments/assets/cfeeea94-c305-4c5a-9f3a-300d4ea13efa)

**Empower your crypto trading with this Telegram bot that automates market analysis and provides actionable signals.**

This project features a Telegram bot that fetches live cryptocurrency data, generates dynamic candlestick charts, and leverages advanced AI vision analysis to offer trading hints with precise entry/exit points. It's built with security in mind, handling all API keys through environment variables for safe deployment and usage.

-----

## Features

  * **Real-time Data Fetching:** Integrates with cryptocurrency exchanges (via `ccxt`) to retrieve OHLCV (Open, High, Low, Close, Volume) data.
  * **Dynamic Chart Generation:** Creates insightful candlestick charts using Plotly to visualize market trends.
  * **AI-Powered Analysis:** Utilizes a vision-capable AI model to analyze charts and generate trading signals.
  * **Actionable Trading Hints:** Provides clear signals including position type (Long/Short/None), current price, stop-loss, and take-profit percentages, along with a brief explanation.
  * **Secure API Key Handling:** Employs `.env` files and environment variables for secure management of sensitive API keys.

-----

## Getting Started

Follow these steps to set up and run your Telegram AI Trading Bot.

### Prerequisites

Before you begin, ensure you have the following installed:

  * **Python 3.8+**
  * **pip** (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/DrSavalan/Telegram_AI_Trading.git
    cd Telegram_AI_Trading
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

      * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
      * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** This will install `pyTelegramBotAPI`, the library used to interact with the Telegram Bot API.

### Configuration

1.  **Create a `.env` file:** In the root directory of your project, create a file named `.env`.

2.  **Add your API keys to the `.env` file:**

    ```env
    bot_token="YOUR_TELEGRAM_BOT_TOKEN"
    API_KEY="YOUR_AI_SERVICE_API_KEY"
    ```

      * **`bot_token`**: Obtain this from [BotFather on Telegram](https://t.me/botfather).
      * **`API_KEY`**: This is your API key for the AI vision service.

    **Important Note on AI Service:**
    The current code is configured to use **AvalAI** (`base_url="https://api.avalai.ir/v1"`).
    **AvalAI is primarily intended for users in Iran due to regional limitations and easier access within the region.**

    **For users outside of Iran, it is recommended to switch the AI service to OpenAI's official API.** To do this, simply modify the `client` initialization in `AI_tools.py` to:

    ```python
    client = OpenAI(
        api_key=api_key,
        # base_url="https://api.openai.com/v1", # This is OpenAI's default base URL, usually not needed if using official API
    )
    ```

    and ensure your `API_KEY` in `.env` is an **OpenAI API key**.

    **Important:** Never commit your `.env` file to version control (e.g., Git). It's already included in `.gitignore` for your convenience.

### Running the Bot

Once configured, you can start your bot:

```bash
python bot.py
```

The bot will print "Bale bot starting..." and begin polling for messages.

-----

## Usage

Interact with the bot on Telegram.

### Commands

  * `/start` or `/help`: Displays a welcome message and usage instructions.

### Signal Requests

To request a trading signal, use the following format:

```
SIG [cryptocurrency_name] [timeframe] [limit] [your_custom_prompt]
```

**Example:**

```
SIG ETH 1h 250 use Al Brooks Method
```

  * `SIG`: The command to request a signal.
  * `ETH`: The cryptocurrency symbol (e.g., BTC, ETH, SOL).
  * `1h`: The timeframe (e.g., `15m`, `1h`, `4h`, `1d`).
  * `250`: The data limit (number of candles to fetch).
  * `use Al Brooks Method`: Your custom prompt to guide the AI's analysis.

The bot will then generate a candlestick chart, analyze it, and respond with a trading signal and an image of the chart.

-----

## Project Structure

  * `bot.py`: The main Telegram bot script, handling messages and integrating with AI tools.
  * `AI_tools.py`: Contains the core logic for AI analysis, image encoding, and calling the OpenAI (AvalAI) API.
  * `price_data.py`: Handles fetching cryptocurrency OHLCV data using `ccxt` and generating candlestick charts with Plotly.
  * `requirements.txt`: Lists all the necessary Python dependencies.
  * `.env`: (Not committed) Stores sensitive API keys.

-----

## `requirements.txt`

```text
pyTelegramBotAPI==4.27.0
python-dotenv==1.1.1
openai==1.93.0
Pillow==11.2.1
ccxt==4.4.91
pandas==2.3.0
plotly==6.2.0
kaleido==1.0.0
```

-----

## Contributing

Feel free to fork this repository, open issues, or submit pull requests. All contributions are welcome\!

-----

## Contact

For any questions or inquiries, feel free to reach out:

DrSavalan | mechsavalan@gmail.com

-----
