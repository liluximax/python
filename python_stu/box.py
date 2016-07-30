#!/usr/bin/python3

sentence = raw_input("sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print
print ' ' * (left_margin-2) + '+' + '-' * box_width + '+'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '| ' + sentence + ' |'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * (left_margin-2) + '+' + '-' * box_width + '+'
