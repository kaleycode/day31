def colorText(color, word):
  if color =="red":
    print("\033[31m", word, sep="", end="")
  elif color =="orange":
    print("\033[33m", word, sep="", end="")
  elif color =="green":
    print("\033[32m", word, sep="", end="")
  elif color =="blue":
    print("\033[34m", word, sep="", end="")
  elif color =="yellow":
    print("\033[33m", word, sep="", end="")
  elif color =="purple":
    print("\033[35m", word, sep="", end="")
  elif color =="cyan":
    print("\033[36m", word, sep="", end="")

  else:
    print("\033[0m", word, sep="", end="")
    
topLine = f"🎶 Music App 🎶"
colorText("yellow", f"{topLine: ^50}")
print()
print()
colorText("reset","🔥▶️ \tRadio Gaga")
colorText("yellow", "\n\t\tQueen")
print()
print()
print()
colorText("reset", "PREV")
colorText("green", "\n\t\tNEXT")
print()
lastLine = "PAUSE"
colorText("purple", f"{lastLine: ^35}")