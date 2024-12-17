from flask import Flask,render_template,request

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

from src.pipeline.train_pipeline import TrainPipeline

application=Flask(__name__)

app=application

@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender= request.form.get("gender"),
            race_ethnicity= request.form.get("race_ethnicity"),
            parental_level_of_education= request.form.get("parental_level_of_education"),
            lunch= request.form.get("lunch"),
            test_preparation_course= request.form.get("test_preparation_course"),
            reading_score= request.form.get("reading_score"),
            writing_score= request.form.get("writing_score"),
        )

        pred_df=data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        results= predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
@app.route('/train', methods=['GET', 'POST'])
def train_model():
    training_completed = False
    model_performance = None
    model_name = None
    
    if request.method == 'POST':
        pipeline = TrainPipeline()
        model_performance, model_name = pipeline.train()
        training_completed = True
    
    return render_template('train.html', 
                           training_completed=training_completed,
                           model_performance=model_performance,
                           model_name=model_name)

    
if __name__ == "__main__":
    print("Working")
    app.run(port=5050,host="0.0.0.0")