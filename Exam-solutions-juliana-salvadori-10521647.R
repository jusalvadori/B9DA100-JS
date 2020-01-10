# Juliana Salvadori
# student number: 10521647


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

par(mfrow = c(2, 2))

boxplot( iris_new$Sepal.Length ~ iris_new$Species,
        xlab = "Species",
        xaxt = "n",
        col = 2:6,
        main = "Sepal.Length", 
        ylab = "Sepal.Length",
        las=2)
axis(1, at = 1:3, labels = c("Setosa", "Versicolor", "Virginica"))

boxplot(iris_new$Sepal.Width ~ iris_new$Species ,
        xlab = "Species",
        xaxt = "n",
        col = 2:6,
        main = "Sepal.Width", 
        ylab = "Sepal.Width",
        las=2)
axis(1, at = 1:3, labels = c("Setosa", "Versicolor", "Virginica"))

boxplot(iris_new$Petal.Length ~ iris_new$Species ,
        xlab = "Species",
        xaxt = "n",
        col = 2:6,
        main = "Petal.Length", 
        ylab = "Petal.Length",
        las=2)
axis(1, at = 1:3, labels = c("Setosa", "Versicolor", "Virginica"))

boxplot(iris_new$Petal.Width ~ iris_new$Species ,
        xlab = "Species",
        xaxt = "n",
        col = 2:6,
        main = "Petal.Width",
        ylab = "Petal.Width",
        las=2)
axis(1, at = 1:3, labels = c("Setosa", "Versicolor", "Virginica"))


# question 4
library(ggplot2)

par(mfrow = c(1, 2))

# Change point shapes and colors
ggplot(iris_new, aes(x=Sepal.Width, y=Sepal.Length, shape=Species, color=Species)) +
  geom_point()


# Change point shapes and colors
ggplot(iris_new, aes(x=Petal.Width, y=Petal.Length, shape=Species, color=Species)) +
  geom_point()



# question 5

iris_sub <- iris_new[ , c(1,3,5) ]
head(iris_sub)

iris_sub[ iris_sub$Sepal.Length == 5.7 & iris_sub$Petal.Length == 4.1, ]$Species
