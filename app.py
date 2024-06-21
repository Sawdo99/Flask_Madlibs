from stories import Story

@app.route("/")
def ask_questions():
    """asks question."""

    prompts = story.prompts

    return render_template("page.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)