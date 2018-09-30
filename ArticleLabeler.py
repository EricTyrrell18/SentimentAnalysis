import pandas
import pandas_datareader
import os
class ArticleLabeler:
    def __init__(self, filename):
        self.create_directories()

        self.grouped_df = self.read_csv(filename)

        start_date = self.grouped_df["date_published"].min()[0]
        end_date = self.grouped_df["date_published"].max()[0]
        print("start = " + start_date)
        print("end = " + end_date)
        print(type(start_date))
        print(end_date)
        self.stock_df = pandas_datareader.DataReader("AAPL", "iex", "9-27-2018")

    def create_directories(self):
        labels = ("Positive", "Negative")

        for label in labels:
            #Create the directories if they don't exist already
            try:
                os.mkdir(label)
            except OSError:
                pass

    def write_file(self):
        for name, group in self.grouped_df:
            filename = self.label_article(name)+ "/" + name
            file = open(filename, "a+")
            for index, row in group.iterrows():
                file.write(row['text'])
            file.close()


    def label_article(self, date):
        """Returns a string - 'Positive' or 'Negative' based on the open and closing prices"""
        historical_price = self.stock_df.loc[date]
        if float(historical_price['open'] > float(historical_price['close'])):
            return "Negative"
        else:
            return "Positive"


    def read_csv(self, filename):
        df = pandas.read_csv(filename).groupby("date_published")
        return df


k = ArticleLabeler("test.csv")
k.write_file()