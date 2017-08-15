#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  
# Project: untitled  
# File name: Modifier.py
# Author: Minchao Sun
# Created: 2017/8/14 15:49

from __future__ import print_function
import os
import platform
import shutil
import sys
import xml.etree.ElementTree as ET

# sunny:0; rainy:1; not change:2; thunderstorm:3
weather = 2


def main():
    print('Python', sys.version)
    cur_path = os.path.abspath('.')
    save_path = cur_path + os.path.sep + uni('Tony_162475701')
    print(save_path)
    backup = save_path + '_backup'
    shutil.copy(save_path, backup)
    if os.path.isfile(backup):
        print('Backup success')
    Save = SaveFile(save_path)
    Save.write_file()
    if platform.system() == 'Windows':
        os.system("pause")


def uni(str):
    if sys.version_info[0] == 3:
        return str
    else:
        return unicode(str, 'utf-8')


class SaveFile:
    def __init__(self, save_path):
        self.__save_path = save_path
        self.__tree = ET.parse(save_path)
        self.__root = self.__tree.getroot()
        self.__player = self.__root.find('player')
        self.__xsi = '{http://www.w3.org/2001/XMLSchema-instance}type'
        self.__xsd = 'http://www.w3.org/2001/XMLSchema'
        # self.player_modify()
        # self.luck_modify()
        # self.location_modify()
        # self.weather_modify()

    @staticmethod
    def __exp_process(n):
        x = int(n)
        if x in range(1, 100):
            x = 99
        elif x in range(100, 380):
            x = 379
        elif x in range(380, 770):
            x = 769
        elif x in range(770, 1300):
            x = 1299
        elif x in range(1300, 2150):
            x = 2149
        elif x in range(2150, 3300):
            x = 3299
        elif x in range(3300, 4800):
            x = 4799
        elif x in range(4800, 6900):
            x = 6899
        elif x in range(6900, 10000):
            x = 9999
        elif x in range(10000, 15000):
            x = 14999
        return x.__str__()

    def __exp_modify(self):
        i = 0
        for e in self.__player.find('experiencePoints').findall('int'):
            i += 1
            if i == 6:
                # abandon luck exp points
                break
            e.text = self.__exp_process(e.text)

    def __money(self):
        t = int(self.__player.find('money').text)
        if t < 500000:
            t += 300000
            self.__player.find('money').text = t.__str__()
            print('300,000 money added')

    @staticmethod
    def __friendship_process(n):
        if n == 0:
            return n
        x = 250 - (n % 250)
        x += (n - 1)
        return x

    def __friendship(self):
        for i in self.__player.find('friendships').findall('item'):
            t = i.find('value').find('ArrayOfInt').find('int')
            temp = int(t.text)
            t.text = self.__friendship_process(temp).__str__()

    @staticmethod
    def __stack_process(node):
        if int(node.text) > 1:
            node.text = '800'

    @staticmethod
    def __quality_process(node):
        if int(node.text) > 0:
            node.text = '4'

    def __backpack(self):
        items = self.__player.find('items')
        for i in items.iter('Stack'):
            self.__stack_process(i)
        for i in items.iter('stack'):
            self.__stack_process(i)
        for i in items.iter('quality'):
            self.__quality_process(i)
        print('Backpack items modified')

    def __quest(self):
        global delivery
        for q in self.__player.find('questLog').findall('Quest'):
            if q.get(self.__xsi) == 'ItemDeliveryQuest':
                delivery = q.find('deliveryItem')

    def player_modify(self):
        self.__exp_modify()
        self.__quest()
        self.__money()
        self.__friendship()
        self.__backpack()

    def luck_modify(self):
        self.__root.find('dailyLuck').text = '1.18'

    def location_modify(self):
        location = self.__root.find('locations')
        for house in location.findall('GameLocation'):
            if house.get(self.__xsi) == 'FarmHouse':
                # find farm house
                break

        for item in house.find('objects').findall('item'):
            chest = item.find('value').find('Object')
            if chest.get(self.__xsi) == 'Chest':
                # in each chest
                for i in chest.iter('Stack'):
                    self.__stack_process(i)
                for i in chest.iter('stack'):
                    self.__stack_process(i)
                for i in chest.iter('quality'):
                    self.__quality_process(i)
        print('Chest(in house) items modified')

    def weather_modify(self):
        global weather
        t = self.__root.find('weatherForTomorrow')
        s = ["Sunny", "Rainy", "Not change", "Thunderstorm"]
        if weather not in range(0, 4):
            print("Wrong input")
        else:
            print('Weather for tomorrow: {} => {}'.format(s[int(t.text)], s[weather]))
            if weather != 2:
                t.text = weather.__str__()

    def write_file(self):
        self.__tree.write(self.__save_path, 'utf-8', True)


if __name__ == '__main__':
    main()
