from WhatsAnalyzerWeb import app
from flask import render_template, request, url_for, redirect, session
from WhatsAnalyzerWeb.analyzer.analyzer import Analyzer
from WhatsAnalyzerWeb.analyzer.plotter import Plotter

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_file():
    session["chat"] = request.files["chat"].read()
    return redirect(url_for("report"))

@app.route("/report/")
def report():
    def as_html(ascii_img):
        return f"<img class='card-img-top img-fluid mt-auto' src='data:image/png;base64,{ascii_img}'/>"

    try:
        chat_read = session["chat"]
        session.clear()
    except KeyError:
        return redirect(url_for("index"))

    anl = Analyzer(chat_read)
    plt = Plotter(anl.manager.messages)
    
    os=anl.manager.os
    emoji_dict=anl.user_most_common_emojis()
    word_dict=anl.user_most_common_words()
    media_dict=anl.user_count_media()
    link_list=anl.most_common_links()
    
    chat_facts = {}
    chat_facts["Nachrichten gesamt"] = anl.total_msg_count()
    chat_facts["Nachrichten pro Tag"] = round(anl.chat_avg_msg_per_day())
    

    msg_per_person_per_week=as_html(
        plt.plot_user_messages_over_time())

    media_per_user=as_html(
        plt.plot_user_vs_number_dict(
            anl.user_count_media(sum_only=True),
            mode="pie"))

    conv_start=as_html(
        plt.plot_user_vs_number_dict(
            anl.user_start_conversation(),
            mode="pie",
            label_func=lambda s: f"{s}%"))

    msg_len_per_user=as_html(
        plt.plot_user_vs_number_dict(
            anl.user_avg_word_count(),
            mode="bar"))

    msg_by_weekday=as_html(
        plt.plot_group_messeges_by(
            "weekday"))

    msg_by_hour=as_html(
        plt.plot_group_messeges_by(
            "hour"))

    msg_per_week=as_html(
        plt.plot_total_messages_over_time())

    msg_per_user=as_html(
        plt.plot_user_vs_number_dict(
            anl.user_msg_count(),
            mode="pie"))

    return render_template("report.html",
            link_list=link_list,
            chat_facts=chat_facts,
            
            os=os,
            emoji_dict=emoji_dict,
            word_dict=word_dict,
            media_dict=media_dict,
            
            msg_per_person_per_week=msg_per_person_per_week,
            media_per_user=media_per_user,
            conv_start=conv_start,
            msg_len_per_user=msg_len_per_user,
            msg_by_weekday=msg_by_weekday,
            msg_by_hour=msg_by_hour,
            msg_per_week=msg_per_week,
            msg_per_user=msg_per_user)