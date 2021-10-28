pima <- read.csv('./data/pima2.csv', header = T)

classify <- function(age) {
    if (age <= 19) {
        return('0~19')
    }else if (20 <= age && age <= 30) {
        return('20~30')
    }else if (31 <= age && age <= 40) {
        return('31~40')
    }else if (41 <= age && age <= 50) {
        return('41~50')
    }else {
        return('50+')
    }
}

pima$age <- unlist(lapply(pima$age, classify))
tbl <- table(pima$age, pima$diabetes)
tbl
barplot(t(tbl), col = 1:2, legend = colnames(tbl))