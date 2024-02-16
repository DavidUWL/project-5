# Full Project Testing 

   * [Validation Testing](#validation-testing)
      + [python](#python)
- [Manual Testing](#manual-testing)
   * [Base template](#base-template)
   * [Home](#home)
   * [Products](#products)
      + [Multi products](#multi-products)
      + [Product details](#product-details)
      + [Review Modal](#review-modal)
   * [Cart](#cart)
   * [checkout](#checkout)
      + [Checkout confirmation](#checkout-confirmation)
      + [Stripe Payment](#stripe-payment)
      + [Stripe test-card details](#stripe-test-card-details)
         - [Checkout success](#checkout-success)
   * [Profile ](#profile)
      + [Order history modal](#order-history-modal)
      + [Ratings history modal](#ratings-history-modal)
   * [Custom 404 page](#custom-404-page)
   * [Bugs](#bugs)
      + [Solved Bugs](#solved-bugs)
      + [known/unresolved bugs](#knownunresolved-bugs)
   * [User story testing](#user-story-testing)



## Validation Testing 
All code was passed through validation tools, namely: 
* W3C HTML checker
* W3C CSS checker 
* Flake8/CI pep8 lintner
* ESLint with JQuery addon.
<hr> 

| App        |![HTML Badge](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)                                              | ![CSS Badge](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)                                             | ![JavaScript Badge](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)                                       | ![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)                                            |
|------------|---------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| cart       | PASS                                              | -                                                | -                                                 | PASS                                               |
| checkout   | PASS                                              | PASS                                               | PASS                                               | PASS                                               |
| home       | PASS                                              | -                                                 | -                                                 | PASS                                               |
| products   | PASS                                              | -                                                 | PASS                                               | PASS                                               |
| profiles   | PASS                                              | PASS                                               | PASS                                               | PASS                                               |
| ratings    | PASS                                              | -                                                 | PASS                                                 | PASS                                               |

"-" _denotes not present._

### python
All python code adheres to pep 8 standards. Some lines are viewed as too long, however stylistically they would be harder to read if not in a uniform code block or across multiple lines.

# Manual Testing

## Base template

<details>
  <summary>
    Click to expand base template testing table.
  </summary>

| Feature                           | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Favicon Display                   | 1. Load the website in a browser.                                                                                      | The favicon should be displayed in the browser tab. | Pass          |
| Page Title                        | 1. Inspect the page title.                                                                                              | The page title should be "La Selle" or as specified in the `extra_title` block. | Pass          |
| Meta Tags                         | 1. Inspect the meta tags (charset, viewport, description, etc.).                                                      | Meta tags should be present and set appropriately. | Pass          |
| CSS Stylesheets                   | 1. Inspect the loaded CSS stylesheets.                                                                                  | Core and extra CSS stylesheets should be loaded without errors. | Pass          |
| JavaScript Libraries              | 1. Inspect the loaded JavaScript libraries.                                                                           | Core and extra JavaScript libraries should be loaded without errors. | Pass          |
| Discount Banner Display           | 1. Load the website in a browser.                                                                                      | The discount banner should be displayed with the correct discount percentage. | Pass          |
| Navigation Bar Display            | 1. Load the website in a browser.                                                                                      | The navigation bar should be displayed with the correct links and categories. | Pass          |
| Search Bar Functionality          | 1. Type a query in the search bar and press Enter.                                                                     | The user should be redirected to the products page with search results. | Pass          |
| Navigation Dropdowns              | 1. Hover over each navigation dropdown item.                                                                          | Dropdowns should display subcategories and link to the correct pages. | Pass          |
| My Account Dropdown               | 1. Click on the "My Account" dropdown.                                                                                 | For authenticated users, it should display links to view profile and logout. For unauthenticated users, it should display links to register and login. | Pass          |
| Shopping Bag Icon                 | 1. Click on the shopping bag icon.                                                                                    | The off-canvas cart should slide in, displaying the current total amount. | Pass          |
| Toast Messages                    | 1. Trigger different types of messages (error, warning, success, info).                                                | Toast messages should appear with the correct styles and content. | Pass          |
| Toast Autohide                    | 1. Trigger a message with autohide.                                                                                    | The toast message should disappear after a few seconds. | Pass          |
| Toast Dismiss Button              | 1. Trigger a message. 2. Click the dismiss button on the toast.                                                        | The toast message should disappear immediately.    | Pass          |
| Timestamp Display                 | 1. Trigger a message.                                                                                                  | The toast message should display a timestamp.       | Pass          |
</details>




## Home
<details>
  <summary>
    Click to expand home testing table.
  </summary>

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Header Container                   | 1. Open the home page.                                                                                                   | The header container should be present and contain the main content of the home page. | Pass          |
| Quote Section                      | 1. Open the home page. 2. Check for the presence of the quote. 3. Look for a button with the label "Shop Now." 4. Click on the "Shop Now" button. | The quote section should display a notable quote along with a call-to-action button. | Pass          |
| Link to Products                   | 1. Click on the "Shop Now" button from the quote section.                                                                | Clicking on the "Shop Now" button should navigate the user to the products page. | Pass          |
</details>

## Products 

<details>
  <summary>
    Click to expand Multi-products testing table.
  </summary>

### Multi products
| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Sort Selection Dropdown             | 1. Open the products page.                                                                                              | A dropdown should be present for selecting sorting options. | Pass          |
| Sort By Price (Low to High)         | 1. Open the products page. 2. Select "Price (low to high)" from the dropdown.                                            | Products should be sorted by price in ascending order. | Pass          |
| Sort By Price (High to Low)         | 1. Open the products page. 2. Select "Price (high to low)" from the dropdown.                                            | Products should be sorted by price in descending order. | Pass          |
| Sort By Rating (Low to High)        | 1. Open the products page. 2. Select "Rating (low to high)" from the dropdown.                                           | Products should be sorted by rating in ascending order. | Pass          |
| Sort By Rating (High to Low)        | 1. Open the products page. 2. Select "Rating (high to low)" from the dropdown.                                           | Products should be sorted by rating in descending order. | Pass          |
| Sort By Name (A-Z)                  | 1. Open the products page. 2. Select "Name (A-Z)" from the dropdown.                                                     | Products should be sorted by name in ascending alphabetical order. | Pass          |
| Sort By Name (Z-A)                  | 1. Open the products page. 2. Select "Name (Z-A)" from the dropdown.                                                     | Products should be sorted by name in descending alphabetical order. | Pass          |
| Sort By Category (A-Z)              | 1. Open the products page. 2. Select "Category (A-Z)" from the dropdown.                                                 | Products should be sorted by category in ascending alphabetical order. | Pass          |
| Sort By Category (Z-A)              | 1. Open the products page. 2. Select "Category (Z-A)" from the dropdown.                                                 | Products should be sorted by category in descending alphabetical order. | Pass          |
| Sort By Subcategory (A-Z)           | 1. Open the products page. 2. Select "Subcategory (A-Z)" from the dropdown.                                              | Products should be sorted by subcategory in ascending alphabetical order. | Pass          |
| Sort By Subcategory (Z-A)           | 1. Open the products page. 2. Select "Subcategory (Z-A)" from the dropdown.                                              | Products should be sorted by subcategory in descending alphabetical order. | Pass          |
| Sort By Technology (A-Z)            | 1. Open the products page. 2. Select "Technology (A-Z)" from the dropdown.                                               | Products should be sorted by technology in ascending alphabetical order. | Pass          |
| Sort By Technology (Z-A)            | 1. Open the products page. 2. Select "Technology (Z-A)" from the dropdown.                                               | Products should be sorted by technology in descending alphabetical order. | Pass          |
| Products Count Display              | 1. Open the products page.                                                                                              | The total number of products should be displayed.    | Pass          |
| Search Term Display                 | 1. Open the products page with a search term.                                                                           | The search term should be displayed in the message.  | Pass          |
| Reset Sorting                       | 1. Open the products page with sorting applied. 2. Select "Sort By.." from the dropdown.                               | Sorting should be reset, and products should be displayed in their default order. | Pass          |
| Product Display                     | 1. Open the products page.                                                                                              | Products should be displayed with images, names, prices, categories, and ratings (if available). | Pass          |
| Product Image Display               | 1. Open the products page.                                                                                              | Each product should have an associated image displayed. | Pass          |
| Product Price Display               | 1. Open the products page.                                                                                              | Each product should have its price displayed.         | Pass          |
| Product Category Display            | 1. Open the products page.                                                                                              | Each product should have its category displayed.      | Pass          |
| Product Subcategory Display         | 1. Open the products page.                                                                                              | Each product should have its subcategory displayed.   | Pass          |
| Product Technology Display          | 1. Open the products page.                                                                                              | Each product should have its technology displayed.    | Pass          |
| Product Rating Display              | 1. Open the products page.                                                                                              | Each product should have its rating displayed.        | Pass          |
| Back-to-Top Button Click            | 1. Scroll down the page. 2. Click the back-to-top button.                                                               | The page should smoothly scroll back to the top.      | Pass          |
</details>


### Product details 
<details>
  <summary>
    Click to expand Product details testing table.
  </summary>

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Product Image                      | 1. Open the product details page.                                                                                        | The product image should be displayed.               | Pass          |
| Product Name                       | 1. Open the product details page.                                                                                        | The product name should be displayed.                | Pass          |
| Product Price                      | 1. Open the product details page.                                                                                        | If there is a discount, the discounted price should be displayed; otherwise, the regular price. | Pass          |
| Category Link                      | 1. Open the product details page.                                                                                        | If the product belongs to a category, a link to that category should be displayed. | Pass          |
| Subcategory Link                   | 1. Open the product details page.                                                                                        | If the product belongs to a subcategory, a link to that subcategory should be displayed. | Pass          |
| Technology Link                    | 1. Open the product details page.                                                                                        | If the product is associated with a technology, a link to that technology should be displayed. | Pass          |
| Product Rating                     | 1. Open the product details page.                                                                                        | If the product has a rating, the rating should be displayed; otherwise, "No Rating" should be shown. | Pass          |
| Product Ratings                    | 1. Open the product details page.                                                                                        | The product ratings section should be displayed.    | Pass          |
| Product Description                | 1. Open the product details page.                                                                                        | The product description should be displayed.         | Pass          |
| Size Selection (if available)      | 1. Open the product details page.                                                                                        | If the product has size options, a dropdown should allow selecting a size. | Pass          |
| Quantity Input                     | 1. Open the product details page.                                                                                        | A quantity input field should be present with increment and decrement buttons. | Pass          |
| Add to Cart Button                 | 1. Open the product details page. 2. Enter valid quantity and size (if applicable). 3. Click the "Buy" button.        | The product should be added to the cart, and the user should be redirected to the cart page. | Pass          |
| Increment/Decrement Quantity       | 1. Open the product details page. 2. Click the increment and decrement buttons for quantity.                            | The quantity should increase and decrease accordingly. | Pass          |
| Redirect URL                       | 1. Open the product details page. 2. Click the "Buy" button.                                                             | The user should be redirected to the correct page, preserving the original request path. | Pass          |
</details>


### Review Modal 
<details>
  <summary>
    Click to expand product review testing table.
  </summary>

| Feature                           | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Review Button Display             | 1. Access a page where the review button is displayed.                                                                | If the user is authenticated, a "Leave a review" button should be displayed; otherwise, a login link should be shown. | Pass          |
| Review Modal Display              | 1. Click the "Leave a review" button (if authenticated).                                                              | A modal with the title "Leave a review" should appear. | Pass          |
| Modal Close Button                | 1. Open the review modal. 2. Click the close button (X) on the modal header.                                         | The modal should be closed.                         | Pass          |
| Modal Overlay Click               | 1. Open the review modal. 2. Click outside the modal overlay.                                                        | The modal should be closed.                         | Pass          |
| Review Form Display               | 1. Click the "Leave a review" button (if authenticated).                                                              | The modal should contain a form for submitting a review with a textarea and a submit button. | Pass          |
| Rating Description Input          | 1. Open the review form.                                                                                               | The form should include an input field for the rating description. | Pass          |
| Submit Review Button              | 1. Open the review form. 2. Fill in the rating description. 3. Click the "Submit review" button.                     | The form should be submitted, and the review should be processed. | Pass          |
| Close Button (Footer)             | 1. Open the review form. 2. Click the "Close" button in the modal footer.                                            | The modal should be closed.                         | Pass          |
| Login Link Display                | 1. Access a page where the review button is displayed. 2. Log out (if authenticated).                                | A message should be displayed with a link to login in order to leave a review. | Pass          |
| Login Link Redirect               | 1. Access a page where the review button is displayed. 2. Click the login link.                                     | The user should be redirected to the login page.   | Pass          |
</details>

## Cart
<details>
  <summary>
    Click to expand Cart testing table.
  </summary>

| Feature                      | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| View Cart Header             | 1. Open the Shopping Cart page.                                                                                        | Shopping Cart header with "Shopping Cart" title and horizontal line is displayed. | Pass          |
| View Cart Table Header       | 1. Open the Shopping Cart page.                                                                                        | Table header with columns: "Product description", "", "Qty", "Price", and "Subtotal" is displayed. | Pass          |
| View Cart Items              | 1. Add items to the shopping cart. <br> 2. Open the Shopping Cart page.                                                 | Table rows with cart items, including product image, name, size, quantity input, update link, and remove link are displayed. | Pass          |
| Update Cart Item Quantity    | 1. Open the Shopping Cart page. <br> 2. Change the quantity of an item using the quantity input. <br> 3. Click the "update" link. | The quantity of the item is updated, and the total is recalculated. | Pass          |
| Remove Cart Item             | 1. Open the Shopping Cart page. <br> 2. Click the "remove" link for an item.                                            | The item is removed from the cart, and the total is recalculated. | Pass          |
| View Delivery Fee            | 1. Open the Shopping Cart page.                                                                                        | Delivery fee is displayed in the "delivery fee" section. | Pass          |
| View Total                   | 1. Open the Shopping Cart page.                                                                                        | Total price, including the delivery fee, is displayed. | Pass          |
| Continue Shopping           | 1. Open the Shopping Cart page. <br> 2. Click the "Continue Shopping" button.                                          | Redirects to the Products page.                     | Pass          |
| Proceed to Checkout          | 1. Open the Shopping Cart page. <br> 2. Click the "Checkout" button.                                                   | Redirects to the Checkout page.                    | Pass          |
| Empty Cart                   | 1. Open the Shopping Cart page. <br> 2. Remove all items from the cart.                                                | Message "You have no items in your cart" is displayed, and "go back" button is available. | Pass          |
</details>

## Checkout 

### Checkout confirmation
<details>
  <summary>
    Click to expand checkout confirmation testing table.
  </summary>

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Checkout Header                    | 1. Open the Checkout page.                                                                                              | Checkout header with the title "Checkout" is displayed. | Pass          |
| Item Subtotal                      | 1. Open the Checkout page.                                                                                              | List of items with images, names, sizes, quantities, and subtotal is displayed. | Pass          |
| Purchase Total                     | 1. Open the Checkout page.                                                                                              | Purchase total is displayed.                         | Pass          |
| Delivery Cost                      | 1. Open the Checkout page.                                                                                              | Delivery cost is displayed.                         | Pass          |
| Grand Total                        | 1. Open the Checkout page.                                                                                              | Grand total is displayed.                           | Pass          |
| Customer Details                   | 1. Open the Checkout page.                                                                                              | Customer details form is displayed.                  | Pass          |
| Payment Details                    | 1. Open the Checkout page.                                                                                              | Payment details form is displayed.                   | Pass          |
| Save Info Checkbox (Logged In)     | 1. Open the Checkout page with an authenticated user.                                                                  | The "Save your details for future purchases" checkbox is checked by default. | Pass          |
| Confirm Order Button               | 1. Open the Checkout page.                                                                                              | The "Confirm Order" button is displayed.             | Pass          |
| Stripe Elements Integration        | 1. Open the Checkout page.                                                                                              | Stripe Elements for card input is displayed.        | Pass          |
| Confirm Order Button Click         | 1. Open the Checkout page. 2. Fill in the required details. 3. Click the "Confirm Order" button.                           | If all details are valid, the order is confirmed, and the loading overlay is displayed. | Pass          |
| Card Charged Message               | 1. Open the Checkout page. 2. Complete the checkout process.                                                             | A message indicating that the card will be charged with the grand total is displayed. | Pass          |
| Loading Overlay                    | 1. Open the Checkout page. 2. Click the "Confirm Order" button.                                                           | A loading overlay is displayed while processing the order. | Pass          |
</details>

### Stripe Payment

<details>
  <summary>
    Click to expand Stripe testing table.
  </summary>

### Stripe test-card details
| Scenario              | Card Number          | Expiry Date       | CVV       | ZIP     |
|-----------------------|----------------------|-------------------|-----------|---------|
| Valid Payment         | 4242 4242 4242 4242  | Any future date   | Any 3 digits | Any 5 digits |
| Declined Payment      | 4000 0000 0000 0002  | Any future date   | Any 3 digits | Any 5 digits |
| Verification (3D Secure) | 4000 0027 6000 3184  | Any future date | Any 3 digits | Any 5 digits |

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Stripe Elements Integration        | 1. Open the Checkout page.                                                                                              | Stripe Elements for card input is displayed.        | Pass          |
| Card Number Validation             | 1. In the card number field, enter a valid card number.                                                                | Card number is accepted.                            | Pass          |
| Expiry Date Validation             | 1. In the expiry date field, enter a valid expiry date.                                                                | Expiry date is accepted.                            | Pass          |
| CVV Validation                     | 1. In the CVV field, enter a valid CVV.                                                                                | CVV is accepted.                                   | Pass          |
| Invalid Card Number                | 1. In the card number field, enter an invalid card number.                                                             | An error message indicates that the card number is invalid. | Pass          |
| Invalid Expiry Date                | 1. In the expiry date field, enter an invalid expiry date.                                                             | An error message indicates that the expiry date is invalid. | Pass          |
| Invalid CVV                        | 1. In the CVV field, enter an invalid CVV.                                                                            | An error message indicates that the CVV is invalid. | Pass          |
| Valid Payment                      | 1. Fill in valid card details. 2. Click the "Confirm Order" button.                                                    | Payment is successful, and a success message is displayed. | Pass          |
| Declined Payment                   | 1. Fill in valid card details. 2. Use a test card number that results in a declined payment (e.g., 4000000000000002). | A message indicates that the payment is declined, and the user is prompted to try another card. | Pass          |

</details>

#### Checkout success 
<details>
  <summary>
    Click to expand Checkout success testing table.
  </summary>

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Purchase Details Table Header      | 1. Open the Purchase Completed page.                                                                                    | Table header with a dark background and "Purchase Details" title is displayed. | Pass          |
| Purchase Number                    | 1. Open the Purchase Completed page.                                                                                    | Purchase number is displayed in the "Purchase Details" table. | Pass          |
| Order Date                         | 1. Open the Purchase Completed page.                                                                                    | Order date is displayed in the "Purchase Details" table. | Pass          |
| Items Table Header                 | 1. Open the Purchase Completed page.                                                                                    | Table header with a dark background and "Items" title is displayed. | Pass          |
| Items List                         | 1. Open the Purchase Completed page.                                                                                    | List of purchased items with product name, size (if available), and quantity is displayed in the "Items" table. | Pass          |
| Purchase Total                     | 1. Open the Purchase Completed page.                                                                                    | Purchase total is displayed in the "Items" table.    | Pass          |
| Delivery Cost                      | 1. Open the Purchase Completed page.                                                                                    | Delivery cost is displayed in the "Items" table.     | Pass          |
| Grand Total                        | 1. Open the Purchase Completed page.                                                                                    | Grand total is displayed in the "Items" table.       | Pass          |
| Billing & Delivery Table Header    | 1. Open the Purchase Completed page.                                                                                    | Table header with a dark background and "Billing & Delivery" title is displayed. | Pass          |
| Full Name                          | 1. Open the Purchase Completed page.                                                                                    | Full name is displayed in the "Billing & Delivery" table. | Pass          |
| Email                              | 1. Open the Purchase Completed page.                                                                                    | Email is displayed in the "Billing & Delivery" table.  | Pass          |
| Phone Number                       | 1. Open the Purchase Completed page.                                                                                    | Phone number is displayed in the "Billing & Delivery" table. | Pass          |
| Country                            | 1. Open the Purchase Completed page.                                                                                    | Country is displayed in the "Billing & Delivery" table. | Pass          |
| County (if available)              | 1. Open the Purchase Completed page.                                                                                    | County is displayed in the "Billing & Delivery" table if available. | Pass          |
| Town or City                       | 1. Open the Purchase Completed page.                                                                                    | Town or city is displayed in the "Billing & Delivery" table. | Pass          |
| Postcode (if available)           | 1. Open the Purchase Completed page.                                                                                    | Postcode is displayed in the "Billing & Delivery" table if available. | Pass          |
| Street Address1                    | 1. Open the Purchase Completed page.                                                                                    | Street address1 is displayed in the "Billing & Delivery" table. | Pass          |
| Street Address2 (if available)     | 1. Open the Purchase Completed page.                                                                                    | Street address2 is displayed in the "Billing & Delivery" table if available. | Pass          |
</details>

## Profile 
<details>
  <summary>
    Click to expand profile testing table.
  </summary>

| Feature                            | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Profile Title Display               | 1. Open the profile page.                                                                                               | The page should display a title "Your Profile".      | Pass          |
| Update Delivery Form Display       | 1. Open the profile page.                                                                                               | A form for updating delivery details should be displayed. | Pass          |
| Update Delivery Form Submission    | 1. Open the profile page. 2. Fill in the delivery details form. 3. Click the "Update" button.                           | The form should be submitted, and the details should be updated. | Pass          |
| Delete Details Form Display         | 1. Open the profile page.                                                                                               | A form for deleting user details should be displayed. | Pass          |
| Delete Details Form Submission      | 1. Open the profile page. 2. Click the "Delete Details" button.                                                           | A confirmation prompt should appear, and upon confirmation, the user details should be deleted. | Pass          |
| Order History Modal Display        | 1. Open the profile page.                                                                                               | A section displaying order history should be visible. | Pass          |
| Order History Modal Click          | 1. Open the profile page. 2. Click the "Order History" button.                                                            | A modal should appear, displaying the user's order history. | Pass          |
| Ratings History Modal Display      | 1. Open the profile page.                                                                                               | A section displaying ratings history should be visible. | Pass          |
| Ratings History Modal Click        | 1. Open the profile page. 2. Click the "Ratings History" button.                                                          | A modal should appear, displaying the user's ratings history. | Pass          |
</details>

### Order history modal
<details>
  <summary>
    Click to expand order history modal testing table.
  </summary>

| Feature                           | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Orders Card Display               | 1. Open the page with the orders card.                                                                                  | The card with the title "Your Orders" and a shopping cart icon should be displayed. | Pass          |
| Orders Card Content               | 1. Open the page with the orders card.                                                                                  | The card should have a description "View all your previous orders." | Pass          |
| Orders View Button Click          | 1. Open the page with the orders card. 2. Click the "View" button.                                                      | A modal with the title "Order History" should appear. | Pass          |
| Modal Close Button                | 1. Open the modal. 2. Click the close button (X) on the modal header.                                                  | The modal should be closed.                         | Pass          |
| Order History Table Display       | 1. Open the modal.                                                                                                      | A table displaying order history should be visible. | Pass          |
| Order History Table Headers       | 1. Open the modal.                                                                                                      | The table should have columns: "#", "Date", "Grand Total". | Pass          |
| Order History Table Content       | 1. Open the modal.                                                                                                      | The table should display order details including order number, date, and grand total. | Pass          |
| Order Number Link Click           | 1. Open the modal. 2. Click on an order number link in the table.                                                      | The page should navigate to the detailed purchase history of the clicked order. | Pass          |
| Modal Close Button (Footer)        | 1. Open the modal. 2. Click the "Close" button in the modal footer.                                                      | The modal should be closed.                         | Pass          |
| Modal Overlay Click               | 1. Open the modal. 2. Click outside the modal overlay.                                                                | The modal should be closed.                         | Pass          |
</details>

### Ratings history modal 
<details>
  <summary>
    Click to expand Review history testing table.
  </summary>

| Feature                           | Test Steps                                                                                                              | Expected Result                                    | Pass/Fail     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Ratings Card Display              | 1. Open the page with the ratings card.                                                                               | The card with the title "Your Ratings" and a star icon should be displayed. | Pass          |
| Ratings Card Content              | 1. Open the page with the ratings card.                                                                               | The card should have a description "View all the products you have previously rated." | Pass          |
| Ratings View Button Click         | 1. Open the page with the ratings card. 2. Click the "View" button.                                                   | A modal with the title "Your Ratings" should appear. | Pass          |
| Modal Close Button                | 1. Open the modal. 2. Click the close button (X) on the modal header.                                                 | The modal should be closed.                         | Pass          |
| Ratings Table Display             | 1. Open the modal.                                                                                                     | A table displaying product ratings should be visible. | Pass          |
| Ratings Table Headers             | 1. Open the modal.                                                                                                     | The table should have columns: "Product", "Rating Description", and an empty column for deletion. | Pass          |
| Ratings Table Content             | 1. Open the modal.                                                                                                     | The table should display product ratings including product name and rating description. | Pass          |
| Delete Rating Checkbox            | 1. Open the modal.                                                                                                     | The modal should have a "Enable deletion" checkbox.  | Pass          |
| Delete Rating Enable              | 1. Open the modal. 2. Check the "Enable deletion" checkbox.                                                           | The delete buttons in the table should be enabled and displayed in red. | Pass          |
| Delete Rating Disable             | 1. Open the modal. 2. Uncheck the "Enable deletion" checkbox.                                                         | The delete buttons in the table should be disabled and revert to the default color. | Pass          |
| Delete Rating Click               | 1. Open the modal. 2. Check the "Enable deletion" checkbox. 3. Click a delete button in the table.                  | A confirmation prompt should appear, and upon confirmation, the rating should be deleted. | Pass          |
| Modal Close Button (Footer)        | 1. Open the modal. 2. Click the "Close" button in the modal footer.                                                   | The modal should be closed.                         | Pass          |
| Modal Overlay Click               | 1. Open the modal. 2. Click outside the modal overlay.                                                               | The modal should be closed.                         | Pass          |
</details>

## Custom 404 Page
<details>
  <summary>
    Click to expand custom 404 testing table.
  </summary>

| Feature                | Test Steps                                                                                           | Expected Result                                                      | Pass/Fail     |
| ---------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------- |
| Page Title             | 1. Inspect the page title.                                                                          | The page title should be "Page Not Found" as specified in the block. | Pass          |
| Overlay Background     | 1. Load the page in a browser.                                                                     | The overlay background should cover the entire screen.               | Pass          |
| Header Container       | 1. Load the page in a browser.                                                                     | The header container should be present and centered on the page.     | Pass          |
| Header Text            | 1. Load the page in a browser.                                                                     | The header should display "404 - Page Not Found" in a large font.    | Pass          |
| Lead Paragraph         | 1. Load the page in a browser.                                                                     | The lead paragraph should provide information about the error.       | Pass          |
| Horizontal Rule        | 1. Load the page in a browser.                                                                     | A horizontal rule should be present below the lead paragraph.        | Pass          |
| URL Check and Link     | 1. Verify the content of the lead paragraph. 2. Click on the "home page" link.                      | The lead paragraph should instruct the user to check the URL. Clicking the link should redirect to the home page. | Pass          |
| Simulate 404 Error     | 1. Manually enter a non-existent URL in the browser address bar.                                    | The browser should display the custom 404 page.                     | Pass          |
</details>

## Bugs

### Solved Bugs
| BUG | FIX | COMMIT |
|---|---|---|
| Users could not review multiple products - limited to one review only. | Error was being caused by dependency of OneToOne model field, fixed by setting to foreign key and blank=True | [cce1505](https://github.com/DavidUWL/project-5/commit/cce15052f95f2e4112ebc2981785e5b7962b423b) |
| Users could not leave a review, form would render but would submit an empty form on submission. | Code was refactored to create a database record within the product view instead of being contained within the ratings app, and helper functions imported. | [1a7d2d5](https://github.com/DavidUWL/project-5/commit/1a7d2d5df1df70b008089920ce13fbaf2d5ce7f1) |
| Cart would display delivery price when empty. | Fixed by simply adding an "if/else" statement to zero the cart if there are no items. | [8531ce4](https://github.com/DavidUWL/project-5/commit/8531ce4f193cbf2d7fa5675b0ee8eff985ec1d78) |
| Type error with calculate discount price property. | Incorrectly trying to apply decimal package math to non-decimal package converted variables. | [649df5f](https://github.com/DavidUWL/project-5/commit/649df5ff53a4158d9510960f95526d754c5ba70e) |
| Sort options not functional. | Incorrectly calling the option value name. | [0c70ae8](https://github.com/DavidUWL/project-5/commit/0c70ae8e755962d6e1469728fcef0f89f549a119) |


### known/unresolved bugs 
No known bugs at the time of writing. 


## User story testing
All user stories would require their tasks completed before testing their acceptance, "id" links to github project tasks .

| id | User Story | Acceptance | 
| --- | ---------- | ---------- | 
| [#1](https://github.com/DavidUWL/project-5/issues/1)   | As a visitor to the website, I want to view a list of available products for sale. | Pass. | 
| [#2](https://github.com/DavidUWL/project-5/issues/2)   | As a user, I want to add products to my shopping cart for future purchase. | Pass. | 
| [#3](https://github.com/DavidUWL/project-5/issues/3)   | As a user, I want to view and manage the contents of my shopping cart. | Pass. | 
| [#4](https://github.com/DavidUWL/project-5/issues/4)   | As a user, I want to enter my shipping details before making a purchase. | Pass. | 
| [#5](https://github.com/DavidUWL/project-5/issues/5)   | As a user, I want to make a payment for the items in my shopping cart. | Pass. | 
| [#6](https://github.com/DavidUWL/project-5/issues/6)   | As a user, I want to view a summary of my order after completing a purchase. | Pass. | 
| [#7](https://github.com/DavidUWL/project-5/issues/7)   | As a user, I want to view my order history on my profile. | Pass. | 
| [#8](https://github.com/DavidUWL/project-5/issues/8)   | As a user, I want to view a detailed summary of a specific order. | Pass. | 
| [#9](https://github.com/DavidUWL/project-5/issues/9)   | As a user, I want to receive email notifications for order confirmation. | Pass. | 
| [#10](https://github.com/DavidUWL/project-5/issues/10)  | As a user, I want to log in securely to access my profile and order history. | Pass. | 
| [#11](https://github.com/DavidUWL/project-5/issues/11)  | As a user, I want to log out securely to protect my account. | Pass. | 
| [#12](https://github.com/DavidUWL/project-5/issues/12)  | As a user, I want the website to be visually appealing and responsive. | Pass. | 
| [#13](https://github.com/DavidUWL/project-5/issues/13)  | As a Shopper, I want to be able to provide ratings and descriptions for the products I have purchased, so that I can share my experiences and help other users make informed decisions. | Half-Pass. | 
| [#14](https://github.com/DavidUWL/project-5/issues/14)  | As an admin, I want to add or remove products without having to use the built-in admin panel. | - | 


