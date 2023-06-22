# -*- coding: utf8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2021-07-04 09:22:26
# 提供简单方法生成随机假名记忆练习
import random

import fire

hirakana = ['あ', 'い', 'う', 'え', 'お',
            'か', 'き', 'く', 'け', 'こ',
            'さ', 'し', 'す', 'せ', 'そ',
            'た', 'ち', 'つ', 'て', 'と',
            'な', 'に', 'ぬ', 'ね', 'の',
            'は', 'ひ', 'ふ', 'へ', 'ほ',
            'ま', 'み', 'む', 'め', 'も',
            'や', '○', 'ゆ', '○', 'よ',
            'ら', 'り', 'る', 'れ', 'ろ',
            'わ', '○', 'を', '○', 'ん',
            ]

katakana = ['ア', 'イ', 'ウ', 'エ', 'オ',
            'カ', 'キ', 'ク', 'ケ', 'コ',
            'サ', 'シ', 'ス', 'セ', 'ソ',
            'タ', 'チ', 'ツ', 'テ', 'ト',
            'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
            'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
            'マ', 'ミ', 'ム', 'メ', 'モ',
            'ヤ', '○', 'ユ', '○', 'ヨ',
            'ラ', 'リ', 'ル', 'レ', 'ロ',
            'ワ', '○', 'ヲ', '○', 'ン',
            ]

roomaji = ['a', 'i', 'u', 'e', 'o',
           'ka', 'ki', 'ku', 'ke', 'ko',
           'sa', 'shi', 'su', 'se', 'so',
           'ta', 'chi', 'tsu', 'te', 'to',
           'na', 'ni', 'nu', 'ne', 'no',
           'ha', 'hi', 'fu', 'he', 'ho',
           'ma', 'mi', 'mu', 'me', 'mo',
           'ya', '○', 'yu', '○', 'yo',
           'ra', 'ri', 'ru', 're', 'ro',
           'wa', '○', 'wo', '○', 'nn',
           ]

testList = []


def hira(genNum, remenberNum):
    testList = []
    for i in range(genNum):
        i = i + 1
        testList.append(hirakana[random.randrange(0, remenberNum-1)])
    return testList


def kata(genNum, remenberNum):
    testList = []
    for i in range(genNum):
        i = i + 1
        testList.append(katakana[random.randrange(0, remenberNum-1)])
    return testList


def rooma(genNum, remenberNum):
    testList = []
    for i in range(genNum):
        i = i + 1
        testList.append(roomaji[random.randrange(0, remenberNum-1)])
    return testList


def mix(genNum, remenberNum):
    testList = []
    testPool = hirakana[0:remenberNum-1]+katakana[0:remenberNum-1]
    for i in range(genNum):
        i = i+1
        testList.append(testPool[random.randrange(0, len(testPool)-1)])
    return testList


if __name__ == '__main__':
    fire.Fire()