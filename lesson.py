# class Button:
#  count = 0

#  def click(self):
#   Button.count += 1

#  def click_count(self):
#   return Button.count

#  def reset(self):
#   Button.count = 0

# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.reset()
# print(button.click_count())

# class Big_bell:
#  def __init__(self):
#   self.count = 1

#  def sound(self):
#   self.count += 1
#   if not self.count % 2:
#    print('ding')
#   else:
#    print('dong')

# bell = Big_bell()
# bell.sound()
# bell.sound()
# bell.sound()

# bell_2 = Big_bell()
# bell_2.sound()

# class Balance:

#  def __init__(self):
#   self.left = 0
#   self.right = 0

#  def add_left(self, weight):
#   self.left += weight

#  def add_right(self, weight):
#   self.right += weight

#  def result(self):
#   if self.left < self.right:
#    return 'R'
#   elif self.left > self.right:
#    return 'L'
#   else:
#    return '='

# ballance = Balance()
# ballance.add_right(10)
# ballance.add_left(9)
# ballance.add_left(2)
# print(ballance.result())

# class OddEvenSeparator:
#     def __init__(self):
#         self.lst = []

#     def add_number(self,number):
#         self.lst.append(number)

#     def even(self):
#         return list(filter(lambda x : x%2 == 0, self.lst))

#     def odd(self):
#         return list(filter(lambda x : x%2 != 0, self.lst))

# separator = OddEvenSeparator()
# separator.add_number(1)
# separator.add_number(5)
# separator.add_number(6)
# separator.add_number(8)
# separator.add_number(3)

# print(' '.join(map(str, separator.even())))
# print(' '.join(map(str, separator.odd())))

class MinMaxWordFinder:
    def __init__(self):
        self.some_list = []

    def add_sentence(self, sentence):
        self.some_list.extend(sentence.split())

    def shortest_words(self):
        self.short_list = []
        short_word = self.some_list[0]
        for word in self.some_list:
            if len(word) < len(short_word):
                short_word = word
        for word in self.some_list:
            if len(word) == len(short_word):
                self.short_list.append(word)
        return sorted(self.short_list)

    def longest_words(self):
        self.long_list = []
        long_word = self.some_list[0]
        for word in self.some_list:
            if len(word) > len(long_word):
                long_word = word
        for word in self.some_list:
            if len(word) == len(long_word) and word not in self.long_list:
                self.long_list.append(word)
        return sorted(self.long_list)

finder = MinMaxWordFinder()
finder.add_sentence('hellow abc words')
finder.add_sentence('def acdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

    

    