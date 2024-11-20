from class_2 import Sample
s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4,
            petal_width=0.2, species='Iris-setosa')
print(s2, '\n')

s2.classification = 'wrong'
print(s2)
