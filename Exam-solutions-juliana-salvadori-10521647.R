
# question 1

iris_new = read.csv("C:/Temp/input/iris.data")
head(iris_new)
colnames(iris_new) <- c('Sepal.Length', 'Sepal.Width','Petal.Length', 'Petal.Width', 'Species')
head(iris_new)

top5mean <- head(iris_new, 5)
top5mean
mean(top5mean$Sepal.Length)

mean( head(iris_new, 5)$Sepal.Length)

install.packages("stringr")
library(stringr)
iris_new$Species <- str_replace(iris_new$Species, 'Iris-', '')
head(iris_new)  

iris_new$Species <- tools::toTitleCase(iris_new$Species)
head(iris_new)

# question 2

iris_sub <- iris_new[ iris_new$Sepal.Length < 6.4 & iris_new$Petal.Length > 5.1, ]
nrow(iris_sub)
mean(iris_sub$Sepal.Width)
mean(iris_sub$Petal.Length)


# question 3




# question 4




# question 5

iris_sub <- iris_new[ , c(1,3,5) ]
head(iris_sub)

iris_sub[ iris_sub$Sepal.Length == 5.7 & iris_sub$Petal.Length == 4.1, ]$Species
