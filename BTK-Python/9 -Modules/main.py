import mod #mod.py dokümanı içerisinde çalıştırılabilir olan kod varsa direkt çalıştırılır.

# result = help(mod)
# result = help(mod.func)

result = mod.number         # Çıktı = 10
result = mod.numbers        # Çıktı = [1, 2, 3]
result = mod.person['name'] # Çıktı = Ali
result = mod.func(10)       # Çıktı = x: 10

p = mod.Person()
p.speak()

print(result)

