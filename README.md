# Project 5 - La Selle 
![Readme banner - device screens](readme_images/readme_banner.png)

La Selle is a fictitious bicycle saddle E-Commerce site created using the Django Framework and numerous other packages, libraries, modules and external tooling.
### View the site - [La Selle](https://la-selle-45cacae9f212.herokuapp.com/)
<br>

 * [Table of Contents](#table-of-contents)
 * [User Experience (UX)](#user-experience-ux)
    + [Initial Discussion](#initial-discussion)
    + [User Stories](#user-stories)
 * [Design](#design)
 * [Wireframes](#wireframes)
 * [Database Schema](#database-schema)
 * [Color Palette](#color-palette)
 * [Typography](#typography)
 * [Features By Page](#features-by-page)
    + [Home page](#home-page)
    + [Products](#products)
    + [Product details](#product-details)
    + [Cart](#cart)
    + [Checkout](#checkout)
    + [Stripe Webhooks](#stripe-webhooks)
    + [Accounts](#accounts)
    + [Profiles](#profiles)
    + [Emails](#emails)
    + [Defensive Design](#defensive-design)
    + [Future Implentations](#future-implentations)
 * [Technologies Used](#technologies-used)
    + [Languages & Packages Used ](#languages-packages-used)
 * [Database tools](#database-tools)
    + [Programs Used](#programs-used)
 * [Deployment and Local Development](#deployment-and-local-development)
 * [Testing](#testing)
 * [marketing ](#marketing)
    + [Strategic Partnerships:](#strategic-partnerships)
    + [Community Engagement:](#community-engagement)
    + [User-Generated Content:](#user-generated-content)
    + [Interactive Content:](#interactive-content)
    + [Customer Reviews and Testimonials:](#customer-reviews-and-testimonials)
    + [Localized Marketing:](#localized-marketing)
    + [Influencer Marketing:](#influencer-marketing)
    + [Sustainability and Innovation:](#sustainability-and-innovation)
    + [Limited Editions and Special Releases:](#limited-editions-and-special-releases)
    + [Educational Content:](#educational-content)
    + [B2B Distributor and Supplier Engagement:](#b2b-distributor-and-supplier-engagement)
    + [Mailing list](#mailing-list)
    + [Mockup Facebook page](#mockup-facebook-page)
    + [Marketing synopsis ](#marketing-synopsis)
 * [credits](#credits)
    + [Content](#content)
 * [Media](#media)
 * [Acknowledgments](#acknowledgments)

## User Experience (UX)
### Initial Discussion
La Selle was created to accelerate product sales and create greater branding exposure for the saddle manufacturer "La Selle".  


### User Stories
A full list of user stories with documentation outlining the user stories and their respective storyboard can be found [here.](https://github.com/users/DavidUWL/projects/2/views/1?layout=table&pane=info) 
<br>
If the project README does not open, it can be accessed via the button below. 
<br>
![README button location](readme_images/story_board.png) 


## Design
Market research on other competitors in this domain has led me to a consistent color scheme/design that has roots in the product itself. A simple slightly rounded black and white page allows the products to be the centerpiece for catching the eye. As the products do not contain colour or straight corners, including either of these in the design would make the UX slightly jarring when moving across multiple products. Small uses of straight corners or colour allows the user to be strongly guided through the order and purchasing process. 

## Wireframes

<details>
  <summary>
  Click to expand homepage.
  </summary>
  
  * The homepage contains two main CTA's, including the discount banner and the button below the pages body tagline to view all products in the store. It will also contain functional elements like a navigation bar, and its associated search bar. All subsequent pages hereafter are extensions of this page minus the the body tagline and background image. 

![Home Page Wireframe](readme_images/wireframes/homepage.png) 
</details> 
<details>
  <summary>
  Click to expand all products page.
  </summary>

  * The all products page will render all products in the database and print their associated categories/ratings/price below. There will be a functional sort by element to sort the products by their dimensions. A back to top button will be in the bottom right which will bring the user back to the top of the page. 

![all products Wireframe](readme_images/wireframes/multi_products.png)
</details> 
<details>
  <summary>
  Click to expand product details page.
  </summary>
  
  * The product details page will contain the same product elements as the all products page, but include a description below, with a ratings section and size/quantity selectors. A simple CTA "buy" button will be below this. 

![product details Wireframe](readme_images/wireframes/product_details_page.png)
</details>
<details>
  <summary>
  Click to expand offcanvas sidebar cart.
  </summary>
  
  * If the shopping cart button is clicked, it will open an offcanvas element containing all the elements added to the cart during the users session. This will provide better UX for the customer instead of constant popups on the screen which may be distracting. A "checkout" CTA will be present. 

![cart offcanvas Wireframe](readme_images/wireframes/offcanvas_sidebar.png)
</details>
<details>
  <summary>
  Click to expand checkout cart page.
  </summary>
  
  * Similiar to the offcanvas shopping cart, all items in the user session will be rendered, with a second quantity selector and item prices. Below will be delivery/total/grand total. Two buttons below will take the user back to the products page, or continue to the checkout.  

![checkout cart Wireframe](readme_images/wireframes/checkout_cart.png)
</details>
<details>
  <summary>
  Click to expand checkout delivery and payment page.
  </summary>
  
  * The checkout will contain a form to submit the users shipping information, with a second render of the products added to the cart and the totals ect. Below will be a stripe payment section and a payment confirmation button.  

![checkout delivery Wireframe](readme_images/wireframes/checkout_delivery_payment.png)
</details>
<details>
  <summary>
  Click to expand checkout success page.
  </summary>
  
  * The checkout success page will render two tables, containing the confirmed order and the delivery details. 

![checkout success Wireframe](readme_images/wireframes/checkout_success.png)
</details>
<details>
  <summary>
  Click to expand the user profile page.
  </summary>
  
   * The user profile will contain a form that allows the user to update or delete their shipping details, view their previous orders/ratings/product wishlist. 

![user profile Wireframe](readme_images/wireframes/my_profile.png)
</details>


## Database Schema 
A relational database was used for this project as it would best suit the needs of site. The schema below was created using [DbVisualiser.](https://www.dbvis.com/) <br>
_For more information on the User table/objects please refer to the_ [AllAuth Documentation.](https://docs.allauth.org/en/latest/index.html)
<br>
<details>
  <summary>
  Click to expand database schema.
  </summary>

![A database schema](readme_images/schema/schema_pk_only.svg)
_For a high res full table schema_ [click here](readme_images/schema/full_tables.svg)
</details>


## Color Palette 
![Color Palette](readme_images/site-palette.svg)
* The color palette for this project was created to be quite minimalist and match the tones of the products being sold. A mix of bootstraps built in class colours were used lightly across elements to give them some extra pop on the page, however - generally, colour was kept to a minimum. 

## Typography 
The
[Orbitron](https://fonts.google.com/specimen/Orbitron?query=orbitron)
Google Font was used for the logo text in this project, suiting the minimalist design with its mixture of straight and rounded edges/cornering. Relying on a standard sans-Serif font as a backup if the Google font becomes unavailable. <br>
Bootstrap 5's "Native Font Stack" was used for the bread and butter text of the website as it is [dynamic based on the viewing device](https://getbootstrap.com/docs/5.0/content/reboot/#native-font-stack). 

## Features By Page
_Each Page feature section has been formatted as a dropdown for image tidiness, please click on them to expand the dropdown._
### Home page
![Homepage full](readme_images/features/home/homepage_full.png)
<details>
  <summary>
  The home page's Navbar is dynamic based on the login state of the user. Users will not be able to view their profile or checkout until they are authenticated.
  </summary>

  ![Dynamic nav bar login](readme_images/features/home/navbar_login.png)
  ![Dynamic nav bar logout](readme_images/features/home/navbar_logout.png)
  ![Dynamic nav bar mobile](readme_images/features/home/navbar_mobile.png)
  ![Dynamic nav bar mobile expanded](readme_images/features/home/navbar_mobile_expanded.png)
</details>

<details>
  <summary>
  Toasts will display depending on the actions of the user, providing dynamic success or error messages. 
  </summary>

  ![toasts](readme_images/features/home/timestamped_toasts.png)
  ![toasts](readme_images/features/home/toasts_error.png)
</details>

<details>
  <summary>
  A product search bar has been included that will search both product name and its description for your keywords.
  </summary>

  ![Search bar](readme_images/features/home/search_bar.png)
</details>

<details>
  <summary>
  Site favicon created using [favicon.io](https://favicon.io/).
  </summary>

  ![Site Favicon](readme_images/features/favicon/favicon_tab.png)
</details>

<hr>

### Products
![All products full page](readme_images/features/products/all_products_full.png)
<details>
  <summary>
    The header bar present on each page is dynamic based on the highest discount value assigned to a product in the products table. If a product is added with a discount of 20% to the products table, this would be automatically reflected in the banner. <br>
    The banner can be clicked and will return only products that have discount values assigned to them.
  </summary>

  ![Discount header bar](readme_images/features/products/discount_bar.png)
</details>

<details>
  <summary>
    Products with discounts assigned to them will have their regular price and their calculated discount price displayed. <br>
    Each product has their Category/subcategory/technology rendered below the price along with the product rating.
    Each of these categories can be clicked and will return all products of the same tier. 
  </summary>

  ![Discount pricing and category search](readme_images/features/products/dynamic_discount_category_search.png)
</details>

<details>
  <summary>
    A "return to top" button has been included in the general products page that will allow the user to return to the top of the page quickly. 
  </summary>

  ![Return to top button](readme_images/features/products/return_button.png)
</details>

<details>
  <summary>
    A "Sort By" dropdown feature has been implemented to allow quicker searching by multiple product dimensions.
  </summary>

  ![Sort by feature](readme_images/features/products/sort_by.png)
</details>
<hr>

### Product details
![Product details page full](readme_images/features/product_details/product_details_full.png)
<details>
  <summary>
  Authenticated users can leave a review of products, this is then stored in the database. 
  </summary>

  ![Leave review](readme_images/features/product_details/leave_review.png)
</details>

<details>
  <summary>
    Product reviews are filtered and passed to a modified bootstrap carousel that will cycle each review. 
  </summary>

  ![Dynamic review section](readme_images/features/product_details/product_details_review.png)
</details>

<details>
  <summary>
    A validated quantity selector has been added that will only allow quantities between 1 and 99. 
  </summary>

  ![Quantity selector](readme_images/features/product_details/quantity_selector.png)
</details>

<details>
  <summary>
    A size selector has been added for products that may have multiple sizes. 
  </summary>

  ![Size selector](readme_images/features/product_details/size_selector.png)
</details>

<hr>

### Cart
  ![Cart page full](readme_images/features/cart/cart_full.png)
<details>
  <summary>
    Users will only be able to click through to the checkout when authenticated.
  </summary>

  ![Authenticate only cart](readme_images/features/cart/authenticate_cart.png)
</details>

<details>
  <summary>
    The users cart is stored in the browser session and will persist until session data has been cleared from the site. This setup prevents extra load being added to the database. 
  </summary>

  ![Session stored in cart](readme_images/features/cart/session_cart.png)
</details>

<details>
  <summary>
    The cart page allows modifications of the users items in the cart, including adding or removing quantitys/items.
  </summary>

  ![Update or remove from cart](readme_images/features/cart/update_remove_cart.png)
</details>

<hr>

### Checkout
  ![Checkout page full](readme_images/features/checkout/checkout_full.png)
<details>
  <summary>
    Delivery details can be saved at the checkout, this will save to the users profile.
  </summary>

  ![Save details](readme_images/features/checkout/save_details.png)
</details>

<details>
  <summary>
    Stripe payments have been integrated to the website, allowing both users and the site admins/owners to process their payments and orders with ease. 
  </summary>

  ![Stripe payments](readme_images/features/checkout/stripe_payments.png)
</details>

<details>
  <summary>
    A custom spinner was implemented that occurs when the payment button has been clicked, this will be rendered until the stripe payment is complete. 
  </summary>

  ![Stripe payments spinner](readme_images/features/checkout/checkout_spinner.png)
</details>

### Stripe Webhooks
Stripe webhooks were implemented in parallel with the payments integration. The webhook allows for added failsafes to payments when communication issues may arise, or database errors caused at the time of payment. <br>
A webhook provides direct feedback from the stripe API that a payment has been completed or failed leading to faster response times to orders or issues. <br>
The webhook response can also be used to trigger event specific functions like triggering an order confirmation email for a customer. 
<details>
  <summary>
    Click to expand Local webhook.
  </summary>

  ![Local webhook](readme_images/features/webhooks/local_webhook.png)
</details>

<details>
  <summary>
    Click to expand Local webhook order details.
  </summary>

  ![Local webhook details](readme_images/features/webhooks/local_webhook_details.png)
</details>

<details>
  <summary>
    Click to expand deployed webhook.
  </summary>

  ![Deployed webhook](readme_images/features/webhooks/deployed_webhook.png)
</details>

<details>
  <summary>
    Click to expand deployed webhook order details.
  </summary>

  ![Deployed webhook details](readme_images/features/webhooks/deployed_webhook_details.png)
</details>

<hr>

### Accounts

<details>
  <summary>
    The Allauth package has been used for user authentication and verification, their templates have been modified to suit the styling of the site. 
  </summary>

  ![Allauth account login](readme_images/features/accounts/accounts_sign_up.png)
</details>

<hr>

### Profiles
  ![Profile page full](readme_images/features/profile/profile_full.png)
<details>
  <summary>
    The user profile has been created with a modular setup in mind, allowing sections to be easily added in the future. 
  </summary>

  ![User profile Cards](readme_images/features/profile/profile_order_rating_cards.png)
</details>

<details>
  <summary>
    The orders card will open a modal that returns all orders that a user has made, hyperlinking to their checkout success page, detailing their order details. This is ordered by most recent date for better UX. The table also takes into account overflow and will be scrollable depending on the amount of orders the user has made previously. 
  </summary>

  ![User order history](readme_images/features/profile/order_history.png)
</details>

<details>
  <summary>
    The ratings card will return all reviews that a user has made in a table similiar to the order history modal. It also contains a switch that enable deletions if the user would like to remove their ratings. This is disabled by default to prevent users from deleting their reviews accidently. 
  </summary>

  ![User ratings table](readme_images/features/profile/user_ratings_profile_table.png)
</details>

<details>
  <summary>
    The users shipping details can be created/save and delete from their profile. These details will autofill when a user is at the checkout page. 
  </summary>

  ![User shipping details](readme_images/features/profile/shipping_details_crud.png)
</details>

<hr>

### Emails
Gmail was used for the deployed site as an SMTP server for sending emails to customers for both account related information and for order confirmations. The setup documentation for this can be found [here.](https://support.google.com/a/answer/176600?hl=en)
<details>
  <summary>
    Users will be sent an email on signup to verify their account via a unique URL (Account verifcation is disabled for this project - the  email is still sent however.)
  </summary>

  ![Signup email](readme_images/features/emails/email_confirmation.png)
</details>

<details>
  <summary>
    Users will receive an order confirmation email containing a brief description of their shipping details and total costs.
  </summary>

  ![Order confirmation email](readme_images/features/emails/email_order_confirmation.png)
</details>


<hr>

### Defensive Design
* Users must be validated to access any part of the site that requires authentication, including the cart/checkout/profile pages. <br>
* A custom 404 page has been implemented that will be returned if any page/records cannot be found.
![Custom 404 page](readme_images/features/defensive_design/custom_404.png) 
<br>

* User input fields have either custom validation written for values, or inherited required status from their database models. 
![Form validation required](readme_images/features/defensive_design/form_required_validation.png)
![Quantity validation](readme_images/features/defensive_design/quantity_validation.png)

<hr>

### Future Implentations
1. A user story has already been included into the user story backlog, i would like the super-user to have a dedicated front end page that allows them to add products to the database when needed. Currently the user is able to do this via the admin panel, however i would prefer it to be contained within the frontend of the site with site branding + colouring ect. 
2. In tandem with the user reviews, i would like a numbered rating system that is submitted alongside this. The product ratings would then be amalgamated to form the ratings average for each product instead of being submitted by the super-user when the product is created. 
3. A product wishlist implented onto each product and saved to the users profile, this could then be retrieved via the profile page. 
4. Once product ratings are implemented, i would like to refactor all of the ratings related code to be self contained within its own app for orthogonality. 

## Technologies Used

### Languages & Packages Used 
 ![HTML badge](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
 ![CSS badge](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
 ![Python badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
 ![Javasscript badge](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)   

* packages/Frameworks/Libraries:
  * Django Framework - A Full Stack Python web framework.
  * Bootstrap - A framework designed for responsive + rapid web design.
  * Jquery - A javascript library used for DOM manipulation. **
  * Font Awesome - A CDN For iconography.
  * AllAuth - Used for User authentication and registration.
  * Gunicorn - A Python WSGI HTTP server that aids in deployment.
  * psycopg2-binary - A postgreSQL adapter for Python. 
  * dj-database-url - For parsing the hosted SQL server URL. 
  * Stripe - For secure integrated payment systems.
  * S3transfer - For backend configuration of the AWS s3 Bucket.
  * python-dotenv - Used for .env variable imports. 
  * Crispy forms - For quicker/easier form styling. 
<br>

** _As of Bootstrap v5, jquery is no longer required._

## Database tools
* The development environment used the inbuilt SQLite3 database. 
* PostgreSQL and an externally hosted SQL Server by 
[ElephantSQL.](https://www.elephantsql.com/docs/index.html)
### Programs Used
* Github was used as a repository to store website files and code. 
* Amazon AWS s3 was used for image storage and serving images. 
* Gitpod used as the coding environment with git for version control.
* Balsamic For wireframes. 
* Google Dev tools for development and testing responsiveness. 
* [DbVisualiser.](https://www.dbvis.com/) 
  for creating the Database Schema's. 
* [Site Palette](https://chromewebstore.google.com/detail/site-palette/pekhihjiehdafocefoimckjpbkegknoh?hl=en-GB)
  to create the website colour palette image. 

## Deployment and Local Development
Please refer to [the deployment document](DEPLOYMENT.md) for relevant information on deployment and local development. 

## Testing
Please refer to the [testing document](TESTING.md) for relevant information on testing.

## marketing 
Below are a few strategies that would be employed for marketing how the brand could increase customer reach, brand awareness and how customers view the products. 

### Strategic Partnerships:
* Explore partnerships with cycling events, teams, or influencers. Sponsoring races or collaborating with popular cyclists for events can significantly boost brand visibility.

### Community Engagement:
* Leverage online forums and communities where cycling enthusiasts gather. Participate in discussions, share valuable content, and engage with potential customers directly.

### User-Generated Content:
* Encourage the customer base to share their experiences with La Selle products. Create a hashtag for the brand and ask users to use it when posting their cycling adventures, creating a community around the brand.

### Interactive Content:
* Consider creating interactive content like quizzes or challenges related to cycling and share them on social media. This not only engages the audience but also provides an opportunity for user data collection.

### Customer Reviews and Testimonials:
* Highlight customer reviews and testimonials on the website and social media platforms. Real experiences from actual users can be powerful in convincing potential customers.

### Localized Marketing:
* Tailor the marketing campaigns based on local cycling events or trends. Highlighting regional cycling scenes can resonate well with different segments of the target audience.

### Influencer Marketing:
* Collaborate with cycling influencers who align with the brand values. Their endorsement can be influential, especially if they have a strong and engaged follower base within the target demographic.

### Sustainability and Innovation:
* Emphasize any sustainability efforts in the product design or manufacturing processes. The cycling community often appreciates environmentally conscious brands. Additionally, highlight any innovative features that set the products apart.

### Limited Editions and Special Releases:
* Introduce limited edition products or special releases to create a sense of exclusivity and urgency among consumers. This can drive both sales and brand excitement.

### Educational Content:
* Share educational content about cycling techniques, maintenance, or training tips. Establishing the brand as an authority in the cycling space can enhance credibility.

### B2B Distributor and Supplier Engagement:
* Implement marketing strategies aimed at distributors and suppliers to increase throughput and market share. Establish mutually beneficial partnerships to expand La Selle's reach within the cycling market.

### Mailing list
When users first access the shop page, they will be prompted to sign up to the shops mailing list for exclusive updates and offers. They can use their email and phone number, the phone number is optional. These contact details can then be used to provide targeted promotions and offers based on the users purchase data. Users will only be prompted to sign up for their first visit or when they next clear their cookies - there is nothing more annoying than constant popups when browsing a page. 

![Email mailing list signup](readme_images/features/emails/email_mailing_signup.png)

### Mockup Facebook page
<details>
  <summary>
  Mockup Facebook page.
  </summary>
  
  ![Mockup Facebook page](readme_images/marketing_facebook.png)
</details>


###  Marketing synopsis 
The La selle consumer base would mainly consist of racing amateurs or hobbyist racing cyclists that could be reached via other brick and mortar shops online shops or cycling blogs. The consumer base would mostly use both facebook and instagram as their social media platforms as these are the most common. 
Most apropriate content would be interviews or ride alongs with professional cyclists already using the product. Making-of documentaries would also work well due to the prevalent interest in "marginal gains" in cycling and how they are achieved. Product testing in cycling is also highly viewed due to being easily understood. 
Offers would be best received by email, however advertisements within content promotion would also work as the average cyclists age is slightly higher than other sports demographics. 
The goal of the business is to drive sales, however a secondary effect of the marketing is to drive brand awareness. 
A high budget for advertising would be important however this would be more aimed at the organic content creation as opposed to paid advertising. The younger generation of consumers quickly identify paid advertising and is a highly volatile way to market to younger consumers. 

## credits
### Content
All non-product related content for this website was created by me - David Kirby. <br>
Product descriptions were taken from Selle italia's product sales package which is distributed for free use to any bike shop/retailer who sells their products, due to this their images/descriptions are non-copyrighted.

## Media
Images used for products taken from Selle Italia's sales package. <br>
The hero image was taken from [Getty Images](https://www.gettyimages.ie/) as the image is royalty/copyright free. 

 
## Acknowledgments
Richard Ash for his code-block on bootstrap 5 toasts on the CI slack channel. <br>
[Spencer Barriball](https://github.com/5pence) For his guidance as my Code Institute mentor. <br>
[Kera cudmore](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) For her fantastic README template. <br>
