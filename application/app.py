from flask import Flask, jsonify, render_template

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Amit",
        "role": "DevOps Engineer",
        "department": "Engineering"
    },
    {
        "id": 2,
        "name": "Priya",
        "role": "Cloud Engineer",
        "department": "Infrastructure"
    },
    {
        "id": 3,
        "name": "Rahul",
        "role": "Software Developer",
        "department": "Development"
    },
    {
        "id": 4,
        "name": "Sneha",
        "role": "QA Engineer",
        "department": "Testing"
    }
]


# Home Route
@app.route("/")
def home():
    return render_template("index.html", employees=employees)


# Get All Employees API
@app.route("/api/employees")
def get_employees():
    return jsonify(employees)


# Health Check API
@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "Employee Management App"
    }), 200


# Get Employee by ID API
@app.route("/api/employees/<int:employee_id>")
def get_employee(employee_id):

    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee:
        return jsonify(employee), 200

    return jsonify({
        "error": "Employee not found"
    }), 404


# Run Flask Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
