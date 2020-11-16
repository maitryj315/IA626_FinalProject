---
title: "covid"
author: "Jeenat Maitry"
date: "November 16, 2020"
output: html_document
---

```{r}
library(ggplot2)
mydata<- read.csv("rate_vs_distance.csv", header = TRUE)

ggplot(data=mydata, aes(x=Distance_From_NYC, y=Infection_Rate, fill=County))+theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank(), axis.line = element_line(colour = "black"))+ geom_point()+ theme(legend.position="none")

```

