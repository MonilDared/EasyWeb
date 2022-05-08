import os
import datetime
os.system("clear")
print("ＥａｓｙＷｅｂＦｒｏｍＧｉｔｈｕｂ\n----------------------------------")
time = datetime.datetime.now().strftime("%a--%b--%Y\n%-Ih--%-Mm--%p")
notn,yes = os.getcwd().split('/home/runner/')
inputa = input(f"{time}\n{yes} $ ")
if inputa.startswith("code "):
  notne,ne = inputa.split("code ")
  print(f"<code>{ne}</code>")