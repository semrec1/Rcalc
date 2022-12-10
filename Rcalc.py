#a.find basic descriptive statistcs
library(datasets)  # Load built-in datasets
mtcars # loads in sample datasets for cars
summary(mtcars)
str(mtcars) #displays structure of dataset
quantile(mtcars$mpg)

cars#loads cars dataset
summary(cars)
quantile(cars$speed)
class(cars) # displays class of dataset
dim(cars) #displays dimensions of dataset
str(cars)

#b.find subset of dataset using subset() , aggregate()
aggregate(.~Species,data=iris,mean)
subset(iris,iris$Sepal.Length==5.0)

# Clear packages
detach("package:datasets", unload = TRUE)  # For base
