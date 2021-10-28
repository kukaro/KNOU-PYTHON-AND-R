pima <- read.csv('./data/pima2.csv', header = T)

classify <- function(pregnant) {
    if (pregnant <= 5) {
        return('0~5')
    }else if (6 <= pregnant && pregnant <= 10) {
        return('6~10')
    }else {
        return('10+')
    }
}

pima$pregnant <- unlist(lapply(pima$pregnant, classify))
tbl <- table(pima$pregnant, pima$diabetes)
tbl
barplot(t(tbl), col = 1:2, legend = colnames(tbl))