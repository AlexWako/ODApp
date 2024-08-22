## OD App

The OD app is an application I made for the organization I interned at from April 2023 to December 2023. I got the opportunity to design my own project as part of my internship, so I decided to make an application to complete tedious tasks and manage product data. Some of the tools included in this app are:

- Fufill Order
- Edit Measurement
- Competitor Change
- Add Jean (to database)

### Fulfill Order

The fulfill order functions as a connection to Shopify's backend. Specifically, the fulfillment of orders of customers made during the day. DHL and FedEx shipments come with an end-of-day report storing important data in a CSV file. Using that file, the app submits the data found in the CSV file into Shopify, fulfilling orders that could otherwise take an hour to finish.

### Edit Measurement

The edit measurement functions as another connection to Shopify's backend. Manually creating a table for each measurement of a product can take a long time out of a productive day, so I made a program that can instantly turn the measurements we record on Excel into measurements visible to customers through Shopify.

### Competitor Change

Competitor change tracks a certain competitor brand's price, which also has a headquarters in Tokyo. Some brands we sell overlap with their products, so keeping up with their price, especially in foreign currency, allows us to compete and take advantage of the same market.

### Add Jean

Add Jean bridges the gap between the database stored in Amazon Web Service, the 'Denim Concierge' page, and the new products we receive in our inventory. Products received can have their information typed or filled out in the app to automatically add to the database, which in turn allows customers to receive recommendations from the 'Denim Concierge' page.

The application can not be used without the correct token.
