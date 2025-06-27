from flask import Flask, request, render_template_string

app = Flask(__name__)

UPLOAD_HTML = """
<!doctype html>
<title>LegalSage Contract Upload</title>
<h2>Upload Contract File (.txt)</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=contract_file accept=".txt" required>
  <input type=submit value=Upload>
</form>

{% if filename %}
  <h3>Uploaded: {{ filename }}</h3>
  <pre>{{ preview }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def upload_contract():
    filename = None
    preview = None

    if request.method == "POST":
        file = request.files.get("contract_file")
        if file and file.filename.endswith(".txt"):
            filename = file.filename
            content = file.read().decode("utf-8")
            preview = content[:500]

    return render_template_string(UPLOAD_HTML, filename=filename, preview=preview)

if __name__ == "__main__":
    app.run(debug=True)
