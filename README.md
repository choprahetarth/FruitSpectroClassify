# FruitSpectroClassify
# Code repository for the Engineering Final Year Project. 
Ever since the inception of modern technologies such as IoT and AI/ML, the technologies have been proved to be very helpful in development of industries. One such use case has been carefully studied, and a solution has been provided in this literature. Sorting of fruits is a big task within the agricultural sector, and this task has been realized in an innovate way with the help of IoT and ML. This literature provides the design and development of a machine and an algorithm, capable of segregating fruits based on their ripeness level using MEMS Spectroscopy sensor and computer vision systems. The fruit is initially fed into the system where the Raspberry Pi Camera takes its image. The image processing is done using a cloud-computing platform known as customvision.ai, which has been provided by Microsoft Azure Cloud Services, hence incorporating a sense of IoT within the total framework. The platform has been trained specifically to predict apples with a maximum accuracy of 99%, and in general other fruits with an average accuracy of 83%. After that is done, three readings are taken by the Sparkfun Triad Spectroscopy Sensor, where an ensemble of custom trained XGBoost Machine Learning model was used to classify the fruit according it's ripeness level, with the level of Soluble Sugar Content (SSC) into three specific categories, unripe, mediocre ripe and perfectly ripe. This model was trained using 3660 apple readings taken from Unitec's Apple Sorting and Grading Machine from an industrial plant in Shimla. The model was trained with the help of Python 3.7 and an open source software - H2O’s Driverless.Ai. With the help of this software, the accuracy of the baseline model trained on python was increased by ~1%, it also increased the AUC (Area Under ROC) score by ~24%, F1 score by ~27%, Gini Score by ~50% and decreased the LOGLOSS by ~12%. The overall accuracy of classifying the fruit into different ripeness level classes was scored at approximately 80% (RMSEP – 0.23). The project also provides a Python Graphical User Interface (GUI), made on PyQt5, for integration of the hardware with the cloud-based software to realize a complete solution

### Tech

Dillinger uses a number of open source projects to work properly:

* [Python] - HTML enhanced for web apps!
* [Jupyter Notebook] - awesome web-based text editor
* [Scikit-Learn] - Markdown parser done right. Fast and easy to extend.
* [H20.ai Driverless AI] - great UI boilerplate for modern web apps
* [Raspberry Pi] - evented I/O for the backend
* [Arduino] - fast node.js network app framework [@tjholowaychuk]
* [PyQT5] - the streaming build system
* [Microsoft Azure CustomVision.Ai](https://breakdance.github.io/breakdance/) - HTML to Markdown converter
