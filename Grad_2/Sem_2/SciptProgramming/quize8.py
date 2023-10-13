# pip uninstall googletrans

import googletrans as gt

class MyTranslator(object):

  def __init__(self):
    self.name = "MyTranslator"
    self.this_is_translator = gt.Translator()

  def translate_decorator(original_func):
    def wapper_translate_func(self, *args, **kwargs):
      print("번역 결과입니다.")
      return original_func(self, args, kwargs)
    return wapper_translate_func

  @translate_decorator
  def Translate(self, *args, **kwargs):
    result_ = self.this_is_translator.translate(str(list(args)[0][0]), dest = list(args)[1]['출력언어'])
    print(result_.text)

translator = MyTranslator()

print("번역하고싶은 한글 문장을 입력하시오.")
my_str = str(input(">> "))

translator.Translate(my_str, 입력언어="ko", 출력언어="ko")
translator.Translate(my_str, 입력언어="ko", 출력언어="en")

