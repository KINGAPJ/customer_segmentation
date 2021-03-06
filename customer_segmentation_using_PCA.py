import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

dataset = pd.read_csv("Wine.csv")
X = dataset.iloc[: , :-1].values
y = dataset.iloc[ : ,-1].values

# Splitting dataset into test set and training set
from sklearn.model_selection import train_test_split
print(sklearn.__version__)
X_train , X_test , y_train , y_test = train_test_split(X, y , test_size = 0.2 ,random_state =0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

# Training Logistic Regression model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state= 0)
classifier.fit(X_train,y_train)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test , y_pred)

# Accuracy of the model
from sklearn.metrics import accuracy_score
accuracy_score(y_test , y_pred)

# Visualizing Training set result
from matplotlib.colors import ListedColormap
X_set , y_set = X_train , y_train
X1,X2= np.meshgrid(np.arange(start = X_set[: ,0].min() -1,
                             stop = X_set[: , 0].max()+1,step =0.01 ),
                   np.arange(start = X_set[: , 1].min()-1 ,
                             stop = X_set[: ,1].max()+1 ,step =0.01))
plt.contourf(X1 ,X2 ,classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red' ,'green','blue')))

for i , j in enumerate (np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] ,X_set[y_set == j ,1] ,
                c = ListedColormap(('red' ,'green','blue'))(i),label = j )
    
plt.title("Logistic Regression after PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()

plt.show()
                   
