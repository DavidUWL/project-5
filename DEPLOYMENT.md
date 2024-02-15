# Deployment & Local Development
The deployment setups attached below are current at the time of creating this deployment document, they are subject to change as the providers needs and documented procedures are updated.  

## ElephantSQL
ElephantSQL provided the hosting and backend for our SQL database.<br>
The database can be created by the following: <br>
  1. Create a new instance in your ElephantSQL dashboard, this can be found in the top right.
  2. Give your instance a name and choose the region closest to you.
  3. Click create instance in the bottom right.
  4. Copy the URl from your dashboard for the new database. 

## Heroku
Heroku Provided the web hosting for our application.
The Heroku App can be created by the following: <br>
  1. From your Heroku Dashboard, click "new" in the top right and create a new app.
  2. Give your App a unique name and click Create App. 
  3. Once created, open the app settings and select config var - create a new variable called `DATABASE_URL` and give it the value of the ElephantSQL URL you copied in step 4 previously.
  
### Preparing your Workspace for Deployment
  1. install dj_database_url and psycopg2 .
  ```python
  pip3 install dj_database_url psycopg2 gunicorn 
  ```
  2. update your requirements.txt file to reflect your new installs.
  ```python
  pip3 freeze > requirements.txt 
  ```
  3. Open your .env file and insert your `DATABASE_URL` variable and its URL value(From step 4 in ElephantSQL steps).
  4. In settings.py Under your OS import - write `import dj_database_url`.
  5. Find your DATABASES variable in settings.py and comment it out, replacing it with the below: 
  ```python 
  DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
  }
  ```
  6. Run your server from the terminal to verify your database connection with `python3 manage.py runserver`

  7. Create your superuser with the terminal command : `python3 manage.py createsuperuser`
  8. View your new superuser within elephant SQL by querying the auth_user table. 
  9. modify your database pointers in settings.py to the below:
  ```python
  if DEBUG:
      DATABASES = {
      'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          }
        }
  else:
      DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
      }
  ```
  10. If your `DEBUG` variable in settings.py is set to `True` you will now use the SQLite database for development, if false you will be working with the deployed database.
  11. Create a `Procfile` (capital P) in your root directory and add the below line of code to serve your app via gunicorn: 
  ```python
  web: gunicorn YOUR_APP_NAME.wsgi:application
  ``` 

  12. add the below code to your allowed hosts and modify the Heroku URL to your deployed URL: 
  ```python
  if DEBUG:
    ALLOWED_HOSTS = ['8000-daviduwl-project5-jusbyi2qwcf.ws-eu108.gitpod.io']
  else: 
    ALLOWED_HOSTS = ['la-selle-45cacae9f212.herokuapp.com']
  ``` 
  13.  Enable Automatic deployments on Heroku within the deploy section of your app. Connect via your GitHub credentials and search for your current working repo and connect, you will now be able to select automatic deployments below. 
  14. Save your current changes and add a commit message and push to GitHub.

## Forking/Cloning 
To create a fork for this repository: 
* Navigate to the url - https://github.com/DavidUWL/project-5
  * In the top right corner, click on the Fork dropdown. 
  * Create a new fork
  * Name the repository and/or give it a description - Click create fork. 
* You have now created a fork of this repository! 
To create a clone of this repository:
* Navigate to the url - https://github.com/DavidUWL/project-5
  * Click on the "code" button and select which format you would like to clone with and copy that link.
  * In your Terminal window of whichever IDE you use, navigate to the whichever directory you want to clone the project to. 
  * type into the terminal "git clone", you have now cloned the project! 


## Amazon AWS S3 Bucket
To create an Amazon S3 Bucket: 
1. Create your amazon account [here](https://portal.aws.amazon.com/billing/signup#/start/email) 
and add your billing information - you will not be charged unless you exceed the free tier usage terms. 
2. Once logged in, navigate to all services and storage. Click on the link saying "S3".
3. choose a name for your bucket and select your nearest region. 
4. For "object ownership" select "ACLS enabled and continue. 
5. Select the checkbox that enables public access to your bucket and click create. 
6. Select your newly created bucket and select the properties tab. Click "edit" under 'static website hosting' and enable this setting. Copy your ARN number from here for later. 
7. Navigate to the permissions tab and scroll to the "CORS" section, edit this section and add the below code: 

```python
 [
   {
       "AllowedHeaders": [
           "Authorization"
       ],
       "AllowedMethods": [
           "GET"
       ],
       "AllowedOrigins": [
           "*"
       ],
       "ExposeHeaders": []
   }
 ]
``` 

8. Return to the "bucket policy" section and click 'edit', open the policy generator page. 
9. Select 'S3 Bucket policy' from the policy menu and insert the * selector inside 'Principle'. 
10. Select 'get Object' from the actions dropdown - insert the ARN number that we copied from earlier into the Amazon Resouce name Field. 
11. Add the statement and generate the policy. Copy this policy and insert it into your policy editor. 
12. Add "/*" to the tail of your resouce key to allow access to all resouces contained. 
13. Edit the ACL section and enable the 'list' checkbox, agree to the popup and save. 

### IAM user management 
1. Search for IAM in the user searchbar.
2. Click on IAM and navaigate to user groups and create a group. Name this group and click create. 
3. Click on policies and create a policy, enter the JSON section and 'import managed policy'. Search for S3 and select "AmazonS3FullAccess" and import. 
4. Edit the newly imported policy and update it with the below information, insertingy your copied arn number as required. 

```python
 {
         "Version": "2012-10-17",
         "Statement": [
         {
                 "Effect": "Allow",
                 "Action": [
                 "s3:*",
                 "s3-object-lambda:*"
                 ],
                 "Resource": [
                 "copied_arn_number",
                 "copied_arn_number/*"
                 ]
         }
         ]
 }
```

5. Click through until you are on the "review" section and name the policy and give a description if required and save.
6. On the policy page, click on "user groups" and click on the the permissions tab, and "add permissions" - click on "attach policies". Add your created policy. 
7. Click on "add user" from the sidebar, name it and click on "prgrammatic access" and continue, select your group and proceed to create the user. 
8. Once created, download the CSV containing your secret access key and regular key.   

### Django integration 
Two packages are required before beginning, run the below code to install and save the required package names:
```python
 pip3 install boto3
 pip3 install django-storages
 pip3 freeze > requirements.txt
```

1. Navigate to your settings.py file and add "storages" to your installed apps. 
```python
INSTALLED_APPS = [
    '...',
    '...',
    'crispy_forms',
    'profiles',
    'ratings',
    'storages',
]
```

2. Copy the below code and insert it into your settings.py file : 
```python
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age-94608000'  # allows caching of images for faster load times
    }

    AWS_STORAGE_BUCKET_NAME = 'YOUR_PROJECT_NAME'
    AWS_S3_REGION_NAME = 'YOUR_SELECTED_REGION'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

3. Open your CSV file containing your access keys, navigate to your deployed heroku app - open the app settings and click "reveal VARS".
4. Add both `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` variables and their values. Add `USE_AWS` and the value of `True`, remove `DISABLE_COLLECTSTATIC` if this was added previously. 
5. We now need to define `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE` to assign our static/media directories within S3. 
6. create a new file called "custom_storages.py" in your root directory. 
7. Add the below code to this file : 
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
8. Save-add-commit-push your changes to github and wait for the auto deploy to complete, this will also push your static files to the S3 bucket. 
9. Navigate to S3, open your file directories, create a new folder called 'media' and upload all images in use on your site. 
10. Under 'permissions' select 'grant public read access' and upload, agree to any popups.

**Your S3 setup is now complete.**

## Stripe

### initial setup 
To begin, a stripe account is needed - signup can be completed [here.](https://dashboard.stripe.com/register)

Stripe have refined their documentation over the years and now provide quick and succinct documentation to get stripe payments up and running, initial setup documentation can be found [here.](https://docs.stripe.com/payments/accept-a-payment#web-collect-card-details)

### webhooks 
A Stripe webhook is a tool that enables real-time communication between your server and Stripe, notifying your application of important events like successful payments. When these events occur, Stripe sends secure HTTP POST requests to a specified endpoint on your server, this allows you to carry out any custom logic when the post request is received via this endpoint. 

1. Login to your stripe account, activate test mode and click on "Developers" to the left. 
2. Click on "Webhooks" and add an endpoint. Enter your endpoint address - my endpoint address was `https://my_app.heroku.com/checkout/WH/`
3. Click on "select events" and select "all events", add them to the webhook and proceed with the creation. 
4. Once on the webhook page, you will be able to reveal your webhook key - save this for later. 
5. in either your `.env` file or `env.py` file add the webhook key along with your stripe variables if not added already from the stripe documentation setup: 

```python 
# inside .env or env.py files
 STRIPE_PUBLIC_KEY = 'insert your public key'
 STRIPE_SECRET_KEY = 'insert your secret key'
 STRIPE_WH_SECRET = 'insert the webhook key copied from earlier'
 ```

 6. Navigate to your settings.py file and now reference these variables: 
```python
# inside your settings.py file
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')
``` 

Your stripe webhook is now configured. 



