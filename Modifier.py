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
import lxml.etree as ET

# sunny:0; rainy:1; not change:2; thunderstorm:3
weather = 2
DEBUG = False


def main():
    print('Python', sys.version)
    cur_path = os.getcwd()
    filename = None
    for filename in os.listdir(cur_path):
        if '.' not in filename and '_' in filename \
                and 'old' not in filename and 'SaveGameInfo' not in filename:
            break

    save_path = cur_path + os.path.sep + uni(filename)
    if not os.path.isfile(save_path):
        print("save file does not exist")
        exit(0)
    print(save_path)
    print(filename == os.path.basename(save_path))
    if not DEBUG:
        if not os.path.exists("backup"):
            os.mkdir("backup")
        back_path = cur_path + os.path.sep + 'backup'
        n = 1
        backup = back_path + os.path.sep + 'backup' + str(n)
        while os.path.isfile(backup):
            n += 1
            backup = back_path + os.path.sep + 'backup' + str(n)
        shutil.copy(save_path, backup)
        if os.path.isfile(backup):
            print('Backup success')
    save = SaveFile(save_path)
    save.write_file()
    if platform.system() == 'Windows':
        os.system("pause")


def uni(string):
    if sys.version_info[0] == 3:
        return string
    else:
        return unicode(string, 'utf-8')


class SaveFile(object):
    def __init__(self, save_path):
        if DEBUG:
            self.__save_path = save_path + '_debug.xml'
        else:
            self.__save_path = save_path
        self.__tree = ET.parse(save_path)
        self.__root = self.__tree.getroot()
        self.__player = self.__root.find('player')
        self.__xsi = '{http://www.w3.org/2001/XMLSchema-instance}type'
        ET.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema")
        
        self.player_modify()
        self.luck_modify()
        self.location_modify()
        self.weather_modify()

    def __exp_modify(self):
        def exp_process(n):
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
            return str(x)

        for e in self.__player.find('experiencePoints').findall('int'):
            e.text = exp_process(e.text)

    def __money(self):
        t = int(self.__player.find('money').text)
        if t < 500000:
            t += 300000
            self.__player.find('money').text = str(t)
            print('300,000 money added')

    def __friendship(self):
        def friendship_process(n):
            if n == 0:
                return n
            x = 250 - (n % 250)
            x += (n - 1)
            return x

        for i in self.__player.find('friendships').findall('item'):
            t = i.find('value').find('ArrayOfInt').find('int')
            temp = int(t.text)
            t.text = str(friendship_process(temp))

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
        for q in self.__player.find('questLog').findall('Quest'):
            if q.get(self.__xsi) == 'ItemDeliveryQuest':
                delivery = ET.tostring(q.find('deliveryItem'))
                delivery = ET.fromstring(delivery)

                delivery.find('hasBeenPickedUpByFarmer').text = 'true'
                delivery.find('hasBeenInInventory').text = 'true'
                delivery.tag = 'Item'
                delivery.set(self.__xsi, "Object")

                for i in self.__player.find('items').findall('Item'):
                    if i.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                        i.addnext(delivery)
                        i.getparent().remove(i)
                        print("quest item added")
                        break
        if DEBUG:
            ET.ElementTree(self.__player.find('items')).write(
                file='items.xml',
                encoding='utf-8',
                pretty_print=True)

    def player_modify(self):
        self.__exp_modify()
        self.__quest()
        self.__money()
        self.__friendship()
        self.__backpack()

    def luck_modify(self):
        self.__root.find('dailyLuck').text = '0.12'

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
        elif int(t.text) in range(0,4):
            print('Weather for tomorrow: {} => {}'.format(s[int(t.text)], s[weather]))
            if weather != 2:
                t.text = str(weather)

    def write_file(self):
        self.__tree.write(
            file=self.__save_path,
            encoding='utf-8',
            xml_declaration=True,
            pretty_print=DEBUG,
            method='xml')


if __name__ == '__main__':
    main()
