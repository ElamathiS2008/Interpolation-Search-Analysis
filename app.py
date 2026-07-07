from flask import Flask, render_template, request

from task1 import interpolation_search

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        try:

            arr = list(map(int, request.form["array"].split()))

            arr.sort()

            target = int(request.form["target"])

            index, comparisons = interpolation_search(arr, target)

            if index == -1:

                result = f"Element not found | Comparisons = {comparisons}"

            else:

                result = (
                    f"Element found at index {index}"
                    f" | Comparisons = {comparisons}"
                )

        except Exception:

            result = "Please enter valid numbers."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
