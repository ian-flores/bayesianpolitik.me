---
date:   "2018-10-16"
publishdate: "2018-10-16"
draft: false
title: "How was mortality distributed through Puerto Rico after Hurricane Maria?"
tags: ['puerto_rico', 'bayesian_stats', 'mortality', 'demographics', 'tr-blog']
series: ['Social Data Analysis']
categories: ['English']
img: '/images/blog/2018-10/puerto_rico_death_choropleth.png'
toc: true
---

### Context

<hr>
Hurricane Maria struck Puerto Rico the 20th of September of 2017 at 6:15 a.m. entering through the municipality of Yabucoa as a Category 4 hurricane. According to the governments of Puerto Rico and the U.S. Virgin islands, the cost of the damage is estimated in $102 billion USD[1](https://www.wunderground.com/cat6/hurricane-maria-damages-102-billion-surpassed-only-katrina). However, the impact wasn't only economical. Following a lawsuit presented by the Center for Investigative Journalism (CPI, by its spanish initials) and CNN, the Government of Puerto Rico, and more specifically the Demographic Registry, was forced to publish the individual-level data of all the fatalities occurred from September 20, 2017 to June 11, 2018.

With access to this data we focused on answering two main questions.

-   Which municipalities in Puerto Rico should prioritize their emergency response plan revision to prevent fatalities in case of future natural disasters?
-   Which type of municipal zone, urban or rural, had higher mortality rates?

This questions enable us with actionable insight to maximize aid and minimize the loss of life for future natural disasters.

### The Data

<hr>
As previously mentioned, the main data source was the individual-level data of all the deaths in the island after the hurricane. It is worth noting that this dataset contains data that it's not confidential, but very sensitive as it contains all identifiable data such as names and addresses. I also used the 2017 Annual Estimates of the Resident Population from the United States Census Bureau to get the population estimates per municipality in 2017.

### The Analysis

<hr>

To answer the first of our questions **Which municipalities in Puerto Rico should prioritize their emergency response plan revision to prevent fatalities in case of future natural disasters?** , I decided that it was better to first standarize the data to be on a comparable scale and then visualize it to see if there were spatial patterns. I did this by calculating the mortality rate for each municipality and overlaying this over a map of Puerto Rico.

![](https://raw.githubusercontent.com/ian-flores/Hurricane_Maria_Mortality_Analysis/master/analysis/figs/puerto_rico_death_choropleth.png)

This maps highlights the top ten municipalities with the highest mortality rate. We see a spatial cluster of municipalities in the mountainous/central region of the island. We can observe as well that municipalities that are on the west coast of the island have a lower mortality rate than the other municipalities, this might be because they were the farthest from the Hurricane, but there might be other public policy possibilites as to why that is.

Moving on to the second question, **Which type of municipal zone, urban or rural, had higher mortality rates?** I wanted to compare the mortality rate in urban areas with the mortality rate in rural areas, see if it was significant, but allow for a greater variability as a urban area in the north part of the island is not very similar to an urban area in the central part of the island. Given this reasons, I opted to estimate the mortality rate in urban and rural areas and compare this estimates. It is worth noting that the categories of rural and urban are assigned by the Department of Health of Puerto Rico.

![](https://raw.githubusercontent.com/ian-flores/Hurricane_Maria_Mortality_Analysis/master/analysis/figs/difference_of_means.png)

This estimates yielded an average mean of 1.98 with a confidence interval of 1.55 and 2.41. What this means is that on average 2 more persons died in rural areas than in urban areas. However, which rural areas might need more focus after another natural disaster? In the table below I present the top 5 municipalities with the higher rural mortality rates.

| Municipality  | Zone  |  Number of Deaths|  Population (2017)|  Mortality Rate per 1000 individuals|
|:--------------|:------|-----------------:|------------------:|------------------------------------:|
| GUANICA       | RURAL |               111|              16363|                             6.783597|
| SAN SEBASTIAN | RURAL |               242|              37306|                             6.486892|
| VIEQUES       | RURAL |                55|               8669|                             6.344446|
| LARES         | RURAL |               162|              25772|                             6.285892|
| AGUADILLA     | RURAL |               320|              53164|                             6.019111|

If we are to focus on the urban areas, this would be the top 5 municipalities with the higher urban mortality rates:

| Municipality | Zone   |  Number of Deaths|  Population (2017)|  Mortality Rate per 1000 individuals|
|:-------------|:-------|-----------------:|------------------:|------------------------------------:|
| SAN JUAN     | URBANO |              2531|             337288|                             7.503973|
| BAYAMON      | URBANO |              1174|             179565|                             6.538022|
| PONCE        | URBANO |               919|             140859|                             6.524255|
| CATANO       | URBANO |               150|              24374|                             6.154099|
| CAROLINA     | URBANO |               866|             154489|                             5.605577|

However, on an island with a limited budget and a complex public health system segregating between rural and urban areas might not be the most important factor in determining where to impact. With this last table, we can visualize the top 5 zones in the island with the highest mortality rates.

| Municipality  | Zone   |  Number of Deaths|  Population (2017)|  Mortality Rate per 1000 individuals|
|:--------------|:-------|-----------------:|------------------:|------------------------------------:|
| SAN JUAN      | URBANO |              2531|             337288|                             7.503973|
| GUANICA       | RURAL  |               111|              16363|                             6.783597|
| BAYAMON       | URBANO |              1174|             179565|                             6.538022|
| PONCE         | URBANO |               919|             140859|                             6.524255|
| SAN SEBASTIAN | RURAL  |               242|              37306|                             6.486892|

### Conclusion

<hr>
In a context of climate change and a worsening economic crisis, Puerto Rico's organizations (Government and NGO's) need to improve their preparedness and their plans of action to fit the economic and infrastructure constrains present to be able to effectively save lives and maximize aid. There's been a lot of talk as to how the organizations should act upon on times of crisis, however, without data from previous disasters we are merely speculating as to which processes happened and how they happened. This analyses shows that more focus needs to be turned into the rural areas of the island as those are the ones with a higher mortality rate. Not only this, but remote and hard-to-access locations such as the mountainous region need to be aided with greater efficency as this ones as well suffered higher mortality rates.

### References

1.  <https://www.wunderground.com/cat6/hurricane-maria-damages-102-billion-surpassed-only-katrina>

### License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

> The GitHub repository of the analysis hereby presented is available at: <https://github.com/ian-flores/Hurricane_Maria_Mortality_Analysis>