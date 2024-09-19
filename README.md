## Artist Website

### **A single-page multimedia art portfolio website featuring an interactive fluid simulation and an extensive editing page so that the artist may customize the theme of the site directly via the admin page.**


## Of Note:

* This is a real world project and I will continue working with the artist after my submission to make further refinements.

* The artist is still preparing documentation and statements about their work. The site is currently populated with some example entries.

* The artist is a fluent Python programmer and prefers to edit works within the seed.py file directly. The admin page is dedicated to CRUD operations related to the visual presentation of the site.

* For the convenience of the reviewer, a function has been added within app.py that logs the visitor in as an admin so that the editing page may be viewed. 

## Imgs
#####Individual Work
![](static/readmeImgs/readme1.png "Site")
#####Edit Page
![](static/readmeImgs/readme4.png "Site")
#####Site After Edit
![](static/readmeImgs/readme2.png "Site")



## Website Features:

* Single page site that dynamically loads different windows without redirects via Javascript.

* Seperate sections for individual artworks, performances, and an about page with bio and links to relevant external.

* An interactive fluid simulator implemented in the background of the site. 

* An admin editing page with authenticated credentials via Bcrypt. 

* Embedded audio works via Soundcloud Api


##Future Improvements:

* Currently reworking fluid simulator code for more efficient CPU usage which is currently quite high.

* The CSS code is in need of additional refactoring as I decided to not rely on certain Bootstrap features mid-project.

* The elements within the page do not resize especially well at the moment. There may be additional elements added in the future so I'm not 100% on the css relationships currently.

* I was having some difficulty communicating between Javascript and Flask via Wtforms so some JS code is written within CSS files which isn't ideal.


##  Built With:

* Python
	* Flask  
	* BCrypt  
	* SQLAlchemy  
	* Wtforms	
* Javascript, CSS, HTML  
	* Bootstrap	
* SQL via PostgreSQL



##Fluid Simulator Source Code:
* The fluid simulator is a modification of the script found here: 
	* https://codepen.io/aecend/pen/WbONyK