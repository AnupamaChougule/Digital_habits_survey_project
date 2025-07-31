from flask import Flask,render_template,request,redirect
from flask import Response
import csv
import io
import mysql.connector
import qrcode
import logging

url="YOUR_PYTHONANYWHERE_URL"
qr=qrcode.make(url)
qr.save("form_qr.png")

app= Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def get_db():
    return mysql.connector.connect(
        host="YOUR_HOST",
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        database="YOUR_DATABASE_NAME"
        )

@app.route("/",methods=["GET","POST"])
def survey():
    if request.method=="POST":
        try:
            db=get_db()
            cursor=db.cursor()

            user_type=request.form["user_type"]
            full_name=request.form["full_name"]
            age=request.form["age"]
            gender=request.form["gender"]
            college_name=request.form["college_name"]
            year_of_study=request.form["year_of_study"]
            field_of_study=request.form["field_of_study"]
            preferred_device=request.form["preferred_device"]
            daily_screen_time=request.form["daily_screen_time"]
            social_media_platforms=request.form["social_media_platforms"]
            during_lectures=request.form["during_lectures"]
            primary_purpose=request.form["primary_purpose"]
            check_frequency=request.form["check_frequency"]
            academic_impact=request.form["academic_impact"]
            social_media_detox=request.form["social_media_detox"]
            favourite_content=request.form["favourite_content"]
            follow_influencers=request.form["follow_influencers"]
            influencer_name=request.form["influencer_name"] if follow_influencers=="Yes" else None
            purchase_based_on_ADs=request.form["purchase_based_on_ADs"]
            mental_health_impact=request.form["mental_health_impact"]
            privacy_concern=request.form["privacy_concern"]
            cyberbullying_experience=request.form["cyberbullying_experience"]
            security_measures=request.form["security_measures"]
            prefer_online_communication=request.form["prefer_online_communication"]
            reduce_usage_for_productivity=request.form["reduce_usage_for_productivity"]
            sleep_impact=request.form["sleep_impact"]
            deleted_account=request.form["deleted_account"]
            additional_comments=request.form["additional_comments"]

            query=""" INSERT INTO responses(user_type,full_name,age,gender,college_name,year_of_study,field_of_study,preferred_device,daily_screen_time,social_media_platforms,
            during_lectures,primary_purpose,check_frequency,academic_impact,social_media_detox,favourite_content,follow_influencers,influencer_name,
            purchase_based_on_ADs,mental_health_impact,privacy_concern,cyberbullying_experience,security_measures,prefer_online_communication,reduce_usage_for_productivity,
            sleep_impact,deleted_account,additional_comments) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            values=(user_type,full_name,age,gender,college_name,year_of_study,field_of_study,preferred_device,daily_screen_time,social_media_platforms,
            during_lectures,primary_purpose,check_frequency,academic_impact,social_media_detox,favourite_content,follow_influencers,influencer_name,
            purchase_based_on_ADs,mental_health_impact,privacy_concern,cyberbullying_experience,security_measures,prefer_online_communication,
            reduce_usage_for_productivity,sleep_impact,deleted_account,additional_comments)

            cursor.execute(query,values)
            db.commit()
            cursor.close()
            db.close()

            return redirect("/thankyou")
        except Exception as e:
            logging.error("Error while saving data:%s",str(e))
            return "An error occurred while submitting the form. Please try again later."

    return render_template("form.html")

@app.route("/export")
def export_csv():
    try:
        db=get_db()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM responses")
        rows=cursor.fetchall()
        column_names=[i[0] for i in cursor.description]
        output=io.StringIO()
        writer=csv.writer(output)
        writer.writerow(column_names)
        writer.writerows(rows)

        cursor.close()
        db.close()

        response=Response(output.getvalue(),mimetype="text/csv")
        response.headers["Content-Disposition"]="attachment;filename=survey_responses.csv"
        return response
    except Exception as e:
        logging.error("Error while exporting data:%s",str(e))
        return "Failed to export CSV. Please try again later."

@app.route("/thankyou")
def thank_you():
    return " Thank you for participating in the survey!"

if __name__=="__main__":
    app.run(debug=True)