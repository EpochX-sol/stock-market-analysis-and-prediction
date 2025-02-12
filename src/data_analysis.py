from api_integration import fetch_data, get_symbols as fetch_symbols 

def process_data(symbol):
    data = fetch_data(symbol)
    if 'Error' in data:
        return f'Error fetching data for {symbol}: {data["Error Description"]}'
    print(data)

def get_all_symbols():
    container = [] 
    data = fetch_symbols().text.split('\n')
    print(data)
    for text in data:
        data_obj={}
        arr_data = text
        print(data)
        # print(len(arr_data))
        # for n in range(len(arr_data)):
        #     if arr_data[n]:
        #         data_obj[arr_data[n]] = arr_data[n]
        # container.append(data_obj)
    return container



data  = get_all_symbols() 
print(data)