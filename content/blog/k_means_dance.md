---
date:  "2019-05-07"
publishdate: "2019-05-07"
draft: false
title: "Dancing the K-Means Dance"
tags: ['ds-education']
series: ['Education']
categories: ['English']
img: '/images/blog/2019-05/k_means.png'
toc: true
---

Dancing can be traced back to the origins of almost every society in the world. It is a way to communicate ideas and feelings in a free manner. It also is a simple, memorable and effective way to communicate from kids to seniors. We wondered whether we could use dance to facilitate student learning and retention of a Machine Learning algorithm in an introductory data science course. For this activity we wanted to involve students
to be part of the process of the algorithm. To do this we used interpreative dance as part of active learning, which has been shown that helps improve the students' perception of the learning material (Detlor et.al. 2012) and performance (Anderson et. al. 2005). (For a more complete treatment of resources on Active Learning look at:
https://www.queensu.ca/activelearningspaces/active-learning/benefits-active-learning)

For this lecture in particular, we wanted to showcase how the K-Means clustering algorithm works, from initialization to convergence. K-means is an algorithm that tries to find sub-groups within data sets in an unsupervised manner. It uses the similarity and disimilarity of the observations in order to group them without the use of class labels. It starts by choosing K random points from the data that will act as the centers of the clusters (aka centroids) we are looking for. We then look at the closest points to these centroids and say they belong to the same cluster. After this we calculate the new center of each cluster and reassign them to be the cluster centers. We keep doing this process until the centroids no longer change their position from one iteration to the other. 

To do this in the classroom we had the students act as data points and the Teaching Assistant's (TA's) as centroids. To start the activity we gave the students 3 different coloured sticky notes matching the TA' shirt colours. Then the TA's randomly positioned themselves in the classroom and the students discussed which TA was closer to them. Based on this, they assigned themselves the labels of the cluster to which they decided they belong by raising the sticky note of the corresponding colour to match the centroid colour. Once all of the students had assigned themselves,
the TA's moved to the center of the new clusters. We repeated the process until the
students agreed that the algorithm had converged (that the TA's didn't had to move more).

We received postitive feedback from the students that this class activity helped them learn and remember the K-means algorithm. One of the limitations to this class activity that we observed was that the algorithm converges very quickly given the students engagement and attention to detail.

All educators, including Data science educators, should be looking to acquire new teaching techniques that are engaging to help students learn complex concepts. We believe that interpretive dance is a great tool for the data science educator's toolbox for teaching the K-means, and potentially, other algorithm(s). 

> I want to thank Dr. Tiffany Timbers for her role as the Instructor in this course, for giving me the opportunity to work in this course as an Academic Assistant and a Teaching Assistant, and for her help in editing this blog post which contributions helped me improve it.