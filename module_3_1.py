calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(a='Str'):
    global calls
    count_calls()
    return ((len(a), a.upper(), a.lower()))

def is_contains(a='Str', b=['Str']):
    global calls
    count_calls()
    flag = 0
    for i in b:
        if a.lower() == str(i).lower():
            flag = 1
            break
    return True if flag == 1 else False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)