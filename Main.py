"""Used to Load in, Train, and Test The Model"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
articles = datasets.load_files("Categories",description="News articles about AAPL scraped from NASDAQ.com",
                        shuffle=True, random_state=42)
print(len(articles.data))
print(articles.target_names)

def train(classifier, x, y):
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.25, random_state=42)

    classifier.fit(x_train, y_train)

    print("Accuracy: %s" % classifier.score(x_test, y_test))
    return classifier

trial_1 = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])
train(trial_1, articles.data, articles.target)










