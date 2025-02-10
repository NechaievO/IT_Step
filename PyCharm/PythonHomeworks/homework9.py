import json


target_items = ['Laptop', 'Mouse', 'Keyboard']
increase_value = 10


try:

    with open('goods.json', 'r') as json_file:
        data = json.load(json_file)
        print(f"Current inventory data: {data}")



    if 'inventory' in data:
        for item_dict in data['inventory']:
            if 'item' in item_dict and item_dict['item'] in target_items:
                if 'quantity' in item_dict:
                    item_dict['quantity'] += increase_value
                    print(f"Updated '{item_dict['item']}' quantity to {item_dict['quantity']}.")

                else:
                    print(f"'quantity' for '{item_dict['item']}' is missing or not an integer.")
            else:
                print(f"Item '{item_dict.get('item', 'Unknown')}' not in target items.")

        if inventory_updated:
            with open('goods.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print("Inventory data has been updated.")
        else:
            print("No inventory items were updated.")
    else:
        print("'inventory' key is missing or not a list in the JSON data.")

except FileNotFoundError:
    print("The file 'goods.json' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

