#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Basic(object):
    def __init__(self):
        self.Strawberry = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-79</category><specialItem>false' \
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
        self.Catfish = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-4</category><specialItem>false' \
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
        self.PinkCake = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-7</category><specialItem>false' \
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
        self.IridiumBar = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-15</category>' \
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
        self.Amethyst = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>-2</category>' \
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
        self.OmniGeode = '<Item xsi:type="Object"><specialVariable>0</specialVariable><category>0</category><specialItem>false' \
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


Object = Basic()
