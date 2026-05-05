from flask import Flask,request,render_template

app=Flask(__name__)
expenses=[]
@app.route("/", methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/expense" , methods=["GET","POST"])
def expense():
    return render_template("expense.html")

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method=="POST":
        source=request.args.get("source")
        expense_name=request.form.get("expense_name")
        category=request.form.get("category")
        amount=request.form.get("amount")
        date=request.form.get("date")

        new_expense={"expense_name" : expense_name , "category":category , "amount":amount, "date": date}
        expenses.append(new_expense)

    return render_template("add.html")

if __name__=="__main__":
    app.run(debug=True)