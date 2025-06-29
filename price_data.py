import ccxt
import pandas as pd
import plotly.graph_objects as go
def price_dataframe(symbol='BTC/USDT',timeframe='1h',exchange='kucoin',limit=100):
    if(exchange=='kucoin'):
        exchange = ccxt.kucoin() # You can choose other exchanges like ccxt.kraken(), ccxt.kucoin(), etc.

    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

        if not ohlcv:
            print(f"No OHLCV data fetched for {symbol} on {exchange.id} for timeframe {timeframe}.")
        else:
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            print("Fetched OHLCV data head:")
            #print(df)
            return df



    except ccxt.NetworkError as e:
        print(f"Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Exchange error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def create_and_save_candlestick_chart(symbol='BTC/USDT',timeframe='1h',exchange='kucoin',limit=100):
    df=price_dataframe(symbol=symbol,timeframe=timeframe,exchange=exchange,limit=limit)
    if df is None or df.empty:
        print("Cannot create chart: DataFrame is empty or None.")
        return
    df_string = df.to_csv(index=False)
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    print(df['datetime'][0])
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    fig.update_layout(
        title=f'{symbol} Candlestick Chart',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False, # Hide the range slider for a cleaner look
        height=600, # Set a fixed height for the chart
        template='plotly_dark' # Use a dark theme for better aesthetics
    )


    try:
        filename = 'test.png'  # Changed filename to PNG
        fig.write_image(filename)  # Save as PNG image
        print(f"Candlestick chart saved successfully as '{filename}'")
        return filename
    except ImportError:
        print("Error: 'kaleido' package not found. Please install it to save charts as images: pip install kaleido")
    except Exception as e:
        print(f"An unexpected error occurred while saving chart: {e}")
