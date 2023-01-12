import json

def applyChanges(window, startBtn, endBtn, isSecondBox):
  with open("config.json", "w") as file:
    json.dump(
      {
        "isSecondBox": isSecondBox,
        "bindStartButton": startBtn,
        "bindEndButton": endBtn
      },
      file
    )
  window.destroy()

def getSettings():
  with open("config.json", "r") as file:
    data = file.read()
    jsonData = json.loads(data)

  return jsonData