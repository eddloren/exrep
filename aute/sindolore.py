from datetime import datetime
current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")
print(f"Today's date is: {formatted_date}")
