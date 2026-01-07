from appJar import gui
i = "X"

def btnClick(name):
    global i
    if app.getButton(name) != "X" or app.getButton(name) != "O":
        app.setButton(name, i)
        if i == "X":
            i = "O"
        else:
            i = "X"
    else:
        print("Dit vakje is bezet!") # Veranderen naar GUI-melding


def btnReset(name):
    app.setButton("btn1", "  ")
    app.setButton("btn2", "  ")
    app.setButton("btn3", "  ")
    app.setButton("btn4", "  ")
    app.setButton("btn5", "  ")
    app.setButton("btn6", "  ")
    app.setButton("btn7", "  ")
    app.setButton("btn8", "  ")
    app.setButton("btn9", "  ")


app = gui("TicTacToe", "300x350")
app.setFont(size=20)
app.addLabel("titel", "TicTacToe", 0, 0, 3)
app.addLabel("status", "hallo", 1, 0)

app.addNamedButton("  ", "btn1", btnClick, 1, 0)
app.addNamedButton("  ", "btn2", btnClick, 1, 1)
app.addNamedButton("  ", "btn3", btnClick, 1, 2)
app.addNamedButton("  ", "btn4", btnClick, 2, 0)
app.addNamedButton("  ", "btn5", btnClick, 2, 1)
app.addNamedButton("  ", "btn6", btnClick, 2, 2)
app.addNamedButton("  ", "btn7", btnClick, 3, 0)
app.addNamedButton("  ", "btn8", btnClick, 3, 1)
app.addNamedButton("  ", "btn9", btnClick, 3, 2)

app.addButton("reset", btnReset, 4, 0, 3)

app.go()