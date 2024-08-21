import MetaTrader5 as mt5
from datetime import datetime, timedelta

## Tested and working
#from openMt5 import openMt5

def getTradeTimes(magic):
    deals = mt5.history_deals_get(0, datetime.now())

    deals = [deal for deal in deals if deal.magic == magic]
    # Dictionary to track open times
    open_trades = {}
    trade_durations = []

    # Process each deal
    for deal in deals:
        ticket = deal.position_id
        if deal.reason == 3:
            # Trade opening
            open_trades[ticket] = deal.time
        else:
            # Trade closing
            if ticket in open_trades:
                open_time = open_trades.pop(ticket)
                close_time = deal.time
                trade_duration = close_time - open_time
                trade_durations.append(trade_duration)

    if len(trade_durations) == 0:
        return 0, 0, 0
    else:
        # Convert trade durations to timedeltas
        trade_durations = [timedelta(seconds=duration) for duration in trade_durations]

        # Calculate min, max, and average trade duration
        min_trade_duration = format_duration(min(trade_durations))
        max_trade_duration = format_duration(max(trade_durations))
        avg_trade_duration = format_duration(sum(trade_durations, timedelta()) / len(trade_durations))

        return min_trade_duration, max_trade_duration, avg_trade_duration

def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds_remainder = divmod(remainder, 60)
    if len(str(hours)) == 1:
        hours = f"0{hours}"
    if len(str(minutes)) == 1:
        minutes = f"0{minutes}"
    if len(str(seconds_remainder)) == 1:
        seconds_remainder = f"0{seconds_remainder}"
    return f"{hours}:{minutes}:{seconds_remainder}"

#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getTradeTimes(3342))