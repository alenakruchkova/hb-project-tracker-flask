from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student_add")
def student_add():
    """Add a student."""

    return render_template("new_student.html")



@app.route("/new_student_confirmation", methods=['POST'])
def new_student_confirm():
    """Confirms that new student has been registered and provides link to student page"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")

    return render_template("new_student_confirmation.html",
                            fname=first_name,
                            lname=last_name)


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html





if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
