
# coding: utf-8

# In[84]:


"Simple classification example"
import unittest
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# In[79]:


def build_model():
    "Builds classification model"
    data = load_breast_cancer()
    labels = data['target']
    features = data['data']
    train, test, train_labels, test_labels = train_test_split(
        features,
        labels,
        test_size=0.33,
        random_state=42)
    gnb = GaussianNB()
    model = gnb.fit(train, train_labels)
    print test_labels
    print test[0]
    return model


# In[80]:


def test_model(model, value):
    "Run model on given value"
    return model.predict(value)


# In[81]:


class ClassificationTest(unittest.TestCase):
    """Example of how to use unittest in Jupyter."""
    def setUp(self):
        self.test_model = build_model()
        self.positive_test = [[1.247e+01, 1.860e+01, 8.109e+01, 4.819e+02, 9.965e-02
                               , 1.058e-01, 8.005e-02, 3.821e-02, 1.925e-01, 6.373e-02
                               , 3.961e-01, 1.044e+00, 2.497e+00, 3.029e+01, 6.953e-03
                               , 1.911e-02, 2.701e-02, 1.037e-02, 1.782e-02, 3.586e-03
                               , 1.497e+01, 2.464e+01, 9.605e+01, 6.779e+02, 1.426e-01
                               , 2.378e-01, 2.671e-01, 1.015e-01, 3.014e-01, 8.750e-02]]
        self.negative_test = [[1.894e+01, 2.131e+01, 1.236e+02, 1.130e+03, 9.009e-02
                               , 1.029e-01, 1.080e-01, 7.951e-02, 1.582e-01, 5.461e-02
                               , 7.888e-01, 7.975e-01, 5.486e+00, 9.605e+01, 4.444e-03
                               , 1.652e-02, 2.269e-02, 1.370e-02, 1.386e-02, 1.698e-03
                               , 2.486e+01, 2.658e+01, 1.659e+02, 1.866e+03, 1.193e-01
                               , 2.336e-01, 2.687e-01, 1.789e-01, 2.551e-01, 6.589e-02]]
    def test(self):
        "Assert values"
        positive_value = test_model(self.test_model, self.positive_test)
        negative_value = test_model(self.test_model, self.negative_test)
        self.assertEqual(positive_value[0], 1)
        self.assertEqual(negative_value[0], 0)


# In[82]:


TEST_CLASS = ClassificationTest("test")
SUITE = unittest.TestLoader().loadTestsFromModule(TEST_CLASS)
unittest.TextTestRunner().run(SUITE)


# In[85]:


# Nose test cases
POSITIVE_TEST = [[1.247e+01, 1.860e+01, 8.109e+01, 4.819e+02, 9.965e-02
                  , 1.058e-01, 8.005e-02, 3.821e-02, 1.925e-01, 6.373e-02
                  , 3.961e-01, 1.044e+00, 2.497e+00, 3.029e+01, 6.953e-03
                  , 1.911e-02, 2.701e-02, 1.037e-02, 1.782e-02, 3.586e-03
                  , 1.497e+01, 2.464e+01, 9.605e+01, 6.779e+02, 1.426e-01
                  , 2.378e-01, 2.671e-01, 1.015e-01, 3.014e-01, 8.750e-02]]
NEGATIVE_TEST = [[1.894e+01, 2.131e+01, 1.236e+02, 1.130e+03, 9.009e-02
                  , 1.029e-01, 1.080e-01, 7.951e-02, 1.582e-01, 5.461e-02
                  , 7.888e-01, 7.975e-01, 5.486e+00, 9.605e+01, 4.444e-03
                  , 1.652e-02, 2.269e-02, 1.370e-02, 1.386e-02, 1.698e-03
                  , 2.486e+01, 2.658e+01, 1.659e+02, 1.866e+03, 1.193e-01
                  , 2.336e-01, 2.687e-01, 1.789e-01, 2.551e-01, 6.589e-02]]
TEST_MODEL = build_model()
def test_classifier(self):
    "Assert values"
    positive_value = test_model(TEST_MODEL, POSITIVE_TEST)
    negative_value = test_model(TEST_MODEL, NEGATIVE_TEST)
    self.assertEqual(positive_value[0], 1)
    self.assertEqual(negative_value[0], 0)

