import requests
from bs4 import BeautifulSoup
import re

def get_data(map_name,diffcult_name):
    url = 'https://maelstroom.net/filtered.php'

    if diffcult_name == 'Sedition':
        content_length = '65'
    elif diffcult_name == 'Uprising':
        content_length = '65'
    elif diffcult_name == 'Malice':
        content_length = '63'
    elif diffcult_name == 'Heresy':
        content_length = '63'
    elif diffcult_name == 'Damnation':
        content_length = '66'
    else:
        content_length = '78'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Host': 'maelstroom.net',
        'Content-Length': content_length,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'bookCir'     : '0',
        'missionDif'  : diffcult_name,
        'missionCir'  : '',
        'button1'     : 'Filter Missions'
    }

    data_gold = {
        'bookCir'     : '0',
        'missionDif'  : 'Damnation',
        'missionCir'  : '',
        'flashOnly'   : '0',
        'button1'     : 'Filter Missions'
    }

    if diffcult_name == 'Gold_Damnation':
        r = requests.post(url=url, headers=headers, data=data_gold).text
    else:
        r = requests.post(url=url, headers=headers, data=data).text

    bs4 = BeautifulSoup(r, 'lxml')
    texts = bs4.find_all('body')
    texts = str(texts).replace('<br/>','\n')
    result = re.findall(map_name + r'.+\n/mmtimport \w{8}-\w{4}-\w{4}-\w{4}-\w{12}', texts)

    return result

def result_format(result):
    mmt_code = ''
    for item in result:
        item = item.replace('Mutants', '牛潮')
        item = item.replace('Poxbursters Gauntlet', '自爆怪')
        item = item.replace('Hunting Grounds', '狗潮')
        item = item.replace('Grenades', '强化闪击')
        item = item.replace('Barrels', '额外的炸药桶')
        item = item.replace('Nurgle-Blessed', '纳垢赐福')
        item = item.replace('Hi-Intensity', '高强度')
        item = item.replace('Low-Intensity', '低强度')
        item = item.replace('Monstrous', '假boss')
        item = item.replace('Gauntlet', '挑战')
        item = item.replace('Shock Troop', '突击部队')
        item = item.replace('Snipers', '狙击')
        item = item.replace('Sniper', '狙击')
        item = item.replace('Ventilation Purge', '雾天')
        item = item.replace('Engagement Zone', '交战区')
        item = item.replace('Scab Enemies Only', '只有血痂')
        item = item.replace('Cooldowns Reduced', '技能CD-20%')
        item = item.replace('Ranged Scab Enemies Only', '只有远程血痂')
        item = item.replace('Power Supply Interruption', '停电')
        item = item.replace('Raid', '突袭')
        item = item.replace('Strike', '打击')
        item = item.replace('Disruption', '破坏')
        item = item.replace('Espionage', '谍报')
        item = item.replace('Assassination', '暗杀')
        item = item.replace('Investigation', '调查')
        item = item.replace('Recover Scriptures', '圣经')
        item = item.replace('Seize Grimoires', '魔法书')
        item = item.replace('Sedition', '煽动')
        item = item.replace('Uprising', '起义')
        item = item.replace('Malice', '憎恶')
        item = item.replace('Heresy', '异端')
        item = item.replace('Damnation', '诅咒')
        item = item.replace('Mercantile HL-70-04', 'HL-70-04贸易区')
        item = item.replace('Consignment Yard HL-17-36', 'HL-17-36货运站')
        item = item.replace('Warren 6-19', '窄道 6-19')
        item = item.replace('Chasm Station HL-16-11', 'HL-16-11隘口站')
        item = item.replace('Chasm Logistratum', '隘口后勤处')
        item = item.replace('Archivum Sycorax', '档案馆')
        item = item.replace('Enclavum Baross', '巴洛斯飞地')
        item = item.replace('Magistrati Oubliette TM8-707', 'TM8-707法庭密牢')
        item = item.replace('Refinery Delta-17', 'D-17精炼厂')
        item = item.replace('Comms-Plex 154/2f', '154/2f通讯站')
        item = item.replace('Excise Vault Spireside-13', '尖塔区-13赃物库')
        item = item.replace('Silo Cluster 18-66/a', '18-66/a水仓群')
        item = item.replace('Ascension Riser 31', '31号升降机')
        item = item.replace('Power Matrix', '电力矩阵')
        item = item.replace('Started', '开始于')

        mmt_code = mmt_code + item + '\n'

    return mmt_code