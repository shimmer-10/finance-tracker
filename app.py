from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)
expenses=[]

@app.route("/", methods=["GET","POST"])
def dashboard():
    recent_expenses=expenses[-5:][::-1]
    return render_template("dashboard.html",recent_expenses=recent_expenses)

@app.route("/expense" , methods=["GET","POST"])
def expense():
    return render_template("expense.html",expenses=expenses)

@app.route("/add", methods=["GET","POST"])
def add():
    source=request.args.get("source")
    if request.method=="POST":
        name=request.form.get("name")
        category=request.form.get("category")
        amount=request.form.get("amount")
        date=request.form.get("date")

        new_expense={"name":name , "category":category , "amount":amount, "date": date}
        expenses.append(new_expense)
        
        if source=="expense":
            return redirect(url_for("expense"))
        else:
            return redirect(url_for("dashboard"))

    return render_template("add.html", source=source)

@app.route("/budget" , methods=["GET","POST"])
def budget():
    if request.method=="POST":
        budget_amount=request.form.get("budget_amount")
        return redirect(url_for("budget"))
    
    return render_template("budget.html")

if __name__=="__main__":
    app.run(debug=True)