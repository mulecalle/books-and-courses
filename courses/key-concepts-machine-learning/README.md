# Key Concepts Machine Learning

```
https://www.pluralsight.com/courses/key-concepts-machine-learning
```

ML vs DL

features are choosen by us - the model chose the features to use

structures data - un structure data

both can solve problems : 
  Classification, classify input data into categories. (supervised)
  Regression, predict continuous numeric values. (supervised)
  Clustering, discover patterns and grouping in data. (unsupervised)
  Dimensionality reduction, find latent or significant features in data. (unsupervised)

white box - black box

scikit-learn - tensorflow / keras / pytorch

both

ML models starts to decreade when they are deployed into production. 
  Models needs to be re trained based on new data
    A constant stream of new data is necessary to the model
      It's something like "the model needs to be updated with the shifting reallity of the world"


ML algo types:
  supervised, labels associted with the training data is used to correct the algo
    x input, y output
    y = fn(x) -> approximate the mapping fuction so in new values of x we can predict y
    algo learns from the feed data


  unsupervised, the models has to be set up right to learn structure in the data
    x input, no output
    algo self discover the patterns and structure in the data
    models works on their own with no labeled data

-- functions

ds.info()

ds.describe()

histplot(n)

outliers = raws in the data que me hacen ruido en el modelo, rompen lo homogeneo del set
  para removerlos de un set creo un subset de [~f(n)]


con los null values en el set, opciones:
  - los remuevo si tengo un set grande
  - los relleno con mean()
