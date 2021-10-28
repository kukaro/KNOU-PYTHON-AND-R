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


for (col in c('glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree')) {
    print(paste0('**********:', col))
    print('##########:MEAN')
    print(aggregate(pima[col], list(diabetes = pima$diabetes), mean, na.rm = T))
    print('##########:SD')
    print(aggregate(pima[col], list(diabetes = pima$diabetes), sd, na.rm = T))
}
pima$pregnant <- unlist(lapply(pima$pregnant, classify))

for (col in c('glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree')) {
    print(paste0('**********:', col))
    print('##########:MEAN')
    print(aggregate(pima[col], list(diabetes = pima$pregnant), mean, na.rm = T))
    print('##########:SD')
    print(aggregate(pima[col], list(diabetes = pima$pregnant), sd, na.rm = T))
}