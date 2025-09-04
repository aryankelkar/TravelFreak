from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Features Page
@app.route("/features")
def features():
    return render_template("features.html")

# Community Blogs & Reviews
@app.route("/community")
def community():
    return render_template("community.html")

# Trip Planner
@app.route("/planner")
def planner():
    return render_template("planner.html")

# Travel Tools (Maps, Translator, Stats)
@app.route("/tools")
def tools():
    return render_template("tools.html")

# Booking Page (commodities like bikes/rentals)
@app.route("/booking")
def booking():
    return render_template("booking.html")

# Gamification (points, rewards, leaderboard)
@app.route("/gamification")
def gamification():
    return render_template("gamification.html")

if __name__ == "__main__":
    app.run(debug=True)
