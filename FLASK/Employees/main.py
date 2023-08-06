from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for("employees"))

@app.route("/employees", methods=['GET', 'POST'])
def employees():
    if request.method == "GET":
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        data = requests.get("http://localhost:8080/employees").json()
        return render_template("employees.html", data=data, sectors=sectorData)
    elif request.method == "POST":
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        id = request.form["select"]
        if id == "-1":
            data = requests.get(f"http://localhost:8080/employees").json()
        else:
            data = requests.get(f"http://localhost:8080/employees/search?sectorId={id}").json()
        return render_template("employees.html", data=data, sectors=sectorData)

@app.route("/sectors", methods=['GET', 'POST'])
def sectors():
    if request.method == "GET":
        data = requests.get("http://localhost:8080/sectors").json()
        return render_template("sectors.html", data=data)

@app.route("/employees/<int:id>", methods=['GET', 'POST'])
def employeeDetails(id):
    if request.method == "GET":
        data = requests.get(f"http://localhost:8080/employees/{id}").json()
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        return render_template("employeeDetails.html", employee=data, sectors=sectorData)
    elif request.method == "POST":
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        edit = {"name": request.form["name"],
                "email": request.form["email"],
                "phone": request.form["phone"],
                "birthday": request.form["birthday"],
                "baseSalary": request.form["salary"], 
                "imgUrl": request.form["img"],
                "sector": {"id": request.form["select"]}}
        req = requests.put(f"http://localhost:8080/employees/{id}", json=edit)
        return redirect(url_for("employees"))
    
@app.route("/create/employee", methods=["GET", "POST"])
def createEmployee():
    if request.method == "GET":
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        return render_template("createEmployee.html", sectors=sectorData)
    elif request.method == "POST":
        sectorData = requests.get(f"http://localhost:8080/sectors").json()
        insert = {"name": request.form["name"],
                  "email": request.form["email"],
                  "phone": request.form["phone"],
                  "birthday": request.form["birthday"],
                  "baseSalary": request.form["salary"], 
                  "imgUrl": request.form["img"],
                  "sector": {"id": request.form["select"]}}
        req = requests.post(f"http://localhost:8080/employees", json=insert)
        return redirect(url_for("employees"))

@app.route("/delete/employee/<int:id>", methods=["GET", "POST"])
def deleteEmployee(id):
    req = requests.delete(f"http://localhost:8080/employees/{id}")
    return redirect(url_for("employees"))


@app.route("/sectors/<int:id>", methods=["GET", "POST"])
def sectorDetails(id):
    if request.method == "GET":
        data = requests.get(f"http://localhost:8080/sectors/{id}").json()
        return render_template("sectorDetails.html", sector=data)
    elif request.method == "POST":
        edit = {"name": request.form["name"]}
        req = requests.put(f"http://localhost:8080/sectors/{id}", json=edit)
        return redirect(url_for("sectors"))

@app.route("/create/sector", methods=["GET", "POST"])
def createSector():
    if request.method == "GET":
        return render_template("createSector.html")
    elif request.method == "POST":
        insert = {"name": request.form["name"]}
        req = requests.post("http://localhost:8080/sectors", json=insert)
        return redirect(url_for("sectors"))
    
@app.route("/delete/sector/<int:id>", methods=["GET", "POST"])
def deleteSector(id):
    req = requests.delete(f"http://localhost:8080/sectors/{id}")
    return redirect(url_for("sectors"))

@app.route("/payments", methods=["GET", "POST"])
def payments():
    if request.method == "GET":
        employeesData = requests.get(f"http://localhost:8080/employees").json()
        data = requests.get("http://localhost:8080/payments").json()
        return render_template("payments.html", data=data, employees=employeesData)
    elif request.method == "POST":
        employeesData = requests.get(f"http://localhost:8080/employees").json()
        id = request.form["select"]
        if id == "-1":
            data = requests.get(f"http://localhost:8080/payments").json()
        else:
            data = requests.get(f"http://localhost:8080/payments/search?employeeId={id}").json()
        return render_template("payments.html", data=data, employees=employeesData)

@app.route("/payments/<int:id>", methods=["GET", "POST"])
def paymentDetails(id):
    if request.method == "GET":
        data = requests.get(f"http://localhost:8080/payments/{id}").json()
        employees = requests.get(f"http://localhost:8080/employees").json()
        return render_template("paymentDetails.html", payment=data, employees=employees)
    elif request.method == "POST":
        edit = {"amount": request.form["amount"], "date": request.form["date"]}
        employeeId = request.form["employeeId"]
        req = requests.put(f"http://localhost:8080/payments/{id}?employeeId={employeeId}", json=edit)
        return redirect(url_for("payments"))
    
@app.route("/create/payment", methods=["GET", "POST"])
def createPayment():
    if request.method == "GET":
        employees = requests.get(f"http://localhost:8080/employees").json()
        return render_template("createPayment.html", employees=employees)
    elif request.method == "POST":
        insert = {"amount": request.form["amount"], "date": request.form["date"]}
        employeeId = request.form["employeeId"]
        req = requests.post(f"http://localhost:8080/payments/insert?employeeId={employeeId}", json=insert)
        return redirect(url_for("payments"))
    
@app.route("/delete/payment/<int:id>", methods=["GET", "POST"])
def deletePayment(id):
    req = requests.delete(f"http://localhost:8080/payments/{id}")
    return redirect(url_for("payments"))

if __name__ == "__main__":
    app.run(debug=True)