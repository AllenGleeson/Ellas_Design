# Ellas Design

Ellas Design is a full stack Django web app to sell clothing from Ella Moya. The user can browse the products and add them to cart where they can checkout and pay using Stripe Payments. They can also create a profile to store their delivery information and see their order history. The owner will be able to add, edit and delete products.

I made the website for someone I know so I had extra motivation but the goal was to use the django framework and ultimately for the designer to be able to sell her products. I also use JS and Jquery . The site is a series of Django apps with their own js and css.

Here is a link to the published site on Heroku: https://ella-moya.herokuapp.com/

## UX

### Strategy

My goal for this website was to create a place for a fashion designer to sell their designs and clothing based on what the designer wanted. For this she would need to be able to create, edit and delete products and also create additional categories. She would also need those products displayed nicely to the user and with a way to purchase them so there will be a payment system. I also wanted a way for the user to sign in to save their delivery information and also see their order history. I will make her easy to contact her so their will be a contact page to send emails and social media links visible on the footer of the site. Also an about page for more information about the designer. While I want the user to have a profile I only want it just be a benefit to them so making a purchase on the site wont require you to be logged in.


#### User Stories

- A User looking for some clothes to buy:
Arrives on home page.
Directed to the Shop with a button.
At the Shop the user can browse the products and choose different categories.
Clicking on a product with bring the user to that products page.
On the products page the user can increase or decrease the quantity and then click add to cart which will update the shopping bag.
When the user has added what they would like to their bag they can click on the bag to bring to the Bag page.
On the Bag page the user can change quantity for each product and remove the product from the bag if they wish.
When the user is ready they can click Proceed to Checkout to go to the Checkout page or click Keep Shopping to go back to the products page.
On the Checkout page the user will see their bag and will need to enter their shipping and card details.
When complete they can click Checkout and the payment will be confirmed and a confirmation email sent to the users email.
The user will then be taken to checkout succes where they can see their order information and then continue to browse products.

- A User Creating a Profile:
If the user wants to save their delivery information and see their order history they can click on the profile icon.
When clicked they can Login, Logout and Register for a new profile.
Clicking register will bring to account signup where the user will be asked for a username and password. On create they will get a confirmation email.
Clicking login the user will be able to log in with their username and password and their username will be displayed beside the Profile icon.
Clicking logout the user will be brought to sign out where they will be asked if they are sure they want to sign out. If yes then they will be brought sign out and be brought to the Home page.

- A User using their Profile:
When logged in the user has access to their Profile where delivery information and order history is stored.
Clicking the Profile icon will display Profile and Log Out.
Clicking Profile will bring to the Profile page.
On the Profile page the user can see their deilvery information and update it if they wish. They can also see previous orders made.
Clicking logout the user will be brought to sign out where they will be asked if they are sure they want to sign out. If yes then they will be signed out and be brought to the Home page.
If a user is logged in then when they go to the Checkout page with products in their bag they will have their shipping details prefilled from their information. Their order will also be saved to their profile upon payment.

- A Admin using their Profile:
Along with other user functionality the Admin will be able to create, edit and delete Products.
Clicking the Profile icon will display Product, Management, Profile and Log Out.
Clicking Profile will bring to the Profile page.
Clicking logout the Admin will be brought to sign out where they will be asked if they are sure they want to sign out. If yes then they will be signed out and be brought to the Home page.
Clicking Product Management will bring the Admin to the Product Management Page.
From here the admin can create new Products and Categories as well as see how many products they have and how many orders have been made.

Clicking on Create a Product will bring the Admin to the Create Product page.
Here the Admin can add information about the product such as name, description, image, price etc.
Clicking Create will create that new product and save it to the database.
The Admin will then be brought to that Products page.

If the Admin visits any of the products pages and they will be able to see an Edit and Delete Button.
Clicking Edit will bring the Admin to the Edit page for that product.
Here the Admin can edit information about the product such as name, description, an image, price etc.
Clicking Save the product will be changed and saved to the database and the Admin will be brought back to the Products page.

Clicking Delete will show an Alert Box asking if the Admin is sure. If Yes the product will be deleted from the database.

### Scope

To achieve my goal I need the following:

#### Functional Requirements
    1. The site will need 6 apps
    2. Django Allauth to handle logins.
    3. Stripe Payments to handle Payments.
    4. Navigation that is easy to use.
    5. A database to store all site data
    6. AWS S3 to store Images
    7. A Bag app to store products the user wants to purchase.
    8. A Checkout where Stripe payments will be used.
    9. Confirmation emails when the user makes a purchase.
    10. A way to contact the site owner through the Contact page
    11. A Profile to display the users delivery information and order history

#### Non-Functional Requirements
    1. The website will be clear to use
    2. Give useful information to the user
    3. Responsive Design


#### Content Requirements
    1. Cards to display the products
    2. Forms for creating and editing products
    3. Forms for a profiles delivery information
    4. A home background image and logo, provided by Ella Moya

### Structure

The goal of the website if for users to be able to browse the website and choose products to purchace and to also allow the owner to create, edit and delete products.
Also for the user to create a profile that can show them their order history and save their delivery information if they wish.
It will consist of 7 main apps: Home, About, Contact, Shop, Bag, Checkout and Profiles.

#### Navigation -
    Shop - The shop page will display all the products and give the option of different categories to search by.
    About - The about page gives a brief description of the designer and links to their social media.
    Contact - Contact page will allow a user to send the designer a comment. Wether that be just a message or a issue they have with the site or a purchase.

    Profile - on click displays Log In/Log Out and Register(For Users) and also Product Management(for the site owner).
    Bag - on click brings to the bag page and display the bag contents to the user where they can change the quantity, remove the product or proceed to checkout.

#### Home -
    The Home page will have a background image with a message directing the user to the shop and a Shop Now button.

#### About -
    The About page will be show a description of the designer with some other information about them and their social media link.

#### Contact -
    From here the user can enter a subject, email and comment and send it to the designer for feedback or issues with their payment.

#### Shop -
    The Shop page will display all the products in cards which an image, name, catagory and price. From here the user can select the catagory to display and click on a product that interests them.
    Clicking on that product will display that products details to the user. From here they can increase and decrease the quantity and then add that item to their shopping bag.
    The Admin will be able to edit and delete products from here.

#### Bag -
    The bag will store any products the user added to their bag and give the option to change the quantity or remove the item from their bag before proceeding to checkout.

#### Checkout -
    Checkout displays a form for the user to enter their delivery and payment information. It also displays what is currently in their bag.
    When the user wants to checkout it uses Stripes Payment system to confirm the payment and sends a confirmation email to the user.

#### Profiles -
    The profiles app deals with storing the users previous orders and delivery information. A profile is not required to be back to make a purchase. The user can update their delivery information from their profile.
    
### Skeleton

I created some wireframes for the website which are in this repository:
https://github.com/AllenGleeson/Ellas_Design/blob/master/site_info/wireframes

### Surface

The look for the website was based partially on the designers vision for the site and my own research into other fashion designers website and also big websites like amazon for how they do their shopping bag and checkout. The color is a pink the designer chose with white text. I used this throughout for any buttons on the main content of the site while keeping the other text a simple black with white background. The font was chosen as I wanted something that might look like it was written with a pen.

## Features

- Bootstrap 5: I user their cards and grid system
https://blog.getbootstrap.com/

- A Shop
- Shopping Bag
- Checkout

## Technologies Used

This project used Django, Bootstrap 5, HTML5 & CSS3, JS, Jquery, Python3, PostgresSQL.
Github is used for version control and the website is hosted on Heroku.

Django Framework:
https://www.djangoproject.com/

Bootstrap 5:
https://blog.getbootstrap.com/

Stripe Payments is used for payments:
https://stripe.com/ie

Amazon S3 used for image storage:
https://aws.amazon.com/s3/

Heroku for hosting:
https://dashboard.heroku.com/


### My database:
https://github.com/AllenGleeson/Ellas_Design/blob/master/site_info/database_schema/models-graphs.png

## Testing

Testing was done with Chrome DevTools and Visual Studio Codes debug mode to create breakpoints to view what I was changing and to test.
The project was tested in different screen sizes and will be mobile friendly with help from Bootstrap 5.

Below I have some manual testing done through the site:
https://github.com/AllenGleeson/Ellas_Design/blob/master/site_info/testing

## Deployment

I added all my code and images to github and then deployed my project through Heroku.
Going to Heroku and creating a new Heroku App with the projects name. Then connecting the app to the code on github and doing a
manual deploy, ensuring to have the Procile and requirements.txt required to run the project on Heroku.
https://devcenter.heroku.com/articles/github-integration

Site is published at: https://ella-moya.herokuapp.com/

### Content

- There is an image for the background of the Home Page and there is a logo. Other images like products are stored on Amazon S3. Products and stored in the database.

### Media

Media will be added by the site owner when adding new products.

### Future Additions

The ability for the user to be able to log in with other social media accounts like instagram etc. I also may add sorting for the products page but it isn't urgent for the client as there aren't an enormous amount of products at this time. A possible feature is to add reviews for the products. This would be simple enough to do.

### Credits

Credit to Code Institute for the help throughout and to their Boutique website for reference and inspiration.
https://github.com/ckz8780/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218


### Acknowledgements

A big thanks also to my mentor through these projects. He was a big help. Reuben Farrente