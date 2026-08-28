# load the iris dataset as an example 
from sklearn.datasets import load_iris 
iris = load_iris() 

print( "\n====================================" )
print( "\nLoad dataset" )
print( "\n====================================" )
    
# store the feature matrix (X) and response vector (y) 
X = iris.data 
y = iris.target 
    
# store the feature and target names 
feature_names = iris.feature_names 
target_names = iris.target_names 
    
# printing features and target names of our dataset 
print("Feature names:", feature_names) 
print("Target names:", target_names) 
    
# X and y are numpy arrays 
print("\nType of X is:", type(X)) 
    
# printing first 5 input rows 
print("\nFirst 5 rows of X:\n", X[:5])

print( "\n====================================" )
print( "\nSplitting the dataset" )
print( "\n====================================" )

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
  
# printing the shapes of the new X objects
print( "\nprinting the shapes of the new X objects" )
print(X_train.shape)
print(X_test.shape)
  
# printing the shapes of the new y objects
print( "\nprinting the shapes of the new y objects" )
print(y_train.shape)
print(y_test.shape)

print( "\n====================================" )
print( "\nTraining the model" )
print( "\n====================================" )

# training the model on training set
print( "\ntraining the model on training set using knn classifier " )
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

print( "\nThe classifier is trained using X_train data. The process is termed fitting" )
knn.fit(X_train, y_train)
  
# making predictions on the testing set
print( "\nmaking predictions on the testing set. test our classifier on the X_test data. knn.predict method is used for this" )
y_pred = knn.predict(X_test)
  
# comparing actual response values (y_test) with predicted response values (y_pred)
print( "\ncomparing actual response values (y_test) with predicted response values (y_pred)" )
from sklearn import metrics
print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))
  
# making prediction for out of sample data
print( "\nmaking prediction for out of sample data" )
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)
  
# saving the model
print( "\nsaving the model" )
import joblib
joblib.dump(knn, 'iris_knn.pkl')