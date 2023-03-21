<h1 align="center">FaceCheck</h1>
<p align="center"><i>A WebApp to make fetching user information using facial recognition</i></p>
<p align="center"><i>A small scale prototype for identifying specific individuals</i></p><br>

- Submission category: Artificial Intelligence/Facial Recognition Technology(FRT)

## What this is, and what we envision
-  FaceCheck is a prototype WebApp to identify as well as collect information about specific individuals.
-  The WebApp allows authorities to keep track of an individual's information very easily and with minimal amount of setup. 
-  This prototype has a potential to scale on very large levels as well as can be used on a small scale. 
-  One may beg the question, "Why not use biometrics?". The answer to that question is quite simple: It's highly cheap and can be implemented on a large scale. Biometrics need special iot devices, but FaceCheck can work on relatively low cost cameras such as monitoring cameras, traffic cams, etc. It is also integrated with a postgresql server which holds the information of all the users that are registered. Once identified, the WebApp provides all the details of that individual. If not, it will prompt you to register stating that the individual is not identified.

## How does one set this up?
- For the authority/managing team, they would simply need to clone this project and install the requirements.
 `git clone https://github.com/laughingclouds/raj-it-day-hackathon.git`<br>
 <i>It is recommended to work in a virtual environment</i><br>
 `pip install -r requirements.txt`
- Additonally, the managing team will also need a postgresql database to store information regarding users<br>
> <i>NOTE: The backend setup is highly respective to the prototype we've built. Changes can and should be made according to the scale of use</i><br>
> <i><b>Another thing to note is that the face-recognition module requires certain tools to be installed before you install the module itself. Refer: https://stackoverflow.com/a/70044454 for a quick understanding on how to properly setup face-recognition</i></b>
- For a user, to get registered into the connected database, and for the WebApp to start identifying you, all they have to do is fill up their personal information and add 5 photos of themselves.<br>
> <i>NOTE: The model can identify faces using just 1 photo (yes, it is that good). However, it can sometimes be possible that certain light variations in a photograph can hide facial features for the model to recognize. Hence 5 photos ensure that the facial features are recorded properly.<i>

## What is the underlying tech?
- We are using a pre-trained module called "face-recognition". It is built upon a state of the art Dlib face recognition model. 
- It extracts the features of a face such as the outlines of each person’s eyes, nose, mouth and chin.
- In detail, the Dlib library mainly uses two algorithms to detect a face:
  - A HOG + Linear SVM face detector that is accurate and computationally efficient.
  - A Max-Margin (MMOD) CNN face detector that is both highly accurate and very robust, capable of detecting faces from varying viewing angles, lighting conditions, and occlusion.
- The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark.
![image](https://user-images.githubusercontent.com/57110219/226485855-18e6b79e-560d-41e0-9257-be07db52fcb0.png)

## Where can this be used?
The FaceCheck prototype can be scaled for variety of different uses. 
- One of the most basic and a small scale use of this is in reception settings/help desk for a school or a university. Students are registered in a database along with their facial features and a monitoring camera can be used to detect the students coming up to the desk. This saves a lot of time and effort for a receptionist to fetch details
- The above use case can also be used similarly in monitoring classes/exam centres. The camera can give a live feed of students in a class along with their respective details. This again eliminates the need to query each student for their details.
- One of the large scale use case could be monitoring prison cells. This additonal layer of identification can help improve security and attendance in a prison
- Yet another large scale use of this prototype could be implemented in a citizen identification method. In india for example, a database similar to aadhar, or the database used for aadhar itself can be used to keep a track of all citizens of the country. Traffic cams and public monitoring cams can then be used to improve the security of the country.

## Limitations of this prototype/What can further be done?
It is not yet close to perfection. There are yet things that can be improved and made better.
- The current prototype of FaceCheck doesn't use a live video feed for detection of an individual. A photo has to be uploaded. This can certainly be upgraded to a live feed and detection but due to limitation of time, a photo upload method is used. The underlying detection method remains the same.
- The prototype is based a very small scale system. This can certainly be improved with right amount of funding and time spent. 
- Separate servers for database/frontend/backend can be implemented for a clean flow of data.
- Additional security measures can be provided so the information regarding individuals cannot be leaked.
- Initial photos required to register a user can be changed to a more robust and on-site method to collect data (Eg:Live video feed)


  - ### Screenshots
  <img src = "https://user-images.githubusercontent.com/69053040/226495371-05a7288b-3041-4535-adbd-605e138e35a3.png" width="550" height="350"/>
  <img src = "https://user-images.githubusercontent.com/69053040/226495391-42fb536d-0265-477b-9f41-9025015357bf.png" width="700" height="550"/>
  <img src = "https://user-images.githubusercontent.com/69053040/226495407-1ea795e9-db32-4cf9-a147-c89d568a2094.png" width="350" height="550"/>



## References
  - [Face recognition model](https://github.com/ageitgey/face_recognition)
  - [Dlib](https://pyimagesearch.com/2021/04/19/face-detection-with-dlib-hog-and-cnn/)
  - Project name inspired by: [FaceCheck (PS: Not particularly useful information)](https://support.overwolf.com/en/support/solutions/articles/9000179585-what-is-facecheck-)

## Team members
- **Aaryan Tyagi**
  - Github Profile: [4RCAN3](https://github.com/4RCAN3)
  - Linkedin Profile: [Aaryan Tyagi](https://www.linkedin.com/in/aaryan-tyagi-arc4n3/)
  
- **Hemant Bhandari**
  - Twitter Profile: [NeemeshYadav](https://twitter.com/NeemeshYadav)
  - Github Profile: [Stealth-py](https://github.com/Stealth-py)
  - Linkedin Profile: [Neemesh Yadav](https://www.linkedin.com/in/neemeshyadav/)
 
- **Aditya Singh**
  - Twitter Profile: [BlazeSama007](https://twitter.com/BlazeSama007)
  - Github Profile: [BlaZeSama](https://github.com/BlaZeSama)
  - Linkedin Profile: [Aditya Singh](https://www.linkedin.com/in/aditya-singh-a43471193/)
