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

topLine = "WELCOME TO"
print(f"{topLine: ^50}")
armbook = f"--    ARMBOOK    --"
colorText("blue", f"\n{armbook: ^50}")
print()
print()
text1 = "Definitely not a rip off of"
colorText("yellow", f"\n{text1: >50}")
text2 = "a certain other social"
colorText("yellow", f"\n{text2: >50}")
text3 = "networking site."
colorText("yellow", f"\n{text3: >50}")
print()
honest = "Honest."
colorText("red", f"\n{honest: ^50}")
print()
username = "Username:"
password = "Password:"
colorText("reset", f"\n{username: ^50}")
print(f"\n{password: ^50}")