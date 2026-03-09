def bitwise_display(text):
    print(f"\n{'Char':<5} | {'ASCII':<5} | {'&0':<4} | {'|0':<4} | {'^0':<4} | {'&127':<5} | {'|127':<5} | {'^127':<5}")
    print("-" * 65)
    
    for char in text:
        v = ord(char)
        print(f"{char:<5} | {v:<5} | {v&0:<4} | {v|0:<4} | {v^0:<4} | {v&127:<5} | {v|127:<5} | {v^127:<5}")
user_str = input("\nEnter a string for bitwise operations: ")
bitwise_display(user_str)
