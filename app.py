from flask import Flask, render_template, request, jsonify
from pipeline import run_research_pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("langchain_researcher.html")


@app.route("/research", methods=["POST"])
def research():
    try:
        data = request.get_json()
        topic = data.get("topic")

        result = run_research_pipeline(topic)

        return jsonify({
            "success": True,
            "search_results": result.get("search_results", ""),
            "scrape_result": result.get("scrape_result", ""),
            "report": result.get("report", ""),
            "feedback": result.get("feedback", "")
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)