import discord

client = discord.Client()
token = 'Nzc3MDk4MDI2NDEzMDY0MjA0.X6-e7w.fX2h-sCLCdeh5FXHgIdCE6Q0d4k'

@client.event
async def on_ready():
    print('=====================================')
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')

@client.event
async def on_message(message):
    if message.content.startswith('?청소') or message.content.startswith('?삭제'):
        if message.author.guild_permissions.administrator or message.author.guild_permissions.manage_messages or message.author.id == 534214957110394881:
            varrr = message.content.split(' ')
            await message.channel.purge(limit=int(varrr[1]) + 1)
            msg = await message.channel.send(
                embed=discord.Embed(title=f':yes:메시지 {str(int(varrr[1]))}개 삭제 완료!:yes:', descirption='루피가 삭제했어요!!',
                                    colour=0xfc00f4).set_footer(icon_url='https://images-ext-1.discordapp.net/external/vJpRtzfm6vVqfY3YeLLtcO1U1DsxL2TG5CwgzWXInKg/%3Fitemid%3D15950157/https/media1.tenor.com/images/299cf0fe5129cecd4bb839a2dba7e07a/tenor.gif',
                                                              text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일'))
        else:
            embed = discord.Embed(color=discord.Colour.red(),
                                  title=' :no:사용불가:no:  ',
                                  description='사용불가 명령어 입니다\n(서버 관리자 명령어)', timestamp=message.created_at)
            embed.set_footer(text=f"{message.author}", icon_url='https://images-ext-1.discordapp.net/external/vJpRtzfm6vVqfY3YeLLtcO1U1DsxL2TG5CwgzWXInKg/%3Fitemid%3D15950157/https/media1.tenor.com/images/299cf0fe5129cecd4bb839a2dba7e07a/tenor.gif')
            await message.channel.send(embed=embed)


client.run(token)
