#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import re
import os
import platform
import sys
import time


def main():
    global weather
    global add_items
    # sunny:0; rainy:1;notChange:2;thunderstorm:3
    weather = 2
    add_items = False
    save = "Sk_161885676"

    '''log file'''
    # make a copy of original stdout route
    stdout_backup = sys.stdout
    # define the log file that receives your log info
    log_file = open("message.log", "w")
    # redirect print output to log file
    sys.stdout = log_file

    '''get file path'''
    # python version
    print("Python", sys.version)
    if sys.version_info[0] == 2:
        cur_path = unicode(os.path.abspath('..'), 'utf8').encode('gbk')
    else:
        cur_path = os.path.abspath('..')
    save = os.path.join(cur_path, save, save)
    if sys.version_info[0] == 2:
        save = unicode(save, "utf8")
    print("save:", save)
    print(os.path.exists(save))
    '''read'''
    try:
        f = open(save, 'r')
        all_lines = f.readlines()
        print(len(all_lines[-1]))
        f.close()
    except:
        print("Error: cannot open save file")
        os.system("pause")
        exit(0)

    '''backup file'''
    f = open(save + "_backup", 'w+')
    f.writelines(all_lines)
    f.close()

    '''modification'''

    new = NewSave(all_lines[-1])

    '''write'''
    all_lines[-1] = new.get_data()
    f = open(save + '_1', 'w+')
    f.writelines(all_lines)
    f.close()


    print(time.strftime("%b-%d-%Y %a %H:%M:%S", time.localtime()))
    log_file.close()
    # restore the output to initial pattern
    sys.stdout = stdout_backup

    print("Finished")


def uni(str):
    if sys.version_info[0] == 1:
        return unicode(str, 'utf8')
    else:
        return str


class NewSave(object):
    def __init__(self, line):
        self.__line = line
        self.__sep = '<Item xsi:nil="true" />'
        self.__item_end = '</Item>'
        self.__Stack = re.compile("<Stack>(?:(?!([01]|897|999)<))\d+</Stack>")
        self.__stack = re.compile("<stack>(?:(?!([01]|897|999)<))\d+</stack>")
        self.__quality = re.compile("<quality>[123]")
        self.exp_points()
        self.weather_luck()
        self.friendship()
        self.chest()
        self.backpack()
        self.money()
        self.stamina_health()
        self.upgrade()

    @staticmethod
    def __get_strawberry():
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-79</category><specialItem>false' \
            '</specialItem><hasBeenInInventory>true</hasBeenInInventory><DisplayName>草莓</DisplayName>' \
            '<Stack>798</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation><parentSheetIndex>400</parentSheetIndex>' \
            '<owner>0</owner><name>Strawberry</name><type>Basic</type><canBeSetDown>true</canBeSetDown>' \
            '<canBeGrabbed>true</canBeGrabbed><isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject>' \
            '<questItem>false</questItem><isOn>true</isOn><fragility>0</fragility><price>120</price><edibility>20</edibility>' \
            '<stack>798</stack><quality>4</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest><showNextIndex>false</showNextIndex>' \
            '<flipped>true</flipped><hasBeenPickedUpByFarmer>true</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe>' \
            '<isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width>' \
            '<Height>64</Height><Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale>' \
            '<preserve xsi:nil="true" /><preservedParentSheetIndex>0</preservedParentSheetIndex><honeyType xsi:nil="true" /></Item>'
        return s

    @staticmethod
    def __get_catfish():
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-4</category><specialItem>false' \
            '</specialItem><hasBeenInInventory>true</hasBeenInInventory><DisplayName>鲶鱼</DisplayName>' \
            '<Stack>897</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation><parentSheetIndex>143</parentSheetIndex>' \
            '<owner>0</owner><name>Catfish</name><type>Fish</type><canBeSetDown>true</canBeSetDown><canBeGrabbed>true' \
            '</canBeGrabbed><isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject><questItem>false' \
            '</questItem><isOn>true</isOn><fragility>0</fragility><price>200</price><edibility>20</edibility>' \
            '<stack>897</stack><quality>4</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest><showNextIndex>false</showNextIndex>' \
            '<flipped>true</flipped><hasBeenPickedUpByFarmer>true</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe>' \
            '<isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width>' \
            '<Height>64</Height><Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale>' \
            '<preserve xsi:nil="true" /><preservedParentSheetIndex>0</preservedParentSheetIndex><honeyType xsi:nil="true" /></Item>'
        return s

    @staticmethod
    def __get_fishing_rod():
        s = '<Item xsi:type="FishingRod"><specialVariable>0</specialVariable><category>-99</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱金鱼竿</DisplayName><Stack>1</Stack><name>Fishing Rod</name>' \
            '<initialParentTileIndex>189</initialParentTileIndex><currentParentTileIndex>189</currentParentTileIndex>' \
            '<indexOfMenuItemView>11</indexOfMenuItemView><stackable>false</stackable><instantUse>false</instantUse>' \
            '<upgradeLevel>3</upgradeLevel><numAttachmentSlots>2</numAttachmentSlots><attachments><Object>' \
            '<specialVariable>0</specialVariable><category>-21</category><specialItem>false</specialItem>' \
            '<hasBeenInInventory>false</hasBeenInInventory><DisplayName>鱼饵</DisplayName><Stack>212</Stack>' \
            '<tileLocation><X>0</X><Y>0</Y></tileLocation><parentSheetIndex>685</parentSheetIndex><owner>0</owner>' \
            '<name>Bait</name><type>Basic</type><canBeSetDown>true</canBeSetDown><canBeGrabbed>true</canBeGrabbed>' \
            '<isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject><questItem>false</questItem>' \
            '<isOn>true</isOn><fragility>0</fragility><price>1</price><edibility>-300</edibility><stack>212</stack>' \
            '<quality>0</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest><showNextIndex>false</showNextIndex>' \
            '<flipped>false</flipped><hasBeenPickedUpByFarmer>false</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe>' \
            '<isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width>' \
            '<Height>64</Height><Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale>' \
            '<preserve xsi:nil="true" /><preservedParentSheetIndex>0</preservedParentSheetIndex>' \
            '<honeyType xsi:nil="true" /></Object><Object><specialVariable>0</specialVariable><category>-22</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>精装旋式鱼饵</DisplayName><Stack>1</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation>' \
            '<parentSheetIndex>687</parentSheetIndex><owner>0</owner><name>Dressed Spinner</name><type>Basic</type>' \
            '<canBeSetDown>true</canBeSetDown><canBeGrabbed>true</canBeGrabbed><isHoedirt>false</isHoedirt>' \
            '<isSpawnedObject>false</isSpawnedObject><questItem>false</questItem><isOn>true</isOn>' \
            '<fragility>0</fragility><price>500</price><edibility>-300</edibility><stack>1</stack>' \
            '<quality>0</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest>' \
            '<showNextIndex>false</showNextIndex><flipped>true</flipped><hasBeenPickedUpByFarmer>true' \
            '</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe><isLamp>false</isLamp>' \
            '<minutesUntilReady>0</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width>' \
            '<Height>64</Height><Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X>' \
            '<Y>0.249999836</Y></scale><preserve xsi:nil="true" /><preservedParentSheetIndex>0' \
            '</preservedParentSheetIndex><honeyType xsi:nil="true" /></Object></attachments></Item>'
        return s

    @staticmethod
    def __get_pink_cake():
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-7</category><specialItem>false' \
            '</specialItem><hasBeenInInventory>true</hasBeenInInventory><DisplayName>粉红蛋糕</DisplayName>' \
            '<Stack>100</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation><parentSheetIndex>221</parentSheetIndex>' \
            '<owner>0</owner><name>Pink Cake</name><type>Cooking</type><canBeSetDown>true</canBeSetDown>' \
            '<canBeGrabbed>true</canBeGrabbed><isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject>' \
            '<questItem>false</questItem><isOn>true</isOn><fragility>0</fragility><price>480</price><edibility>100' \
            '</edibility><stack>100</stack><quality>4</quality><bigCraftable>false</bigCraftable>' \
            '<setOutdoors>false</setOutdoors><setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest>' \
            '<showNextIndex>false</showNextIndex><flipped>true</flipped><hasBeenPickedUpByFarmer>true' \
            '</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe><isLamp>false</isLamp><minutesUntilReady>0' \
            '</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width><Height>64</Height><Location><X>0</X>' \
            '<Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale><preserve xsi:nil="true" />' \
            '<preservedParentSheetIndex>0</preservedParentSheetIndex><honeyType xsi:nil="true" /></Item>'
        return s

    @staticmethod
    def __get_iridium_bar():
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-15</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱锭</DisplayName><Stack>862</Stack><tileLocation><X>0</X><Y>0</Y>' \
            '</tileLocation><parentSheetIndex>337</parentSheetIndex><owner>0</owner>' \
            '<name>Iridium Bar</name><type>Basic</type><canBeSetDown>true</canBeSetDown>' \
            '<canBeGrabbed>true</canBeGrabbed><isHoedirt>false</isHoedirt>' \
            '<isSpawnedObject>false</isSpawnedObject><questItem>false</questItem><isOn>true</isOn>' \
            '<fragility>0</fragility><price>1000</price><edibility>-300</edibility><stack>862</stack>' \
            '<quality>0</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest>' \
            '<showNextIndex>false</showNextIndex><flipped>true</flipped>' \
            '<hasBeenPickedUpByFarmer>true</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe>' \
            '<isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady>' \
            '<boundingBox><X>0</X><Y>0</Y><Width>64</Width><Height>64</Height>' \
            '<Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale>' \
            '<preserve xsi:nil="true" /><preservedParentSheetIndex>0</preservedParentSheetIndex>' \
            '<honeyType xsi:nil="true" /></Item>'
        return s

    @staticmethod
    def __get_amethyst():
        # 紫水晶
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-2</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>紫水晶</DisplayName><Stack>295</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation>' \
            '<parentSheetIndex>66</parentSheetIndex><owner>0</owner><name>Amethyst</name>' \
            '<type>Minerals</type><canBeSetDown>true</canBeSetDown><canBeGrabbed>true</canBeGrabbed>' \
            '<isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject><questItem>false</questItem>' \
            '<isOn>true</isOn><fragility>0</fragility><price>100</price><edibility>-300</edibility><stack>295</stack>' \
            '<quality>4</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest><showNextIndex>false' \
            '</showNextIndex><flipped>false</flipped><hasBeenPickedUpByFarmer>true</hasBeenPickedUpByFarmer>' \
            '<isRecipe>false</isRecipe><isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady>' \
            '<boundingBox><X>0</X><Y>0</Y><Width>64</Width><Height>64</Height><Location><X>0</X><Y>0</Y>' \
            '</Location></boundingBox><scale><X>0</X><Y>0</Y></scale><preserve xsi:nil="true" />' \
            '<preservedParentSheetIndex>0</preservedParentSheetIndex><honeyType xsi:nil="true" /></Item>'
        return s

    @staticmethod
    def __get_hoe():
        s = '<Item xsi:type="Hoe"><specialVariable>0</specialVariable><category>-99</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱 锄头</DisplayName><Stack>1</Stack><name>Hoe</name>' \
            '<initialParentTileIndex>70</initialParentTileIndex><currentParentTileIndex>70</currentParentTileIndex>' \
            '<indexOfMenuItemView>96</indexOfMenuItemView><stackable>false</stackable><instantUse>false</instantUse>' \
            '<upgradeLevel>4</upgradeLevel><numAttachmentSlots>0</numAttachmentSlots></Item>'
        return s

    @staticmethod
    def __get_pickaxe():
        s = '<Item xsi:type="Pickaxe"><specialVariable>0</specialVariable><category>-99</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱 十字镐</DisplayName><Stack>1</Stack><name>Pickaxe</name>' \
            '<initialParentTileIndex>154</initialParentTileIndex><currentParentTileIndex>154</currentParentTileIndex>' \
            '<indexOfMenuItemView>180</indexOfMenuItemView><stackable>false</stackable><instantUse>false</instantUse>' \
            '<upgradeLevel>4</upgradeLevel><numAttachmentSlots>0</numAttachmentSlots></Item>'
        return s

    @staticmethod
    def __get_axe():
        s = '<Item xsi:type="Axe"><specialVariable>0</specialVariable><category>-99</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱 斧头</DisplayName><Stack>1</Stack><name>Axe</name>' \
            '<initialParentTileIndex>238</initialParentTileIndex><currentParentTileIndex>238</currentParentTileIndex>' \
            '<indexOfMenuItemView>264</indexOfMenuItemView><stackable>false</stackable><instantUse>false</instantUse>' \
            '<upgradeLevel>4</upgradeLevel><numAttachmentSlots>0</numAttachmentSlots></Item>'
        return s

    @staticmethod
    def __get_water_can():
        s = '<Item xsi:type="WateringCan"><specialVariable>0</specialVariable><category>-99</category>' \
            '<specialItem>false</specialItem><hasBeenInInventory>true</hasBeenInInventory>' \
            '<DisplayName>铱 喷壶</DisplayName><Stack>1</Stack><name>Watering Can</name>' \
            '<initialParentTileIndex>322</initialParentTileIndex><currentParentTileIndex>327</currentParentTileIndex>' \
            '<indexOfMenuItemView>345</indexOfMenuItemView><stackable>false</stackable><instantUse>false</instantUse>' \
            '<upgradeLevel>4</upgradeLevel><numAttachmentSlots>0</numAttachmentSlots><waterCanMax>300</waterCanMax>' \
            '<WaterLeft>300</WaterLeft><UpgradeLevel>4</UpgradeLevel></Item>'
        return s

    @staticmethod
    def __num_process(n):
        x = int(n)
        if x < 100:
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

    @staticmethod
    def __get_omni_geode():
        s = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>0</category><specialItem>false' \
            '</specialItem><hasBeenInInventory>true</hasBeenInInventory><DisplayName>万象晶石</DisplayName>' \
            '<Stack>798</Stack><tileLocation><X>0</X><Y>0</Y></tileLocation><parentSheetIndex>749</parentSheetIndex>' \
            '<owner>0</owner><name>Omni Geode</name><type>Basic</type><canBeSetDown>true</canBeSetDown><canBeGrabbed>' \
            'true</canBeGrabbed><isHoedirt>false</isHoedirt><isSpawnedObject>false</isSpawnedObject><questItem>false' \
            '</questItem><isOn>true</isOn><fragility>0</fragility><price>0</price><edibility>-300</edibility>' \
            '<stack>798</stack><quality>4</quality><bigCraftable>false</bigCraftable><setOutdoors>false</setOutdoors>' \
            '<setIndoors>false</setIndoors><readyForHarvest>false</readyForHarvest><showNextIndex>false</showNextIndex>' \
            '<flipped>false</flipped><hasBeenPickedUpByFarmer>true</hasBeenPickedUpByFarmer><isRecipe>false</isRecipe>' \
            '<isLamp>false</isLamp><minutesUntilReady>0</minutesUntilReady><boundingBox><X>0</X><Y>0</Y><Width>64</Width>' \
            '<Height>64</Height><Location><X>0</X><Y>0</Y></Location></boundingBox><scale><X>0</X><Y>0</Y></scale>' \
            '<preserve xsi:nil="true" /><preservedParentSheetIndex>0</preservedParentSheetIndex><honeyType xsi:nil="true" /></Item>'
        return s

    def __change_exp(self, str):
        s = re.sub("<int>\d+</int></e", "<int>15000</int></e", str)
        m = re.search(r"s><int>(\d+)</int><int>(\d+)</int><int>(\d+)</int><int>(\d+)"
                      "</int><int>(\d+)</int><int>\d+</int></e", s)
        t = ["农业", "钓鱼", "觅食", "采矿", "战斗"]

        if m is not None:
            for i in range(1, 6):
                x = m.group(i)
                y = self.__num_process(x)
                print(uni("{}:{}->{}".format(t[i - 1], x, y)))
                s = re.sub("<int>{}</int>".format(x), "<int>{}</int>".format(y), s)
            return s
        else:
            return None

    def __replace_tools(self, str):
        s = str
        # hoe
        start = str.find('<Item xsi:type="Hoe">')
        if start != -1:
            end = str[start:].find(self.__item_end) + 7 + start
            if '<upgradeLevel>4</upgradeLevel>' not in str[start:end]:
                s = s.replace(str[start:end], self.__get_hoe(), 1)
                print("Hoe replaced")
        # axe
        start = str.find('<Item xsi:type="Axe">')
        if start != -1:
            end = str[start:].find(self.__item_end) + 7 + start
            if '<upgradeLevel>4</upgradeLevel>' not in str[start:end]:
                s = s.replace(str[start:end], self.__get_axe(), 1)
                print("Axe replaced")
        # pickaxe
        start = str.find('<Item xsi:type="Pickaxe">')
        if start != -1:
            end = str[start:].find(self.__item_end) + 7 + start
            if '<upgradeLevel>4</upgradeLevel>' not in str[start:end]:
                s = s.replace(str[start:end], self.__get_pickaxe(), 1)
                print("Pickaxe replaced")
        # water can
        start = str.find('<Item xsi:type="WateringCan">')
        if start != -1:
            end = str[start:].find(self.__item_end) + 7 + start
            if '<upgradeLevel>4</upgradeLevel>' not in str[start:end]:
                s = s.replace(str[start:end], self.__get_water_can(), 1)
                print("Watering can replaced")
        # fishing rod
        start = str.find('<Item xsi:type="FishingRod">')
        if start != -1:
            end = str[start:].find(self.__item_end) + 7 + start
            if '<upgradeLevel>3</upgradeLevel>' not in str[start:end]:
                s = s.replace(str[start:end], self.__get_fishing_rod(), 1)
                print("Fishing rod replaced")

        self.__line = self.__line.replace(str, s, 1)

    def __add_amethyst(self, str):
        if '<name>Amethyst</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_amethyst(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Amethyst added")

    def __add_omni_geode(self, str):
        if '<name>Omni Geode</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_omni_geode(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Omni Geode added")

    def __add_iridium_bar(self, str):
        if '<name>Iridium Bar</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_iridium_bar(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Iridium bar added")

    def __add_strawberry(self, str):
        if '<name>Strawberry</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_strawberry(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Strawberry added")

    def __add_pink_cake(self, str):
        if '<name>Pink Cake</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_pink_cake(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Pink cake added")

    def __add_catfish(self, str):
        if '<name>Catfish</name>' not in str and self.__sep in str:
            s = str.replace(self.__sep, self.__get_catfish(), 1)
            self.__line = self.__line.replace(str, s, 1)
            print("Catfish added")

    def __get_backpack(self):
        start = self.__line.find("</experiencePoints>") + 19
        end = self.__line.find("<dialogueQuestionsAnswered>")
        end = self.__line[start:end].rfind(self.__item_end + self.__sep) + start + 7
        return self.__line[start:end]

    def backpack(self):
        print("********** Backpack Modify **********")
        '''replace tools'''
        self.__replace_tools(self.__get_backpack())

        '''add items'''
        if add_items:
            self.__add_pink_cake(self.__get_backpack())
            self.__add_catfish(self.__get_backpack())
            self.__add_omni_geode(self.__get_backpack())
            self.__add_strawberry(self.__get_backpack())
            self.__add_amethyst(self.__get_backpack())
            self.__add_iridium_bar(self.__get_backpack())

        '''stacks'''
        str = self.__get_backpack()
        [s, n] = self.__Stack.subn("<Stack>897</Stack>", str)
        [s, t] = self.__stack.subn("<stack>897</stack>", s)
        if t == n:
            [s, t] = self.__quality.subn("<quality>4", s)
            print(uni("背包: 完成{}次替换,品质替换:{}次".format(n, t)))
        else:
            print("Backpack error")
        self.__line = self.__line.replace(str, s, 1)

    def get_data(self):
        return self.__line

    def chest(self):
        print("********** Chests Modify **********")
        end = 0
        i = 1
        start = self.__line[end:].find("宝箱")
        Stack = re.compile("<Stack>(?:(?!([01]|999|798)<))\d+</Stack>")
        stack = re.compile("<stack>(?:(?!([01]|999|798)<))\d+</stack>")
        while start != -1:
            start += end
            end = self.__line[start:].find("chestType") + start
            str = self.__line[start - 5:end + 12]
            [s, n] = Stack.subn("<Stack>798</Stack>", str)
            [s, t] = stack.subn("<stack>798</stack>", s)
            if n == t:
                [s, t] = self.__quality.subn("<quality>4", s)
                self.__line = re.sub(str, s, self.__line)
                print(uni("宝箱{}: 完成{}次替换,品质替换:{}次".format(i, n, t)))
            else:
                print("Error")
            start = self.__line[end:].find("宝箱")
            i += 1

    def exp_points(self):
        print("********** Exp Modify **********")
        start = self.__line.find("<experiencePoints>")
        end = start + 132
        str = self.__line[start:end]
        s = self.__change_exp(str)
        if s is None:
            print("Error: exp modify fail!")
        else:
            self.__line = re.sub(str, s, self.__line)

    def weather_luck(self):
        print("********** Weather and Luck Modify **********")
        start = self.__line.find("<weatherForTomorrow>")
        str = self.__line[start:start + 30]
        m = re.search(">(\d)<", str)  # 记录原始天气
        if weather not in range(0, 4):
            print("Wrong input")
        else:
            if weather != 2:
                s = re.sub("Tomorrow>\d</w", "Tomorrow>{}</w".format(weather), str)
                self.__line = re.sub(str, s, self.__line)
            t = ["晴", "雨", "Not change", "雷雨"]
            print(uni("明日天气: {}->{}".format(t[int(m.group(1))], t[weather])))

        start = self.__line.find("<dailyLuck>")
        str = self.__line[start:start + 27]
        m = re.search("<dailyLuck>(.*?)</", str)
        s = re.sub("<dailyLuck>(.*?)</", "<dailyLuck>1.18</", str)
        print(uni("运势: {}->1.18".format(m.group(1))))
        self.__line = re.sub(str, s, self.__line)

    def friendship(self):
        print("********** Friendships modify **********")
        start = self.__line.find("<friendships>")
        end = self.__line[start:].rfind('</string></key><value><ArrayOfInt><int>') + start + 60
        str = self.__line[start:end]
        friend = re.compile('<ArrayOfInt><int>(\d+)</int><int>')
        # print((friend.findall(str)))
        t = 0
        s = str
        for n in friend.findall(str):
            n = int(n)
            x = 250 - (n % 250)
            x += (n - 1)
            if x != n and n < 2500 and n != 0:
                s = re.sub('<ArrayOfInt><int>{}</int><int>'.format(n),
                           '<ArrayOfInt><int>{}</int><int>'.format(x), s)
                t += 1
        self.__line = self.__line.replace(str, s, 1)
        print(uni("完成{}次替换".format(t)))
        # print((friend.findall(s)))

    def money(self):
        start = self.__line.find("<money>")
        str = self.__line[start:start + 25]
        m = re.search('<money>(\d+)</money>', str)
        if int(m.group(1)) < 1000000:
            s = re.sub('<money>(\d+)</money>', '<money>{}</money>'.format(int(m.group(1)) + 300000), str)
            self.__line = self.__line.replace(str, s, 1)
            print("Money: 300,000 added")

    def stamina_health(self):
        start = self.__line.find('<maxStamina>')
        str = self.__line[start:start + 25]
        m = re.search("<maxStamina>(\d+)<", str)
        if int(m.group(1)) < 300:
            s = re.sub("<maxStamina>\d+<", "<maxStamina>400<", str)
            self.__line = self.__line.replace(str, s, 1)
            print("Max stamina changed")

        start = self.__line.find('<maxHealth>')
        str = self.__line[start:start + 25]
        m = re.search("<maxHealth>(\d+)<", str)
        if int(m.group(1)) < 150:
            s = re.sub("<maxHealth>\d+<", "<maxHealth>250<", str)
            self.__line = self.__line.replace(str, s, 1)
            print("Max health changed")

    def upgrade(self):
        start = self.__line.find('<daysUntilHouseUpgrade>')
        str = self.__line[start:start + 50]
        if re.search('<daysUntilHouseUpgrade>(?!0<)\d+', str) is not None:
            s = re.sub("<daysUntilHouseUpgrade>\d+", "<daysUntilHouseUpgrade>1", str)
            self.__line = self.__line.replace(str, s, 1)
            print("House upgrade days changed")


if __name__ == '__main__':
    main()
    if platform.system() == "Windows":
        os.system("pause")
