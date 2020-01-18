//-------------------------------------------------
// source code reference: https://github.com/SUYEgit/Surgery-Robot-Detection-Segmentation
// procedure reference: https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46
//-----------------------------------------------------

//--- Setup python dependencies
// Open windows command line in directory of src/, and run the following commands

pip install -r requirements.txt

python setup.py install


//--- Labeling by VIA tool
// Reference: http://www.robots.ox.ac.uk/~vgg/software/via/docs/creating_annotations.html
// Download VIA tool: http://www.robots.ox.ac.uk/~vgg/software/via/

Open via.html

// 1: Selecting local files using browser's file selector
Project → Add local files -> Select all image files -> Open

// 2. Define Attributes
click the Attributes panel in left sidebar and then click Region Attributes
->
Enter "name" in the attribute name textbox and click button to add this attribute (Type: text)

// 3. Labeling
Region Shape: choose "Polygon region shape" 
-> 
start labeling
->
click polygon region after labeling, and input "name" (ex. pill1, pill2...)

// 4. Save annotation to json file
Menu: Annotation 
->
Export Annotation (as json) 
->
put json file in the image directory (ex. data/pill/train/) 

