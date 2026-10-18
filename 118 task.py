url = input()
# ищем q= и берём до &
start = url.find('q=') + 2
end = url.find('&', start)
if end == -1:
    end = len(url)
print(url[start:end])