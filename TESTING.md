## Testing

## Validation Testing 
The W3C validator was used to validate all HTML pages on this site and also used to validate the CSS. 
<hr> 

### HTML 

| Page | Result |
| :--- | :--- |
| Home Page | Pass |     
| View Booking | Pass |     
| Amend Booking | Pass |    
| Cancel Booking | pass | 
| Menu | pass |       
| Reserve Success | pass |
| log in | pass |
| Log Out | Pass | 
| sign up | pass | 
<hr>

### CSS 
style.CSS file in static directory has passed W3C with no errors. 
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

### python
All python code adheres to pep 8 standards. Some lines are viewed as too long, however stylistically they would be harder to read if not in a uniform code block or across multiple lines.

## Automated Unit Testing
Unit testing was used in this project once the database and the models were up and running. There is a variable in the `settings.py` file called `TESTING`, this value needs to be set to `True` in conjunction with `DEBUG` to run the tests on the SQLite database as the test will not run against the postgreSQL database due to external factors. 

Unit tests can be found [here.](https://github.com/DavidUWL/Project-4/blob/main/therestaurant/tests.py)
* The first test case: `ReservationQuerySetTests` simulates a table being assigned automatically when a form is submitted to test the `reserve_table()` function is working correctly. 
* The second test case: `ReservationViewTest` simulates an authenticated user making a booking and verifies whether the reservation is written to the database correctly and redirects to the success page. 

### Solved Bugs
* A bug was experienced when deploying to Heroku where the build wheels for the `backports.zoneinfo` package could not be built. A solution was given on [stack overflow](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta) by user [ayandebnath](https://stackoverflow.com/users/13618361/ayandebnath) to modify the requirements.txt file to include the line which resolved the issue:
```python
backports.zoneinfo;python_version<"3.9"
```

* A bug with the footer being pushed off the bottom of the page was encountered, this was being caused by incorrectly giving the container a class of table-responsive, which is not in use with bootstrap 5. 

### known/unresolved bugs 
* There is a known bug with specifically very small width viewports that causes the tables to push the footer off the end of the page by 80px depending on the amount of values entered. This is caused by the `main {padding-top: 80px;}` and will be resolved in a future release that refactors the navbar into a sidebar overlay. 

### Complications
Many complications were experienced when creating this project, whether it be with code or with the deployment itself. I would typically not deem complications a "bug" until the code has become live and deployed into the wild, prior to this - its simply unimplemented code. If the developer needs to move on, i can see the need for bug tracking at this point - however i did not experience any complications that took a substantial amount of time from the rest of the project. 


### Testing User Stories 
All user stories would require their tasks completed before testing their acceptance. 
| #ID  | Acceptance | Notes if Required
| :--- | :--- | :---: 
|[#1](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=45210713) | PASS |
|[#2](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884010) | PASS |
|[#3](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884008) | PASS |
|[#4](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884007) | PASS |
|[#5](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884005) | PASS |
|[#6](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884003) | not implemented | May be implemented in the future.
|[#7](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884002) | PASS |
|[#8](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37884000) | PASS | Owner can view all bookings in admin panel.
|[#9](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37883995) | PASS |
|[#10](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37883993) | PASS |
|[#11](https://github.com/users/DavidUWL/projects/1?pane=issue&itemId=37883988) | PASS | Owner can modify each booking field in admin panel once a reservation is made.