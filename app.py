import os
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)
fretta_listi = [
    ["0","Best Birthday party in the world","The coolest fucker in the world is holding a birthday party this friday and all the cool kids are going","newsforschool@kidz.com","birthday.jpg"],
    ["1","Minecraft Wins","Minecraft has taken over the world and everything has now become creeper themed","helpUs@notajoke.com","creeper.jpg"],
    ["2","Man fucking dies","This dude just fuckin died, drop an F in the chat","chad@coolkidz.com","rip.jpg"],
    ["3","Best game in the world","New research found that the best game in the world is not Fortnite,scientists are shocked","britebomber@epicgames.net","fortnite.png"]
]
@app.route('/')
def home():
    dicta = {"Seimur Sindrason":696942096,"Sesselja Bolla":1609022560,"Guðmundur Jón":1908042530,"Lárus Lárusson":1012493920}
    return render_template("homepage.html", kennitolur = dicta )

@app.route('/sida/<kt>')
def summma(kt):
    kt_list = map(int,kt)
    summa = sum(kt_list)
    return render_template("summa.html", kt=kt, summa=summa)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    #app.run()
    app.run(debug=True, use_reloader=True)