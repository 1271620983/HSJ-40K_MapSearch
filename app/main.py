import json
from khl import Bot, Message, MessageTypes, Event, EventTypes
from khl.card import Card, CardMessage, Module, Types, Element, Struct
from app.bot_ini import bot
from app.data_crawling import get_data,result_format

@bot.command(name="ping")
async def ping(msg: Message):
    await msg.channel.send("为了帝皇！")

@bot.command(name="map",aliases=["地图","地图选择","search"])
async def ping(msg: Message):
    with open('map_pick.json', 'r', encoding='utf-8') as f:
        map_card = json.load(f)
    await msg.reply(map_card,type=MessageTypes.CARD)

@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def btn_click_event(b:Bot,e:Event):
    """按钮点击事件"""
    map_list = ["Mercantile","Consignment Yard","Warren 6-19","Chasm Station","Chasm Logistratum","Archivum Sycorax",\
                "Enclavum Baross","Magistrati Oubliette","Refinery Delta-17","Comms-Plex 154/2f","Excise Vault Spireside-13",\
                "Silo Cluster 18-66/a","Ascension Riser 31","Power Matrix"]
    diffculy_list = ["Sedition","Uprising","Malice","Heresy","Damnation","Gold_Damnation"]

    ch = await bot.client.fetch_public_channel("4297108093677404")

    if e.body['value'] in map_list:
        with open('diffcult_pick.json', 'r', encoding='utf-8') as f:
            diffcult_card = json.load(f)
        global map_name
        map_name = e.body['value']
        await ch.send(target='ch',content=diffcult_card,type=MessageTypes.CARD)

    elif e.body['value'] in diffculy_list:
        diffcult_name = e.body['value']
        result = get_data(map_name,diffcult_name)
        mmt_code = result_format(result)
        if len(mmt_code) == 0:
            await ch.send("没有找到符合条件的任务")
        else:
            await ch.send(mmt_code)

# if __name__ == "__main__":
#     bot.run()