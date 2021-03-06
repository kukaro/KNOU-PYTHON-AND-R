pima <- read.csv('./data/pima2.csv', header = T)
par(mfrow = c(2, 1))
cols <- c('glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age')
by(pima[cols], pima$diabetes, summary)
for (col in cols) {
    boxplot(get(col) ~ diabetes, data = pima, main = paste0(col, ' boxplot'), col = 2:3)
    hist_pos <- hist(pima[[col]][pima$diabetes == 'pos'], plot = F)
    hist_neg <- hist(pima[[col]][pima$diabetes == 'neg'], plot = F)
    plot(hist_pos,
         col = adjustcolor("red", alpha = 0.5),
         ann = FALSE,
         ylim = c(0, max(hist_pos$counts, hist_neg$counts)))
    plot(hist_neg,
         col = adjustcolor("blue", alpha = 0.5),
         add = TRUE,
         ylim = c(0, max(hist_pos$counts, hist_neg$counts)))
    title(main = paste0(col, ' histogram'))
}
