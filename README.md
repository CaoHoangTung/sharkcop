# Sharkcop - A machine learning tool to detech phishing URLs

Sharkcop has 2 main parts:
1. **Sharkcop-server**: A flask webserver which provide a restful api to fetch an url's information
2. **Sharkcop-extension**: A Chrome extension which interact with sharkcop-server to detech phishing URLs on Facebook and Messenger

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

```
Python 3 >
```

### Installing
Clone the repository
```
git clone https://github.com/CaoHoangTung/sharkcop
```

Install the required packages
```
pip3 install –r requirements.txt
```


**1. Install sharkcop-server on your local machine**

At the project root directory, run
```
cd sharkcop-server
```
```
python3 app.py
```

![Server is up and running](/readme/2.png)

The server will be up at 127.0.0.1:8080. 
The RESTful API endpoint would be in this format:
```
http://127.0.0.1:8080/api/check?url=https://abc.xyz
```

You can test the api through a web interface at http://127.0.0.1:8080

There are 3 statuses that could be returned:
-  1 : The url is phishing
- -1 : The url is normal
-  2 : Cannot fetch the url's information (May be dued to refusal of connection or server error)

![The test webserver](/readme/4.png)
**2. Setup sharkcop-extension (for Chrome)**

  - Open Chrome Extension Manager (chrome://extensions/)
  - Enable Developer Mode
  - Click 'Load unpacked' and select the directory **'sharkcop-extension'** inside our project root directory
  - Try it on facebook
  
## Built With

* Python
* Javascript

## Techniques

* We use Machine Learning to detect Phishing Website, specifically SVM (Support Vector Machine) which is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data, the algorithm outputs an optimal hyperplane which categorizes new examples.

## Authors

* **proxyht** - caohoangtung2001@gmail.com
* **ngocanhnckh** - ngocanhnckh@gmail.com
* **aidenpearce** - aidenpearcewd01@gmail.com

## Notes

* The project is still under construction and requires a lot of optimization.
* Any suggestions or help would be very appreciated
