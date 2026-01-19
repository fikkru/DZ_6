def trim_and_repeat(text, offset=0, repetitions=1):
  
    trimmed_text = text[offset:]
    
    result = trimmed_text * repetitions
    
    return result

print("Тестирование функции trim_and_repeat:")
print("-" * 50)