import os
import pytz
import datetime
os.system("clear")
print("ＥａｓｙＷｅｂＦｒｏｍＧｉｔｈｕｂ\n----------------------------------")

loop = True
while loop:
  time = datetime.datetime.now(pytz.timezone('Asia/Calcutta')).strftime("%a--%b--%Y\n%-Ih--%-Mm--%p")
  notn,yes = os.getcwd().split('/home/runner/')
  inputa = input(f"{time}\n{yes} $ ")
  if inputa.startswith("code "):
    notne,ne = inputa.split("code ")
    print(f"<code>{ne}</code>")
  elif inputa == "exit":
    loop = False
  elif inputa == "cla":
    os.system("clear")
    print("ＥａｓｙＷｅｂＦｒｏｍＧｉｔｈｕｂ\n----------------------------------")
  elif inputa.startswith("heading "):
    notne,ne = inputa.split("heading ")
    print(f"<h1>{ne}</h1>")